from django.shortcuts import render
from .models import User, UserProfile
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from django.contrib.auth import login, authenticate, logout

from .serializers import UserSerializer


# 로그인/로그아웃 기능
class UserView(APIView):
    permission_classes = [permissions.AllowAny]

    # 로그인 기능
    def post(self, request):
        user = authenticate(request, **request.data)
        
        if not user:
            msg = '아이디 또는 패스워드를 확인해주세요.'
            return Response({'message': msg}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)
        msg = '로그인 성공!'
        return Response({'message': msg}, status=status.HTTP_200_OK)

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
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():  # validation
            user_serializer.save()      # create
            return Response({'message': '저장 완료!'}, status=status.HTTP_200_OK)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # 회원수정
    def put(self, request):
        user = request.user

        password = request.data.get('password_old', '')
        confirm_data = { 
            'email': user.email,
            'password': password,
        }
        user = authenticate(request, **confirm_data)
        if not user:
            return Response({'message': '비밀번호를 확인해주세요.'}, status=status.HTTP_400_BAD_REQUEST)

        if request.data.get('password_new'):
            password = request.data.get('password_new')
        
        request.data['password'] = password

        user_serializer = UserSerializer(user, data=request.data, partial=True)
        if user_serializer.is_valid():  # validation
            user_serializer.save()      # update
            return Response({'message': '저장 완료!'}, status=status.HTTP_200_OK)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 회원탈퇴
    def delete(self, request):
        return Response({})