# -*- coding: utf-8 -*-
# @Time : 2021/7/17 11:30
# @Author : menghui

from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = '自定义的管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')