from django.db.models.query_utils import Q

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from upload.models import Image as ImageModel

from upload.serializers import ImageSerializer

# 이미지 등록 페이지
class ImageUploadView(APIView):
    # 이미지 등록 페이지 조회
    def get(self, request):
        return Response({})
        # return render(upload.html)

    # 새로운 이미지 만들기
    # 이미지 두장 받아서 새로운 스타일의 이미지 만들어서 반환
    def post(self, request):
        image_one = request.FILES.get("image_one", "")
        image_two = request.FILES.get("image_two", "")

        # image_one하고 image_two를 이용해서 new_image 만들기
        new_image = 0



        return Response(new_image, status=status.HTTP_200_OK)

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
        # return render(result.html)

    # 저장하기 버튼 클릭 : 이미지 저장
    def post(self, request):
        print(request.data)

        img_serializer = ImageSerializer(data=request.data)

        if img_serializer.is_valid():
            img_serializer.save()
            return Response(img_serializer.data, status=status.HTTP_200_OK)
