from django.db.models.query_utils import Q

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from upload.models import Image as ImageModel

from upload.serializers import ImageSerializer

# 이미지 등록 페이지
class ImageUploadView(APIView):
    #
    def get(self, request):
        return Response({})

    # 이미지 등록 : 이미지 저장
    def post(self, request):
        # ERD 설계를 조금 바꿔야 하는가?
        # 기존 : ImageModel(one, two) 2장, HistoryModel(result) 1장
        # 등록한 이미지 2장 (one, two), 결과 이미지 1장 (result)
        # 총 3장의 이미지를 반환해야 하는데, 어떻게 반환할 것인가? 고민

        # 결론
        # 등록한 이미지 2장 (one, two)
        # 결과 모델에 이미지 2장을 넣고 돌려서 나온 결과 이미지 1장
        # 총 3장을 하나의 모델(Image)에 저장
        
        img_one = request.FILES.get("image_one", "")
        img_two = request.FILES.get("image_two", "")

        # 해당 부분에 결과 모델 불러와서 사용
        # request받은 one, two 이미지를 넣어서 결과 이미지를 img_result에 넣어줌
        # img_result = ResultModel(img_one=img_one, img_two=img_two) # ??
        img_result = request.FILES.get("image_result", "")

        # 이미지 시리얼라이저 사용
        # img_serializer = ImageSerializer(img_result, data=request.data)
        img_serializer = ImageSerializer(data=request.data)

        # # validate 사용 시 검증, HTTP 200 반환
        # if img_serializer.is_valid():
        #     img_serializer.save()
        #     return Response(img_serializer.data, status=status.HTTP_200_OK)
        # # 검증 실패 시 .errors를 사용하여 실패 구간 확인, HTTP 400 반환
        # return Response(img_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(img_serializer.data, status=status.HTTP_200_OK)

# 이미지 결과 페이지
class ImageResultView(APIView):
    # 이미지 3장 불러오기
    def get(self, request):
        # 로그인한 유저, 
        return Response({})

    # 저장하기 버튼 클릭 : 히스토리 저장
    def post(self, request):
        return Response({})

    # 
    def delete(self, request):
        return Response({})
