from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from blogpost.models import Blogpost
from rest_framework import permissions
from rest_framework.response import Response

class BlogpostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogpost
        fields = ('title','author','body','slug')

class BlogpostSet(viewsets.ModelViewSet):
    premission_classes = (permissions.IsAuthenticatedOrReadOnly)

    serializer_class = BlogpostSerializer
    search_fields = 'title'

# 我们添加了一个名为search_fields的变量，顾名思义就是定义搜索字段。接着我们覆写了ModelViewSet的list方法，它是用于列出(list)
# 所有的结果。我们会尝试在我们的请求中获取搜索参量，如果没有的话我们就返回所有的结果。如果搜索的参数中含有标题，
# 则从所有博客中过滤出标题中含有搜索标题中的内容，再返回这些结果。如下是一个搜索的URL：
# http://127.0.0.1:8000/api/blogpost/?format = json & title = test，我们搜索标题中含有test的内容。

    def list(self, request):
        queryset = Blogpost.objects.all()

        search_param = self.request.query_params.get('title',None)
        if search_param is not None:
            queryset = Blogpost.objects.filter(title__contains=search_param)

        serializer = BlogpostSerializer(queryset,many= True)
        return Response(serializer.data)


# 在上面这个例子中，API由两个部分组成：

# ViewSets，用于定义视图的展现形式——如返回哪些内容，需要做哪些权限处理
# Serializers，用于定义API的表现形式——如返回哪些字段，返回怎样的格式
# 我们在我们的URL中，会定义相应的规则到ViewSet，而ViewSet则通过serializer_class找到对应的Serializers。
# 我们将Blogpost的所有对象赋予queryset，并返回这些值。在BlogpsotSerializer中，我们定义了我们要返回的几个字段：title、author、body、slug。