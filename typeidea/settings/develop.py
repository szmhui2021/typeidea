# -*- coding: utf-8 -*-
# @Time : 2021/7/16 8:02
# @Author : menghui
# 开发环境的配置

from .base import * #NOQA注释:PEP8规范检测工具,这个地方需要检测

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
