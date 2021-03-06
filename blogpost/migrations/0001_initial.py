# Generated by Django 2.0.1 on 2018-02-01 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='标题')),
                ('author', models.CharField(max_length=100, unique=True, verbose_name='作者')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('body', models.TextField(verbose_name='正文')),
                ('posted', models.DateField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='称呼')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('content', models.TextField(max_length=140, verbose_name='内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('blog', models.ForeignKey(on_delete=True, to='blogpost.Blogpost', verbose_name='博客')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='名称')),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(default='test', on_delete=True, to='blogpost.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tag',
            field=models.ManyToManyField(default='test', to='blogpost.Tag', verbose_name='标签'),
        ),
    ]
