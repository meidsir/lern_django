from django.db import models


class Myblogs(models.Model):
    class Meta:
        verbose_name = u"我的博客"
        verbose_name_plural = u"我的博客"
    title = models.CharField(verbose_name='标题', max_length=200)
    pub_date = models.DateTimeField('发布日期')

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


from django.db import models

# Create your models here.
