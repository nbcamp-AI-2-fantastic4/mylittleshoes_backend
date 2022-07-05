from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from recommend.serialilzers import ShoesSerializer
from.models import Shoes, Brand

# Create your views here.


class RecommendViewAll(APIView):

    # 모든 신발 보여주기
    def get(self, request):
        allshoes = Shoes.objects.all()
        response = ShoesSerializer(allshoes, many=True).data
        return Response(response)


class RecommendViewBrand(APIView):

    # 브랜드별 신발 보여주기
    def get(self, request):  # 브랜드 id를 역참조해서 shoes 모델에 있는 object를 불러오기 ( name, )
        brand_name = request.GET.get("brand", "")
        brand_object = Brand.objects.get(name=brand_name)
        shoes_brand = Shoes.objects.filter(brand=brand_object)
        # ShoesSerializer(shoes_brand,many=True)
        return Response(ShoesSerializer(shoes_brand, many=True).data)


class RecommendViewColor(APIView):

    # 색깔별 신발 보여주기
    def get(self, request):
        color_name = request.GET.get("color", "")
        color_shoes = Shoes.objects.filter(color=color_name)
        return Response(ShoesSerializer(color_shoes, many=True).data)


class RecommendViewHeight(APIView):

    # 높이별 신발 보여주기
    def get(self, request):
        height_name = request.GET.get("height", "")
        height_shoes = Shoes.objects.filter(height=height_name)
        return Response(ShoesSerializer(height_shoes, many=True).data)