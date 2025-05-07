from django.contrib import admin
from .models import NewsUnit, Category

# admin.site.register(NewsUnit)
admin.site.register(Category)


class NewsUnitAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)
    list_display = ('title', 'category', 'author', 'pub_date')
    search_fields = ('title', 'content')
    list_filter = ('category', 'pub_date')
    fieldsets = (
        ('分類', {'fields': ['category']}),
        ('基本信息', {'fields': ['title', 'content',
         'author', 'is_show', 'click_count', 'link']}),
        ('日期', {'fields': ['pub_date']}),
        ('圖片', {'fields': ['image']}),
    )


admin.site.register(NewsUnit, NewsUnitAdmin)
