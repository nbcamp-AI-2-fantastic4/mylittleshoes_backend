from django.db import models

# 이미지 모델
class Image(models.Model):
    image_one = models.ImageField("첫번째 이미지", upload_to="img/upload_img/%Y%m%d",
    width_field=None, height_field=None, max_length=150)

    image_two = models.ImageField("두번째 이미지", upload_to="img/upload_img/%Y%m%d",
    width_field=None, height_field=None, max_length=150)

    image_result = models.ImageField("결과 이미지", upload_to="img/upload_img/%Y%m%d",
    width_field=None, height_field=None, max_length=150)
