from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import Http404
from blogpost.models import Blogpost
from .forms import CommentForm
from .models import Comment

def index(request):
    ctx = {
        'posts':Blogpost.objects.all().order_by('-posted')
    }

    return render(request,'../templates/index.html', ctx
                  )

# Django的render_to_response方法可以根据一个给定的上下文字典渲染一个给定的目标，并返回渲染后的HttpResponse。即将相应的值，
# 如这里的Blogpost.objects.all()[:5]，填入相应的index.html中，再返回最后的结果。


# 依据拿到的slug，我们就可以创建对应的详情页的view，代码如下所示：

def view_post(request, slug):
    try:
        blog = get_object_or_404(Blogpost, slug=slug)
    except Blogpost.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)

    ctx = {
        'blog':blog,
        'comments':blog.comment_set.all().order_by('-created'),
        'form':form
    }
    return render(request,'../templates/blogpost_detail.html',ctx)
    # return render_to_response('../templates/blogpost_detail.html', {
    #     'post': get_object_or_404(Blogpost, slug=slug)
    # })

# 这里的get_object_or_404将会根据slug来获取相应的博客，如果取不出相应的博客就会返回404。因此，我们的详情页和上面的列表页也是类似的。
