from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag
from typeidea.custom_site import custom_site


@admin.register(Category)
class CatgoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'is_nav', 'created','post_count']
    fields = ['name', 'status', 'is_nav', 'owner']

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CatgoryAdmin, request).save_model(request, obj, form, change)

    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = '文章总数'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'created', 'post_count']
    fields = ['name', 'status']

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)

    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = '文章总数'


class CagegoryOwnerFilter(admin.SimpleListFilter):
    title = "分类过滤器"
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id','name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','category','status', 'created','operator']
    list_display_links = []
    list_filter = [CagegoryOwnerFilter]
    search_fields = ['title','category__name']

    actions_on_top = True
    exclude = ['owner',]

    # fields = (
    #     ('category','title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )

    fieldsets = (
        ('基础配置',{
            'description':'基础配置描述',
            'fields':(
                ('title','category'),
                'status',
            )
        }),
        ('内容',{
            'fields':(
                'desc',
                'content',
            )
        }),
        ('额外信息',{
            'classes': ('collapse',),
            'fields' : ('tag',),
         })
)

    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>',
                            reverse('cus_admin:blog_post_change', args=(obj.id,)))
    operator.short_description = '操作'


    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin,self).save_model(request,obj,form,change)

    def get_queryset(self, request):
        qs = super(PostAdmin,self).get_queryset(request)
        return qs.filter(owner = request.user)
