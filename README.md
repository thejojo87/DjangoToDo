# DjangoToDo

[TOC]

# 资源
Django +python3.6 +win10 +mysql

参考的书：python web 测试驱动方法

http://www.obeythetestinggoat.com/pages/book.html#toc

https://github.com/hjwp/book-example


# 目标
我想要做什么？
Django做的一个ToDo网站。
用户登陆功能。
RestfulAPI
Swift写个iphone客户端。

发布。


# 项目进度

# 遇到的问题

## 问题1：selenuim3无法运行
最开始的测试，因为selenium3需要一个geckodriver的驱动。

https://www.zhihu.com/question/49568096

https://github.com/mozilla/geckodriver/releases

下载这个驱动，放在firefox安装目录，并且系统变量里添加firefox目录就可以了。

## 问题2：pycharm运行runserver，会有exit

Process finished with exit code -1073741819 (0xC0000005)
这个是因为run错了。
pycharm，run configuration里有Django server，而不是像之前一样的python里，添加manage。

## 问题3：Django url引用出错。

django1.10开始修改了地址引用方式。
需要直接在上面引用，然后下面是变量，而不是string

http://stackoverflow.com/questions/38744285/django-urls-error-view-must-be-a-callable-or-a-list-tuple-in-the-case-of-includ

## 问题4：runserver后台怎么运行？
直接后面加一个& 就可以了。
但是后台运行就就不太好杀了。
端口会表示占用的。
只好用nginx重启方式了。
sudo service nginx reload

    You can use netstat -tulpn to see the PID
    kill -9 PID

## 问题5： upstart已经被淘汰了。systemd
怎么转换？

https://gist.github.com/marcanuy/5ae0e0ef5976aa4a10a7

http://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-part-two.html

https://piaosanlang.gitbooks.io/spiders/content/05day/section5.4.html



# 总结



# 第一章 使用功能测试协助安装Django
首先需要selenium

在这里的第一步，永远是先测试，再写代码。
也就是先测试失败，然后写。
而且一次只做一步。

新建一个functional_tests.py文件。
就是用selenium开浏览器。
遇到第一个坑，需要另外的驱动。问题1解决了。

测试网址百度的话，时不时抽风，说编码错误。
google的话，因为这个不是全局翻墙，这个firefox是原始状态，打不开。

## 1.2 让Django运行起来

django-admin.py startproject TODO
这是新建项目命令
TODO文件夹里还有个TODO文件夹，里面有init，settings,urls,wsgi四个文件

书上说，manage.py应该再第二个TODO文件夹里面，不过pycharm新建的却是在外面。
测试了一下，书上的是错的。manage文件在外面，和第二个TODO文件夹平级。
pycharm还附带了sqlite

启动服务器的命令是
python manage.py runserver

这里遇到第二个坑，如果在term里，运行一点问题没有。
但是pycharm的run里运行，会exit。


# 第二章 使用unittest 模块扩展功能测试

为TODO测试文件编写个故事。

```python
from selenium import webdriver

browser = webdriver.Firefox()

# 女孩去看了网站首页
browser.get('http://localhost:8000')
# browser.get('http://sina.com')

# 女孩注意到网站标题含有To-Do
assert 'To-Do' in browser.title

# 应用邀请她输入一个待办

# 她输入了一个，买个本子

# 她输入后，页面更新了，显示了她输入的项目


# 页面又显示了一个文本框，可以输入其他待办
# 女孩输入了另一个待办

# 页面再次更新

# 显示了2个待办

# 她想知道这个网站是否会记住她的清单

# 她看到网站为她生成了一个唯一的url

# 而且页面里有文字解说这个功能

# 她访问这个URL，发现她的待办还存在

# 她很满意，去睡觉了

browser.quit()

```

出了写了个故事，还有个改变就是assert，todo字段。
这个在标题里是没有的，所以会出错。
assert是查找。

## 2.2 python标准库中的unittest模块

在这里需要重新写一份test文件

把测试写在了一个类里，unittest.TestCase的子类。
里面有setup 和teardown。
assert也换了。

## 2.3 隐式等待
setup里添加implicitly_wait
这个是要selenium等待几秒钟。
这个在简单的时候还可以，不过在复杂的时候，需要专门的等待规则。

self.browser.implicitly_wait(3)

第二章结束

# 第三章 使用单元测试，测试简单的首页

创建django应用。
django项目可以多好几个app。
python manage.py startapp lists

对比上面是project
django-admin.py startproject TODO

## 3.2 单元测试和功能测试的区别

功能测试是用户的角度，外面测试。
单元测试是程序员的角度。

顺序是，先用功能测试，再单元测试。

## 3.3 Django中的单元测试

新建的app里，直接就有个tests.py文件
里面是Django提供的TestCase这个类，是增强的unittest.testcase

启动test命令行命令是
python manage.py test
我有个问题，如果好几个app的tests，那么都test么？

运行测试的时候，测试程序会在所有以test开头的文件中查找所有的test cases(inittest.TestCase的子类),自动建立测试集然后运行测试。

注意：如果测试是基于数据库访问的(读取、查询Model)，一定要用django.test.TestCase建立测试类，而不要用unittest.TestCase。


Runing tests

```python
执行目录下所有的测试(所有的test*.py文件)：
1

$ python manage.py test

执行animals项目下tests包里的测试：
1

$ python manage.py test animals.tests

执行animals项目里的test测试：
1

$ python manage.py test animals

单独执行某个test case：
1

$ python manage.py test animals.tests.AnimalTestCase

单独执行某个测试方法：
1

$ python manage.py test animals.tests.AnimalTestCase.test_animals_can_speak

为测试文件提供路径：
1

$ python manage.py test animals/

通配测试文件名：
1

$ python manage.py test --pattern="tests_*.py"

启用warnings提醒：
1

$ python -Wall manage.py test
```

## 3.4 mvc 视图 url

django的工作方式是，http请求地址。
然后计算哪个函数处理。
相应的视图做出反应。

写个测试
使用了django内部的resolve函数，用来解析地址
这个测试当然失败。因为根本没写url解析函数嘛。

## 3.6 urls.py
url前半部分是正则表达式，后半部分是函数。
也可以用include，包含其他urls文件

这里有个问题，Django1.10修改了url引用方式，不再允许string了。
直接再上面引用模块

如果有很多视图，一个个引用不方便。
可以直接从lists import views as lists_views

## 3.7 为视图编写单元测试

```python
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')

```

就是，测试模块，指出用哪个函数，然后views里的函数，指出返回什么对象

第三章结束。

# 第四章 编写这些测试有什么用

在functional_tests文件里 selenium模拟的功能测试给写完。
写测试的时候，需要开启服务器。

函数里，返回html，很愚蠢，所以需要使用模板。
返回的是模板文件。

在lists/templates/home.html
写个最简单的html文件。
然后lists/views.py里
return render home.html
最后注册templates
其实并不是templates没有注册，而是，lists在项目里没有注册到。
在settings里，installed_apps里添加‘lists’

运行test测试，通过了。
再检查一下，是否返回正确html模板。
接下来测试功能测试。

写html文件。
功能测试，就写到有个table。输入项。
assert还可以自定义返回的错误信息。

第四章结束。

# 第五章 保存用户输入

首先input改成form，POST。

然后引入time.sleep(10)
可以看到forbidden，csrf。
input下面
添加一个自带的{% csrf_token %}

但是这里有个问题，加了csrf后，上面的返回正确网址测试就无法通过。


## 5.2 在服务器中处理POST请求

为表单action返回主页。
先写个测试。
lists/tests.py里

然后在views里，写home_page函数。
如果要求是post，那么返回post请求里，item——text标签数据。

## 5.3 把python变量传入模板中渲染

home.html里添加new_item_text

在tests里测试的时候传入。

在views里，传入POST的参数


## 5.5 数据库迁移

先在models文件里，生成item
注意一下，这里默认字符串为空用双引号。

python manage.py makemigrations
就会出现一个migrations文件夹

## 5.9 使用迁移创建生产数据库

test是django生成的测试数据库。
真正的数据库，要自己创建
在settings里设置Database
默认是sqlite3

在这里有个问题，如果用python manage.py shell启动试一下，
会发现Error loading MySQLdb module: No module named 'MySQLdb'

这是因为mysqldb并不兼容于python3

https://docs.djangoproject.com/en/1.10/ref/databases/#mysql-notes

这里的文档，给出了3个选项。
反正都是第一次，我都试一下吧。

http://www.jianshu.com/p/ecc941e861ee

### mysqlclient
这个是django官方推荐的做法。
首先pip install 之后 弹出错误，说需要c++ build tools
http://landinghub.visualstudio.com/visual-cpp-build-tools

那就装吧。

还是遇到很多问题，放弃了，算了。

### 试一下pymysql来代替

因为之前就是用这个链接的。
pip install pymysql
然后在init文件里。

```python
import pymysql
pymysql.install_as_MySQLdb()
```

就可以了。python manage.py shell 试一下。

发现可以了。
那么python manage.py migrate


```python
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'django_todo',
        'USER': 'root',
        'PASSWORD': 'password',  ## 安装 mysql 数据库时，输入的 root 用户的密码
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
forloop.counter，这个可以按照循环次数，增加1，2，3.。。


第五章结束，实际上，我放弃了从5.3开始跟踪tdd了。
因为实在是太繁琐了。

# 第六章 完成最简可用的网站

这一章需要做的是用户自己的清单列表是唯一的。
不过暂时还没用到用户管理机制。

以后要做注册页面。
但是需要第三方登录。
比如百词斩 官网

http://www.baicizhan.com/register

![百词斩官网注册图片](images/百词斩注册.jpg)

先做个view 地址唯一的。

先去views.py修改函数

然后去url定义地址

最后修改模板

修改模板了，当然views里制定的html也要改变

下一步要做新建页面

1. views里，新建一个pass的 new_list函数
2. url里，进行地址引用-这里有个捕获组概念（）包起来才可以
3. 返回views里，修改完new_list函数
4. 修改html表单

接下来要修改model。
新建一个list对象。
一个list，对好几个items对象。
要设置外键。一不用管，多要设置。
新建了，所以要make migrations
views里new_list也要修改

接下来，每个列表都应该有自己的url
要做的就是捕获url-正则表达式


# 第二部分 Web开发要素
# 第七章 美化网站：布局，样式，及其测试方法

首先居中：输入框

```html
<p style="text-align: center;">
```

使用bootstrap。
在这里需要引用模板这个概念

django自带的模板还是，jinja2.这是个问题。
貌似区别很小。

先新建一个base.html吧


引用bootstrap就可以了。
没必要下载。

http://v3.bootcss.com/getting-started/

这里提供cnd加速服务。

超大文本快-jumbotron

大型输入框-class="form-control input-lg"

样式化表格-class="table"

使用自己编写的css

因为在setting里，static选项是‘static’
也就是说，只要css地址用/static开头，那么就会在
应用里，寻找对应的base.css文件


## collectstatic命令

因为你可能需要css放在其他地方，你需要备份保存在专门的文件夹里。
在工程目录新建一个static目录

然后setting里设置

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, './static'))

然后启动 python manage.py collectstatic

# 第八章 使用过度网站测试部署

## 8.3 购买域名
首先需要买个域名
去腾讯云买了个2块钱的域名。
不过网站需要备案，需要购买服务。
充值了1块钱，买了个3毛钱1小时的主机。
结果4个小时后欠费1块钱，被关掉了。
不过备案还是顺利申请了。等结果吧。

域名买到了。

## 8.4 手动配置托管网站的服务器

配置分为两个部分。
1. 配置新服务器，托管代码
2. 新版代码部署到服务器

部署到哪里呢？
也可以分为两类。
fu'wuf
1. 自己的服务器
2. paas-heroku之类的

微软的azure，amazon aws，digital ocean都是选项。

先用azure试一下。
微软的azure貌似也提供网站webapp-paas服务

似乎有两种方式。
一个是使用linux虚拟机，创建pythonweb应用。
一个是使用azure提供的 django

azure里新建了一个虚拟机。
新建的时候有个选项，是否ssh，还是密码。
先密码了。
不过每次都输入密码，太烦人。
在密码重置里重新设置了ssh连接，
其实发现git windows里操作就可以了。
和mac一模一样。
ssh的原理就是生成一个密码对。
自己把当中的公钥上传到服务器，服务器就可以安全链接了。
ssh只是用来确认身份的，所以一份可以在各个不同的网站同时使用。
比如github 和 azure不冲突。

http://jingyan.baidu.com/article/a65957f4e91ccf24e77f9b11.html

然后azure里点击，连接，出现ssh命令

ssh thejojo@xxx.xxx.xxx.xxx
然后输入密码，就连接上了。

### 8.4.4 安装nginx

sudo apt-get install nginx
sudo service nginx start
就启动了nginx了。
但是现在浏览器访问，那么就看不到nginx界面。
这是因为azure并不会默认开放外网端口。
这个改版之后，
在网络接口-有效的安全规则里存在。
而且in就是访问，out才是输出。
in里默认开启了ssh访问。

然后安装了python3 pip3
virtualenv

### 8.4.5 解析域名

域名太长了。
去腾讯云，添加域名解析

cname是网站地址
a是ip地址关联

## 8.5 手动部署代码
先装mysql吧

https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04

### 8.5.1 调整数据库的位置

这里做的其实就是使用git，把代码从github复制到linux里

git我还没有在虚拟机上配置过，教程里缺少这个。

思路就是，生成一个ssh密钥。
然后把这个加进我的github里。

cd ~/.ssh && ssh-keygen
会让你确认密钥保存的地点。
还有密码。留空

然后cat id_rsa.pub
把key复制到剪贴板。
最后到github里，添加就可以了。

教程在这里：

https://git-scm.com/book/zh/v1/%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E7%9A%84-Git-%E7%94%9F%E6%88%90-SSH-%E5%85%AC%E9%92%A5

### 8.5.2 创建虚拟环境

先安装virtualenv
pip install virtualenv

然后在本地 pip freeze >requirements.txt
然后把这个push到git里。
然后在ssh里，git pull 把requirements文件拉回来。
virtualenv --python=python3 ../virtualenv/

这样就在上一个目录的virtualenv文件夹里安装了。
ls ../virtualenv/ 可以查看。

然后安装requirements
../virtualenv/bin/pip install -r requirements.txt
requirements里有一个包如果安装失败，那么都会取消。
所以要去掉那个包继续安装。

pip list 可以查看已经安装的包

启动 是
 ../virtualenv/bin/python3 manage.py runserver

不过因为mysql没有配置，所以现在会出错。
虚拟环境里并不一定都需要activate，只要指定python路径就可以了。

### 额外的，ssh里设置mysql

mysql -u root -p
然后show databases;查看数据库
create database django_todo;
这样就创建好了数据库。
运行起来发现没有任何问题。


### 8.5.3 简单配置nginx

简单配置只需要server
里面是listen 端口，servername 解析的网址
还有location

sudo vim 新建一个django_todo 文件，注意没有后缀名字
然后创建一个符号链接。
把这个加入启用的网站列表里。

这里有两个文件夹。
site-enabled 和site-avaliable
放在avaibable，然后把这个链接到enabled

然后删除default文件。
nginx如果不能重启，那么 查看日志来看哪里出错了。
sudo service nginx reload

如果这时候去访问的话，会出现502 bad gateway，nginx
然后启动manage.py


```python
cd sites/source
../virtualenv/bin/python3 manage.py runserver
```

就成功出现了

不过因为数据库并没有生成tables
所以需要migrate

## 8.6 为部署到生产环境做好准备

要安装gunicorn
这个需要直到wsgi服务器的路径。可以由application函数获取。

```python
../virtualenv/bin/pip install gunicorn
../virtualenv/bin/gunicorn python_ToDo.wsgi:application


../virtualenv/bin/python3 manage.py collectstatic --noinput

```

现在如果访问主页，会发现所有的样式都消失了。
因为bootstrap我是直接引用的，消失的只是我自定义的base的css。
这是因为，Django服务器会自动维护静态文件，但是gunicorn不会。

所以需要配置nginx来服务。

运行上面第三行，就会出现一个static文件夹，里面有base文件。

修改availiable文件夹里的nginx配置文件，加一个location/static

需要注意路径。
static总共有两处，一个是原来的static，但是这个会因为添加app而增加。
另一个就是刚才生成的总的static，这个在source总目录下面。
需要把这个设置为static

cd /etc/nginx/sites-available/
cd /home/thejojo/sites/source/

../virtualenv/bin/gunicorn python_ToDo.wsgi:application
 ../virtualenv/bin/gunicorn --bind unix:/tmp/thejojo.xyz.socket python_ToDo.wsgi:application




### 8.6.3 换用Unix套接字

从这里开始网站变成了502.是不是我弄错了？

location原来只是定义了localhost 8000
但是应该把这个删掉，换成socket方式。


如果想同时使用服务器和过度网站，就不能共用8000端口。

所以使用Unix套接字。类似于硬盘中的文件。
设置了proxy_set_header 和proxy_pass
不太理解。
运行命令也换成了这个，但是依然是502

nginx -t 这个命令是用来查询nginx哪里错了的很好的命令。

这个是enable里的thejojo.xyz nginx配置文件
```python
server {
    listen 80;
    server_name thejojo.xyz;


    location /static{
        alias /home/thejojo/sites/source/static;

        }
    location /{
        proxy_set_header Host $host;
        proxy_pass http://unix:/tmp/thejojo.xyz.socket;
    }
}
```


 ../virtualenv/bin/gunicorn --bind unix:/tmp/thejojo.xyz.socket python_ToDo.wsgi:application

现在就是bad request，在下一节需要设置
### 8.6.4 把debug设为false，设置allowed_hosts

在生产环境里开启了debug，不太好。
所以要在setting里关掉
allowed_host 设置为thejojo.xyz 依然是badrequest400
如果设置为* 那么就可以。
正确的host是什么呢？
ALLOWED_HOSTS是为了限定请求中的host值,以防止黑客构造包来发送请求.只有在列表中的host才能访问.强烈建议不要使用*通配符去配置,另外当DEBUG设置为False的时候必须配置这个配置.否则会抛出异常.配置模板如下:

估计正确的是主页网址 thejojo.XXXXX.XXXX.cn
果然没错，我的xyz域名因为被封锁了，所以无法使用。



### 8.6.5 使用Upstart确保引导时启动Gunicorn

在这里遇到了难题，无法正常启动upstart


但是我启动之后发现， start : command not found
这是因为ubuntu 15之后改为systemd 了。


脚本需要修改的是环境和启动行,runtimedirectory.
需要的问题是，脚本放在哪里？怎么启动？
脚本要放在/lib/systemd/system$ python_ToDo.service
写完后启动sudo systemctl start python_ToDo
关掉是stop。
这样的话，不用runtime来启动，
下一步就是重启服务器，看看能否自动启动nginx
但是现在启动nginx并没有启动python_ToDo服务

因为无法enable service。
会出现invalid

我意识到一个事情
就是install wantedby这个部分我是空着的，一开始以为不需要。
但是现在发现，系统会用这个字段，来做个链接放在etc/systemd/system里。
Failed to enable unit: Invalid argument
就是因为service文件复制的时候，少了注释号，文字错了。
sudo systemctl enable python_ToDo 生成了链接。
因为linux只会在etc/systemd/system目录下的文件才会开机启动。

我自己做个链接吧。
sudo ln -s /lib/systemd/system/python_ToDo.service  /etc/systemd/system/python_ToDo.service

但是原来我把服务给关掉了。
即便是添加了链接，preset显示enabled，但是active显示inactive。
如果开了之后重启会如何？




```script
# Gunicorn Site systemd service file

[Unit]
Description=Gunicorn server for django_ToDo.service
After=network.target
After=syslog.target

[Service]
User=root
# Environment=sitedir=/home/thejojo/sites/source
WorkingDirectory=/home/thejojo/sites/source
ExecStart=/home/thejojo/sites/virtualenv/bin/gunicorn --bind unix:/tmp/thejojo.xyz.socket python_ToDo.wsgi:application
Restart=on-failure
# RuntimeDirectory=gunicorn-stagingd
# RuntimeDirectoryMode=755


#sudo systemctl start django_ToDo.service

[Install]
WantedBy=multi-user.target

```


linux删除目录很简单，很多人还是习惯用rmdir，不过一旦目录非空，就陷入深深的苦恼之中，现在使用rm -rf命令即可。
直接rm就可以了，不过要加两个参数-rf 即：rm -rf 目录名字
-r 就是向下递归，不管有多少级目录，一并删除
-f 就是直接强行删除，不作任何提示的意思

第八章到此结束。

# 第九章 使用fabric自动部署

Fabric是什么？
假定我们有一个Web应用，使用Gunicorn运行，同时后台有一些rqworker处理一些异步的任务。同时supervisor监控这些进程的运行。每次本地修改代码提交之后，一般流程是登录服务器使用git pull 将新的代码拉下来，然后重启这些进程。频繁执行这些机械的流程比较麻烦，我们可以自动化运行这些工作的流程。

pip3 install fabric3

fabric 一般创建一个fabfile.py文件。
定义函数，然后使用fab 命令行工具调用。

## 9.1 分析一个Fabric部署脚本

放在deploy_tools文件夹里面。

以下划线开头的都不是fabric的公开api

首先定义了site folder和source folder。

新建了几个函数按照启动顺序执行。
这里1，database没必要，static我的是放在下一级的。
2 没必要修改
3 有必要把访问网址写进去
4 没必要修改
5 没必要修改
6 没必要修改

1. 创建目录结构的函数
2. 拉取源代码的函数
3. 更新配置文件，设置allowed_host 和debug，创建一个密钥
4. 创建或者更新virtualenv环境
5. 更新静态文件
6. 最后更新数据库


```python
from fabric.contrib.files import append,exists,sed
from fabric.api import env,local,run
import random

REPO_URL = "https://github.com/thejojo87/DjangoToDo.git"
env.host = "thejojo.chinanorth.cloudapp.chinacloudapi.cn"

def deploy():
    site_folder = '/home/thejojo/sites'
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)

def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ( 'virtualenv', 'source'):

        run('mkdir -p %s/%s' % (site_folder, subfolder))

def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        run('cd %s && git fetch' % (source_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, source_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd %s && git reset --hard %s' % (source_folder, current_commit))


def _update_settings(source_folder, site_name):
    settings_path = source_folder + '/python_ToDo/settings.py'
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path,
        'ALLOWED_HOSTS =.+$',
        'ALLOWED_HOSTS = ["%s"]' % (site_name,)
    )
    secret_key_file = source_folder + '/superlists/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, "SECRET_KEY = '%s'" % (key,))
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')

def _update_virtualenv(source_folder):
    virtualenv_folder = source_folder + '/../virtualenv'
    if not exists(virtualenv_folder + '/bin/pip'):
        run('virtualenv --python=python3 %s' % (virtualenv_folder,))
    run('%s/bin/pip install -r %s/requirements.txt' % (
            virtualenv_folder, source_folder
    ))

def _update_static_files(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py collectstatic --noinput' % (
        source_folder,
    ))

def _update_database(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py migrate --noinput' % (
        source_folder,
    ))

```

## 9.2 试着部署脚本

启动命令是
fab deploy:host=thejojo@thejojo.chinanorth.cloudapp.chinacloudapi.cn

貌似成功了。
但是现在的问题是，我的本地git也需要提交，
我的服务器也需要拉回来，可以么？

下次如果想再创建虚拟机。
只需要安装fabric，然后启动这个脚本。
最后再配置nginx和gunicorn，最后是systempd。
就完成了。

第九章结束。

# 第十章 输入验证和测试的组织方式

在这里要做的是，检测是否为空。
可以有两种方式，模型层面和表单层面。
作者倾向于模型层面。

http://python.usyiyi.cn/django/ref/models/fields.html

这里揭示了null字段和blank字段。
django，null默认是false，但是并没有什么用。并不会验证。

## 10.3 在视图中显示模型验证错误

首先在base.html的表单下面，新建一个error模块，如果出错，那么下面显示错误。

为了要把错误传入视图，需要修改view函数，

新建是new_list函数。

```python
def new_list(request):
    list_ = List.objects.create()

    item = Item(text=request.POST['item_text'],list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})

    return redirect('/lists/%d/' % (list_.id))
````

但是仅仅改成这样，并不能防止空字段。

## 10.4 Django模式：在渲染表单的视图中处理post请求

原来的方式是，显示list用一个地址和模板。
add的时候使用另一个地址和模板。
如果把这个改成在一个url里处理，那么好处是
在一个url里既可以显示表单，又可以显示处理用户输入过程中遇到的错误。

先把list template里，发送post的地址给改掉。

然后把new_item 实现的功能转移到view_list中

一共需要修改两处。
一个是主页里空格的时候，newlist不能为空。
另一个是list/3/具体目录里，不能新建为空。

不过现在这里的try，except是重复的。需要重构。

这里先把原来html文件硬编码的url换成django的url模板标签。

再来就把views函数里，redirect硬编码的，也改。

但是获取直接地址也是很有用的。
django里每一个模型对象都对应一个特定的url，因此定义
一个特殊的函数，作用是获取显示单个模型对象的页面url。
因此在models里写一个get_absolute_url函数。

```python
class List(models.Model):

    def get_absolute_url(self):
        return reverse('lists:view_list',args=[self.id])
```

这样的话，下面两句，效果是一样的。

```python
   return redirect(list_)
    # return redirect('lists:view_list' ,list_.id)

```

同样的方法修改view_list视图

```python
            return redirect(list_)
            return redirect('/lists/%d/' % (list_.id))

```

