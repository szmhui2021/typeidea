from django.db import models

from blog.models import  Post

class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEM = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除')
    )

    target = models.ForeignKey(Post,verbose_name='评论目标', on_delete=models.CASCADE)
    content = models.CharField(max_length=500, verbose_name='内容')
    nickname = models.CharField(max_length=10, verbose_name='昵称')
    websit = models.URLField(verbose_name='网址')
    email = models.EmailField(verbose_name='邮箱')
    status = models.PositiveBigIntegerField(choices=STATUS_ITEM, default=STATUS_NORMAL, verbose_name='状态')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '评论'


