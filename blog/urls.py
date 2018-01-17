"""blog URL Configuration
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from blogpost import views as blogpostViews


urlpatterns = [
    url(r'^$', blogpostViews.index),
    url(r'^blog/(?P<slug>[^\.]+).html', blogpostViews.view_post, name='view_blog_post'),
    url(r'^admin/', admin.site.urls)
]

# 在上面的代码里，我们创建了两个route：

# 指向首页，其view是index
# 指向博客详情页，其view是view_post
# 指向博客详情页的URL正则r'^blog/(?P<slug>[^\.]+).html，会将形如blog/hello-world.html中的hello-world提取出来作为参数传给view_post方法。
