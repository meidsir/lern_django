管理员账号:
UserName: admin
Password: 12345678

如何修改添加应用的名称:
你自己添加的app下面的apps.py文件下的类<你的app名Config.py>下面添加一个verbose_name 后面改成你想要显示的名称就OK了！

修改App名称
对应的App目录下的apps.py文件里有Django自动生成的AppNameConfig类 (如果没有，说明这个App不是manage.py startapp AppName命令生成的)。
一般这个类里只有默认的一个属性name，我们自己增加两条属性

class AppNameConfig(AppConfig):
    name = 'appname'
    verbose_name = u"应用名称"
    verbose_name_plural = u"应用名称"
 然后在对应的App目录下__init__.py文件里增加一条语句
default_app_config = 'AppName.apps.UsersConfig'
然后重启服务器即可。

修改Model名称
在自己定义的model类里面增加class Meta然后重启服务器即可

class Example(models.Model):
    # other statements
    class Meta:
        verbose_name = u"模块名称"
        verbose_name_plural = u"模块名称"   
        
        
修改Model内字段名称
这几乎是所有Django教程里都会提到的，定义时增加verbose_name参数即可
class Example(models.Model):
    Name = models.CharField(verbose_name="姓名", max_length=20)
    

更改字段,直接在Model里面修改对应的字段
然后再终端环境运行:
    python manage.py makemigrations
    python manage.py migrate
