from django.contrib import admin
from .models import History, Like, Comment
from django.utils.html import mark_safe

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id','image_preview','user', 'created_at')  # object 목록에 띄워줄 필드를 지정한다.
    list_display_links = ('id','user', 'created_at')         # object 목록에서 클릭 시 상세 페이지로 들어갈 수 있는 필드를 지정한다.
    # list_filter = ('username', )                # filter를 걸 수 있는 필드를 생성한다.
    search_fields = ('user',)     # 검색에 사용될 필드를 지정한다.

    fieldsets = (                               # 상세페이지에서 필드를 분류하는데 사용된다.
        ("info", {'fields': ('user', 'created_at', 'exposure_start','exposure_end')}),
        ('image', {'fields': ('image', 'image_tag', )}),)

    # filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):   # 상세페이지에서 읽기 전용 필드를 설정할 때 사용된다.
        if obj:
            return ('user', 'created_at', 'image', 'image_tag', )
        
    def image_tag(self, obj):
        if obj.image.image_result:
            return mark_safe(f'<img src="{obj.image.image_result.url}" width="150" height="150"/>')
        return None

    def image_preview(self, obj):
        if obj.image.image_result:
            return mark_safe(f'<img src="{obj.image.image_result.url}" width="100" height="100"/>')
        return None

admin.site.register(History, HistoryAdmin)
admin.site.register(Like)
admin.site.register(Comment)