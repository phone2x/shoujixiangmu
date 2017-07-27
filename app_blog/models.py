# # -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app_main.models import User
# Create your models here.


#博客

# class BlogAd(models.Model):
#     img_url = models.ImageField(upload_to='uploads/')
#
#
#     class Meta():
#         verbose_name = '博客广告'
#         verbose_name_plural = verbose_name


#博客导航条
class navbars_blog(models.Model):
    NavName = models.CharField(max_length=10, null=False)
    NavHref = models.CharField(max_length=20, null=False)

    class Meta:
        verbose_name = '博客导航'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.NavName

# 文章分类
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    index = models.IntegerField(default=999,verbose_name='分类的排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.name


# 自定义一个文章Model管理器
class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y/%m') + '文章存档'
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list


# 文章模型
class Article(models.Model):
    author = models.CharField(max_length=20, verbose_name='作者名字', null=False)
    title = models.CharField(max_length=50, verbose_name='文章标题', null=False)
    top_img = models.ImageField(upload_to='blog_img/%Y/%m.%d', blank=True, null=True, verbose_name='博客首图片')
    desc = models.CharField(max_length=150, verbose_name='文章描述', null=False)
    content = models.TextField(verbose_name='文章内容', null=False)
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间', null=False)
    collect_count = models.IntegerField(default=0, verbose_name=u'收藏次数')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类')
    # tag = models.ManyToManyField(Tag, verbose_name='标签')

    # 关联管理器
    objects = ArticleManager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.title


# 评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='登录用户')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='关联文章')
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return str(self.id)


#　视频模型
#
# class Video(models.Model):
#     name = models.CharField(max_length=30)
#     video_url = models.CharField(u'视频资源URL',max_length=200)
#     video_length = models.IntegerField(u'视频长度')
#
#     class Meta():
#         verbose_name = '视频'
#         verbose_name_plural =verbose_name
#
#     def __str__(self):
#         return self.name.encode('utf-8')


#产品图片

# class ProPic(models.Model):
#     title = models.CharField(max_length=30)
#     name = models.CharField(max_length=30)
#     img_url = models.ImageField(upload_to='uploads/')
#
#     class Meta():
#         verbose_name = "产品图片"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.title.encode('utf-8')


# 新闻　
#
# class News(models.Model):
#     title = models.CharField(max_length=50, verbose_name='新闻标题')
#     desc = models.CharField(max_length=50, verbose_name='新闻描述')
#     content = models.TextField(verbose_name='新闻内容')
#     click_count = models.IntegerField(default=0, verbose_name='点击次数')
#     is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
#     date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
#     user = models.ForeignKey(UserInfo, verbose_name='用户')
#     collect_count = models.IntegerField(default=0, verbose_name=u'收藏次数')
#
#     class Meta():
#         verbose_name = '新闻'
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.title
