from django.db import models

from datetime import datetime, timedelta
from django.utils import timezone

from user.models import User
from upload.models import Image

# 히스토리 모델
class History(models.Model):
    user = models.ForeignKey(User, verbose_name='사용자', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, verbose_name='사용된 이미지', on_delete=models.CASCADE)
    created_at = models.DateTimeField('등록일', auto_now_add=True)
    exposure_start = models.DateField('노출 시작일', default="2022-06-29 00:00:00")
    exposure_end = models.DateField('노출 종료', default="2022-07-29 00:00:00")

    def __str__(self):
        return self.created_at

# 코멘트 모델
class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='사용자', on_delete=models.CASCADE)
    history = models.ForeignKey(History, verbose_name='결과 히스토리', on_delete=models.CASCADE)
    content = models.CharField('댓글 내용', max_length=100)

    def __str__(self):
        return self.content

# 좋아요 모델
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    history = models.ForeignKey(History, on_delete=models.CASCADE)