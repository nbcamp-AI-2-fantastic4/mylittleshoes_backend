from django.db.models.query_utils import Q

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from upload.models import Image as ImageModel

from upload.serializers import ImageSerializer

# 이미지 등록 페이지
class ImageUploadView(APIView):
    # 이미지 등록 : 이미지 저장
    def post(self, request):
        image_one = request.FILES.get("image_one", "")
        image_two = request.FILES.get("image_two", "")

        image_result = request.FILES.get("image_result", "")

        return Response(image_one, image_two, image_result ,status=status.HTTP_200_OK)

# 이미지 결과 페이지
class ImageResultView(APIView):
    # 이미지 3장 불러오기
    def get(self, request):
        # GET 요청으로 image에 대한 정보들 불러오기?
        image_one = request.GET.get("image_one", "")
        image_two = request.GET.get("image_two", "")
        image_result = request.GET.get("image_result", "")

        image_serializer = ImageSerializer(image_one=image_one, image_two=image_two, image_result=image_result)

        return Response(image_serializer.data, status=status.HTTP_200_OK)

    # 저장하기 버튼 클릭 : 이미지, 히스토리 저장
    def post(self, request):
        img_serializer = ImageSerializer(data=request.data)

        if img_serializer.is_valid():
            img_serializer.save()
            return Response(img_serializer.data, status=status.HTTP_200_OK)
