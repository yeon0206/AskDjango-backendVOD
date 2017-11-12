#blog/admin.py
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag

# 등록법 1
# admin.site.register(Post) # 기본 ModelAdmin으로 등록
# # admin.site.unregister(Post)


# 등록법 2
# class PostAdmin(admin.ModelAdmin):
#     list_display=['id','title','created_at','updated_at']

# admin.site.register(Post, PostAdmin)


#등록법 3
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','tag_list','content_size','status','created_at','updated_at']
    list_display_links=['title']
    actions=['make_draft','make_published']
    

    # Post에서 Tag로의 접근 호출
    def tag_list(request, post):
        return ',' .join(tag.name for tag in post.tag_set.all()) # list comprehension
    
    #prefetch_related를 통해 sql수를 줄임
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('tag_set')

    

    def content_size(self,post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description='글자수'
    # content_size.allow_tags=True #django 1.9부터 삭제예정

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d') # QeurySet.update 
        self.message_user(request, '{}건의 포스팅을 draft상태로 변경'.format(updated_count)) # django message framework 활용
    make_draft.short_description = '지정 포스팅을 draft상태로 변경합니다.'

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p') # QeurySet.update 
        self.message_user(request, '{}건의 포스팅을 Published상태로 변경'.format(updated_count)) # django message framework 활용
    make_published.short_description = '지정 포스팅을 Published상태로 변경합니다.'


'''
2. list_display에 'content_size'를 필드로 넣었는데 이는 1급함수를 호출하는 방식으로 넣어 admin페이지에서 각 list row마다 함수를 호출하는 건가요?
3, content_size.short_description 옵션을 list_display 보다 밑에 썼는데 파이썬은 이를 어떻게 해석하는지 궁금합니다.
답변2) list_display 에 함수가 지정될 경우, 각 Row마다 개별적으로 호출됩니다.
답변3) admin 에서는 list_display 에 지정된 attr에 short_description 값이 지정되어있을 경우 이를 label로서 활용합니다. 미지정시에는 attr 의 description 이나 함수명이 사용됩니다.
'''

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','author','post_content_len']
    
    # 첫번째 방법 ModelAdmin에 list_select_related 옵션사용 sql을 줄인다
    # list_select_related = ['post']

    def post_content_len(self, comment):
        return '{}글자'.format(len(comment.post.content))

    # 두번째 방법 직접 멤버함수 재정의
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('post')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']