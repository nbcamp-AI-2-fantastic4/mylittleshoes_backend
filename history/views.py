from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from datetime import datetime, timedelta
from django.utils import timezone


class HistoryView(APIView):

    # 결과 히스토리 조회
    def get(self, request):
        return Response({"msg":"get 요청"})
    
    # 결과 히스토리 저장
    def post(self, request):
        return Response({"msg":"post 요청"})


class CommentView(APIView):

    # 댓글 조회
    def get(self, request):
        return Response({"msg":"get 요청"})

    # 댓글 작성
    def post(self, request):
        return Response({"msg":"post 요청"})

    # 댓글 수정
    def put(self, request):
        return Response({"msg":"put 요청"})

    # 댓글 삭제
    def delete(self, request):
        return Response({"msg":"delete 요청"})