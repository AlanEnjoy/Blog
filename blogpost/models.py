from django.db import models
from django.db.models import permalink


class Category(models.Model):
    """
    分类
    """
    name = models.CharField('名称', max_length=16)


class Tag(models.Model):
    """
    标签
    """
    name = models.CharField('名称', max_length=16)

class Blogpost(models.Model):
    """
    博客
    """
    title = models.CharField('标题',max_length=100,unique=True)
    author = models.CharField('作者',max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    body = models.TextField('正文')
    posted = models.DateField(db_index=True , auto_now_add=True)

    category = models.ForeignKey(Category, verbose_name='分类',on_delete= True,default='test')
    tag = models.ManyToManyField(Tag,verbose_name='标签',default='test')

    def __unicode__(self):
        return '%s' %self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None , {'slug': self.slug})


class Comment(models.Model):
    """
    评论
    """
    blog = models.ForeignKey(Blogpost, verbose_name='博客',on_delete= True)

    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.TextField('内容',max_length= 140)
    created = models.DateTimeField('发布时间',auto_now_add=True)


