"""day16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app01.views import user,depart,pretty,admin,account,chart,upload,city
from django.urls import path,re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT},name='media'),

    # 部门管理
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    path('depart/<int:nid>/edit/', depart.depart_edit),
    path('depart/multi/', depart.depart_multi),
    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),
    # 靓号管理
    path('pretty/list/', pretty.pretty_list),
    path('pretty/add/', pretty.pretty_add),
    path('pretty/<int:nid>/edit/', pretty.pretty_edit),
    path('pretty/<int:nid>/delete/', pretty.pretty_delete),
    # 管理员的管理
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),
    # 登录
    path('login/', account.login),
    path('logout/', account.logout),

    # 数据统计
    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),
    path('chart/pie/', chart.chart_pie),
    # 上传文件
    path('upload/list/', upload.upload_list),
    path('upload/form/', upload.upload_form),
    path('upload/modelform/', upload.upload_modelform),

    # 城市
    path('city/list/',city.city_list),
    path('city/add/',city.city_add),

]

