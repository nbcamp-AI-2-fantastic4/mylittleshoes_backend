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

    # 이미지 등록 : 이미지 저장
    def post(self, request):
        # 등록한 이미지 2장 (one, two)
        # 결과 모델에 이미지 2장을 넣고 돌려서 나온 결과 이미지 1장
        # 총 3장을 하나의 모델(Image)에 저장
        
        image_one = request.FILES.get("image_one", "")
        image_two = request.FILES.get("image_two", "")

        # 해당 부분에 결과 모델 불러와서 사용
        # request받은 one, two 이미지를 넣어서 결과 이미지를 img_result에 넣어줌
        # img_result = ResultModel(img_one=img_one, img_two=img_two) # ??
        image_result = request.FILES.get("image_result", "")

        # 이미지 시리얼라이저 사용
        # img_serializer = ImageSerializer(img_result, data=request.data)
        # img_serializer = ImageSerializer(data=request.data)
        # img_serializer = ImageModel(image_one=img_one, image_two=img_two, image_result=img_result)

        # validate 사용 시 검증, HTTP 200 반환
        # if img_serializer.is_valid():
        #     img_serializer.save()
        #     return Response(img_serializer.data, status=status.HTTP_200_OK)

        # 검증 실패 시 .errors를 사용하여 실패 구간 확인, HTTP 400 반환
        # return Response(img_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # ??
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
        # return render(result.html)

    # 저장하기 버튼 클릭 : 이미지, 히스토리 저장
    def post(self, request):
        request.data["image_one"] = request.data
        request.data["image_two"] = request.data
        request.data["image_result"] = request.data

        img_serializer = ImageSerializer(data=request.data)

        if img_serializer.is_valid():
            img_serializer.save()
            return Response(img_serializer.data, status=status.HTTP_200_OK)
