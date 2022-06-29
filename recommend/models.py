from django.db import models


# Create your models here.


# 신발 브랜드 
class Brand(models.Model):
    name = models.CharField(max_length=100)

# 신발 추천 모델
class Shoes(models.Model):
    STATUS_HEIGHT = (
        ('low', '로우'),
        ('middle', '미드'),
        ('high', '하이'),
    )
    STATUS_COLOR = (
     ('red', '빨간색'),
     ('orange', '주황색'),
     ('yellow', '노란색'),
     ('green', '초록색'),
     ('blue', '파란색'),
     ('indigo','남색'),
     ('purple','보라색'),
     ('white','하얀색'),
     ('black','검은색'),
     ('other', '기타'),
    )
    brand = models.ForeignKey(Brand, verbose_name="브랜드", on_delete=models.CASCADE)
    name = models.CharField(max_length=100,unique=True)
    color = models.CharField("색깔", choices=STATUS_COLOR, max_length=10)
    height = models.CharField("높이", choices=STATUS_HEIGHT, max_length=10)
    image = models.ImageField('신발 이미지', upload_to="static/")

    