#blog/models.py
import re
from django.db import models
from django.forms import ValidationError

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value): # [+-]? : +,- 가 없거나 한개있으면
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name='제목',
        help_text='포스팅 제목을 입력해주세요. 최대 100자 내외. ') #길이 제한있는 문자열
    content = models.TextField(verbose_name='내용')            #길이 제한이 없는 문자열(쿼리성능이 안좋아져서 타이트하게 지정)
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=100, blank=True, 
        validators=[lnglat_validator], #함수자체를 넘김
        help_text='경도/위도 포맷으로 입력')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
