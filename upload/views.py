import json
from django.db.models.query_utils import Q

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from upload.models import Image as ImageModel

from upload.serializers import ImageSerializer
import os
from PIL import Image

from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from mylittleshoes import settings

from history.serializers import HistorySerializer
from history.models import History as HistoryModel
from user.models import User as UserModel

IMAGE_WIDTH = 100
IMAGE_HEIGHT = 100

def resize_image(image_field, width=IMAGE_WIDTH, height=IMAGE_HEIGHT, name=None):
    """
    Resizes an image from a Model.ImageField and returns a new image as a ContentFile
    """
    img = Image.open(image_field)
    if img.size[0] > width or img.size[1] > height:
        new_img = img.resize((width, height))
    buffer = BytesIO()
    new_img.save(fp=buffer, format='JPEG')
    return ContentFile(buffer.getvalue())



# 이미지 등록 페이지
class ImageUploadView(APIView):
    # 이미지 등록 페이지 조회
    def get(self, request):
        return Response({})

    # 새로운 이미지 만들기
    # 이미지 두장 받아서 새로운 스타일의 이미지 만들어서 반환
    def post(self, request):
        content = request.FILES.get("image_one", "") 
        style = request.FILES.get("image_two", "")

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        content_path = BASE_DIR + '\content.png'
        style_path = BASE_DIR + '\style.png'

        with open(content_path, 'wb+') as destination:
            for chunk in content.chunks():
                destination.write(chunk)

        with open(style_path, 'wb+') as destination:
            for chunk in style.chunks():
                destination.write(chunk)

        os.system('style_transfer content.png style.png')

        output_path = 'out.png'
            
        return Response({'output_path': output_path}, status=status.HTTP_200_OK)

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

    # 저장하기 버튼 클릭 : 이미지 저장
    def post(self, request):
        data = json.loads(request.body)
        user_id = data['user']

        image_object = ImageModel()
        
        image_one = Image.open('content.png')
        image_file = BytesIO()
        image_one.save(image_file, image_one.format)
        image_object.image_one.save('content.png',
                                    InMemoryUploadedFile(
                                        image_file,
                                        None, 'content.png',
                                        'image/png',
                                        image_one.size,
                                        None),
                                    save=False)
        image_one.close()

        image_two = Image.open('style.png')
        image_file = BytesIO()
        image_two.save(image_file, image_two.format)
        image_object.image_two.save('style.png',
                                    InMemoryUploadedFile(
                                        image_file,
                                        None, 'style.png',
                                        'image/png',
                                        image_two.size,
                                        None),
                                    save=False)
        image_two.close()

        image_result = Image.open('out.png')
        image_file = BytesIO()
        image_result.save(image_file, image_result.format)
        image_object.image_result.save('out.png',
                                    InMemoryUploadedFile(
                                        image_file,
                                        None, 'out.png',
                                        'image/png',
                                        image_result.size,
                                        None),
                                    save=False)
        image_result.close()

        image_object.save()

        history_data = {
            'exposure_start': "2022-06-30 00:00:00",
            'exposure_end': "2023-06-30 00:00:00",
        }
        
        user = UserModel.objects.get(id=user_id)

        history_serializer = HistorySerializer(data=history_data)
        if history_serializer.is_valid():
            history_serializer.save(user=user, image=image_object)


        return Response({'message': '저장 완료!'},status=status.HTTP_200_OK)       