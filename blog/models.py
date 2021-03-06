#blog/models.py
import re
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.forms import ValidationError
from imagekit.models import ImageSpecField,ProcessedImageField
from imagekit.processors import Thumbnail

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value): # [+-]? : +,- 가 없거나 한개있으면
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    # author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name='제목',
        help_text='포스팅 제목을 입력해주세요. 최대 100자 내외. ') #길이 제한있는 문자열
    content = models.TextField(verbose_name='내용')            #길이 제한이 없는 문자열(쿼리성능이 안좋아져서 타이트하게 지정)
    
    # 1) 원본이미지 저장, 썸네일 처리
    # photo = models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d') #pillow 설치필요, upload_to상대경로
    # photo_thumbnail = ImageSpecField(source='photo',
    #         processors=[Thumbnail(300,300)],
    #         format = 'JPEG',
    #         options={'quality':60},
    #         )
    
    # 2) 원본 이미지 저장 없이, 썸네일 처리
    photo = ProcessedImageField(blank=True, upload_to='blog/post/%Y/%m/%d',
            processors=[Thumbnail(300,300)],
            format = 'JPEG',
            options={'quality':60},
            )

    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=100, blank=True, 
        validators=[lnglat_validator], #함수자체를 넘김
        help_text='경도/위도 포맷으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True) #같은 앱에 있는 Tag라는 모델과 relation을 건다. 다른앱: 'auth.Tag'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])
    # 해당 post=Post.object.first() 
    # resolve_url(post) 이함수는 인자에 get_absolute_url 어트리뷰트가 있는지 확인해서 있으면 그 함수를 호출,리턴해줌
    

class Comment(models.Model):
    post = models.ForeignKey(Post) #post_id
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
    
    def get_edit_url(self):
        return reverse('blog:comment_edit', args=[self.post.id, self.id])
    def get_delete_url(self):
        return reverse('blog:comment_delete', args=[self.post.id, self.id])

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name