"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import  include, url
from django.conf.urls.static import static

urlpatterns = [
    (r'^$','blogpost.views.index'),
    url(r'^blog/(?P<slug>[^\.]+).html','blogpost.views.view_post',name='view_blog_post'),
    url(r'^admin/',include(admin.site.urls))
]

# 在上面的代码里，我们创建了两个route：

# 指向首页，其view是index
# 指向博客详情页，其view是view_post
# 指向博客详情页的URL正则r'^blog/(?P<slug>[^\.]+).html，会将形如blog/hello-world.html中的hello-world提取出来作为参数传给view_post方法。
