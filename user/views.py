from django.shortcuts import render
from .models import User, UserProfile
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from django.contrib.auth import login, authenticate, logout

from .serializers import UserSerializer
from history.models import History, Like
import json

# 로그인/로그아웃 기능
class UserView(APIView):
    permission_classes = [permissions.AllowAny]

    # 로그인 기능
    def post(self, request):
        login_data = {
            'email': request.data.get('email', ''),
            'password': request.data.get('password', ''),
        } 
        user = authenticate(request, **login_data)
        
        if not user:
            msg = '아이디 또는 패스워드를 확인해주세요.'
            return Response({'message': msg}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)

        id = user.id
        msg = '로그인 성공!'
        return Response({'message': msg, 'id': id, 'fullname': user.fullname, 'email': user.email}, status=status.HTTP_200_OK)

    # 로그아웃 기능
    def delete(self, request):
        logout(request)
        msg = '로그아웃 성공!'
        return Response({'message': msg}, status=status.HTTP_200_OK)

# 회원 정보 기능
class UserInfoView(APIView):
    # 회원 정보 조회
    def get(self, request):
        user = request.user
        
        if not user.is_authenticated:
            msg = '로그인을 해주세요'
            return Response({'message': msg}, status=status.HTTP_400_BAD_REQUEST)

        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

    # 회원가입
    def post(self, request):
        signup_data = json.loads(request.body)
        user_serializer = UserSerializer(data=signup_data)
        if user_serializer.is_valid():  # validation
            user_serializer.save()      # create
            return Response({'message': '저장 완료!'}, status=status.HTTP_200_OK)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # 회원수정
    def put(self, request):
        user = request.user

        confirm_data = { 
            'email': user.email,
            'password': request.data.get('password_old', ''),
        }
        user = authenticate(request, **confirm_data)
        if not user:
            return Response({'message': '비밀번호를 확인해주세요.'}, status=status.HTTP_400_BAD_REQUEST)

        if request.data.get('password_new'):
            request.data['password'] = request.data.get('password_new')

        user_serializer = UserSerializer(user, data=request.data, partial=True)
        if user_serializer.is_valid():  # validation
            user_serializer.save()      # update
            return Response({'message': '저장 완료!'}, status=status.HTTP_200_OK)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 회원탈퇴
    def delete(self, request):
        confirm_word = request.data.get('confirm_word', '')
        if confirm_word != '확인':
            return Response({'error': '회원 탈퇴 확인 메시지를 정확히 입력해주세요'}, 
                             status=status.HTTP_400_BAD_REQUEST)

        email = request.user.email
        password = request.data.get('password', '')
        
        confirm_data = { 
            'email': email,
            'password': password,
        }

        user = authenticate(request, **confirm_data)
        if not user:
            return Response({'error': '비밀번호를 확인해주세요.'}, status=status.HTTP_400_BAD_REQUEST)

        logout(request)
        user.delete()

        return Response({'message': '삭제 성공!'}, status=status.HTTP_200_OK)

# 회원 히스토리 기능
class UserHistoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # 회원 히스토리 조회 기능
    def get(self, request):
        histories = History.objects.filter(user=request.user)
        history_ids = [history.id for history in histories]
        return Response(history_ids, status=status.HTTP_200_OK)

# 회원 히스토리 좋아요 기능
class UserHistoryLikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # 좋아요누른 히스토리 조회 기능
    def get(self, request):
        likes = Like.objects.filter(user=request.user)
        histories = [like.history for like in likes]
        history_ids = [history.id for history in histories]
        return Response(history_ids, status=status.HTTP_200_OK)