"""blog URL Configuration
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from blogpost import views as blogpostViews
from django.contrib.sitemaps.views import sitemap
from sitemap.sitemaps import *
from rest_framework import routers
from blogpost.api import BlogpostSet
from blogpost.views import index

apiRouter = routers.DefaultRouter()
apiRouter.register(r'blogpost',BlogpostSet,'Blogpost')

sitemaps = {
    "page" : PageSitemap ,
    'flatpages' : FlatPageSitemap ,
    'blogpages' : BlogSitemap ,
}

urlpatterns = [
    url(r'^$', index,name='main'),
    url(r'^blog/(?P<slug>[^\.]+).html', blogpostViews.view_post, name='view_blog_post'),
    url(r'^admin/', admin.site.urls),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^sitemap\.xml$',sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^api/',include(apiRouter.urls)),
    ] + static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)


# 指向首页，其view是index
# 指向博客详情页，其view是view_post
# 指向博客详情页的URL正则r'^blog/(?P<slug>[^\.]+).html，会将形如blog/hello-world.html中的hello-world提取出来作为参数传给view_post方法。
