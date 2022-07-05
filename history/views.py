from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models.query_utils import Q

from history.models import History, Comment, Like
from upload.models import Image
from user.models import User
from history.serializers import CommentSerializer, HistorySerializer
import json

class HistoryView(APIView):

    # 결과 히스토리 조회
    def get(self, request):
        
        today = timezone.now()
        query = (
            Q(exposure_start__lte = today) & 
            Q(exposure_end__gte = today)
        )

        # 노출일자 사이에 해당되는 히스토리를 최신순으로 가져온다.
        histories = History.objects.filter(query).order_by('-id')
        
        # histories 쿼리셋을 시리얼라이저
        histories_serializer = HistorySerializer(histories, many=True).data
        return Response({"result_history":histories_serializer}, status=status.HTTP_200_OK)
    
    # 결과 히스토리 저장
    def post(self, request):
        # request.data['user']=request.user.id
        print(request.data)
        image_id = request.data.get("image","")
        image_obj = Image.objects.get(id=image_id)

        history_serializer = HistorySerializer(data=request.data)

        if history_serializer.is_valid():
            history_serializer.save(user=request.user, image=image_obj)
            return Response(history_serializer.data, status=status.HTTP_200_OK)
        
        return Response(history_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentView(APIView):

    # 댓글 조회
    def get(self, request, history_id):
        history = History.objects.get(id=history_id)
        history_serializer = HistorySerializer(history).data

        comments = Comment.objects.filter(history_id=history_id)
        comment_serializer = CommentSerializer(comments, many=True).data
        
        print(history_serializer)
        print(comment_serializer)
        
        return Response({ "result_history": history_serializer,
                          "result_comment": comment_serializer}, 
                          status=status.HTTP_200_OK)

    # 댓글 작성
    def post(self, request, history_id):
        data = json.loads(request.body)
        data['history'] = history_id
        user = User.objects.get(id=int(data['user'])) 

        comment_serializer = CommentSerializer(data=data)
        
        if comment_serializer.is_valid():
            comment_serializer.save(user=user)
            comments = Comment.objects.filter(history_id=history_id)
            return Response(CommentSerializer(comments, many=True).data, status=status.HTTP_200_OK)
        
        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 댓글 수정
    def put(self, request, comment_id):
        print(comment_id)
        comment = Comment.objects.get(id=comment_id)

        comment_serializer = CommentSerializer(comment, data=request.data, partial=True)
        
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=status.HTTP_200_OK)
        
        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 댓글 삭제
    def delete(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return Response({"msg":"delete 요청"})


class LikeView(APIView):

    # 좋아요 저장
    def post(self, request, history_id):

        history = History.objects.get(id=history_id)

        if User.objects.get(history=history):
            return Response({"msg":"이미 좋아요를 누름"})

        Like.objects.create(user=request.user, history=history)
        return Response({"msg":"post 요청"})

    # 좋아요 취소
    def delete(self, request, history_id):
        
        history = History.objects.get(id=history_id)
        likes = Like.objects.filter(history=history)
        user_like = likes.get(user=request.user)

        user_like.delete()
        return Response({"msg":"delete 요청"})