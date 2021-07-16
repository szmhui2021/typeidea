from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEM=(
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除')
    )

    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveBigIntegerField(choices=STATUS_ITEM, default=STATUS_NORMAL, verbose_name='状态')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
       verbose_name = verbose_name_plural = '分类' #模型名称

class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEM = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除')
    )

    name = models.CharField(max_length=10, verbose_name='名称')
    status = models.PositiveBigIntegerField(choices=STATUS_ITEM, default=STATUS_NORMAL, verbose_name='状态')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '标签'

class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DARFT = 2
    STATUS_ITEM = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DARFT, '草稿')
    )

    title = models.CharField(max_length=250, verbose_name='标题')
    desc = models.CharField(max_length=1024, blank=True, verbose_name='摘要')
    content = models.TextField(help_text='正文必须为MarkDown格式', verbose_name='正文')
    status = models.PositiveBigIntegerField(choices=STATUS_ITEM, default=STATUS_NORMAL, verbose_name='状态')
    category = models.ForeignKey(Category, verbose_name='分类',on_delete=models.CASCADE)
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']                  #以降序从后往前排序






