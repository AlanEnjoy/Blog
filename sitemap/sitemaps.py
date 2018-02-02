from django.contrib.sitemaps import  Sitemap
from django.urls import reverse
from blogpost.models import Blogpost
from django.apps import apps as django_apps

class PageSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['main']

    def location(self, item):
        return reverse(item)

# 它定义了自己的priority是最高的1.0，同时每新频率为daily。然后在items里面去取它所要获取的URL，
# 即urls.py中对应的name的main的URL。在这里我们只返回了main一个值，依据于下面的location方法中的reverse，
# 它找到了main对应的URL，即首页。


class BlogSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return Blogpost.objects.all()

    def lastmod(self, obj):
        return obj.posted

# 与上面相同，我们需要在items方法中返回所有的博客内容。并且在lastmod中返回这篇博客的发表日期，以免他们返回的是同一信息


class FlatPageSitemap(Sitemap):
    priority = 0.8

    def items(self):
        Site = django_apps.get_model('sites.Site')
        current_site = Site.objects.get_current()
        return current_site.flatpage_set.filter()

# 这个方法可能会稍微麻烦一些，我们需要从数据库中取出当前的站点。
# 再取出当前站点中的flatpage集合，对过滤那些不需要注册的页面，即代码中的registration_required = False。