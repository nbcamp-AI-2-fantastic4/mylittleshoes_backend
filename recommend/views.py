from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


# Create your views here.



class RecommendViewAll(APIView):

    #모든 신발 보여주기
    def get(self, request):
        return Response({"msg":"get 요청"})




class RecommendViewBrand(APIView):

    #브랜드별 신발 보여주기
    def get(self, request):
        return Response({"msg":"get 요청"})



class RecommendViewColor(APIView):
    
    #색깔별 신발 보여주기
    def get(self, request):
        return Response({"msg":"get 요청"})



class RecommendViewHeight(APIView):
    
    #높이별 신발 보여주기
    def get(self, request):
        return Response({"msg":"get 요청"})