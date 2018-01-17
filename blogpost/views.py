from django.shortcuts import render, render_to_response, get_object_or_404
from blogpost.models import Blogpost

def index(request):
    return render_to_response('index.html', {
        'posts': Blogpost.objects.all()[:5]
    })

# Django的render_to_response方法可以根据一个给定的上下文字典渲染一个给定的目标，并返回渲染后的HttpResponse。即将相应的值，
# 如这里的Blogpost.objects.all()[:5]，填入相应的index.html中，再返回最后的结果。


# 依据拿到的slug，我们就可以创建对应的详情页的view，代码如下所示：

def view_post(request, slug):
    return render_to_response('blogpost_detail.html', {
        'post': get_object_or_404(Blogpost, slug=slug)
    })

# 这里的get_object_or_404将会根据slug来获取相应的博客，如果取不出相应的博客就会返回404。因此，我们的详情页和上面的列表页也是类似的。