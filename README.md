使用技术：
    前台技术：HTML，CSS，bootstrap(前端模板)
    后台技术：python，django框架，mysql存储数据

主要文件夹/文件作用：
    1. bin目录：在linux/mac系统中的快捷启动文件。在python环境中可以使用python manage.py runserver的方式启动
    2. GraphDTA：算法文件保存的路径
    3. GraphDTA_web：项目的根路径
    4. home：项目主app路径。主要需要关注：
        1. urls.py(路由) 
        2. views.py(视图文件，操作数据库，并且返回页面)
        3. models.py：数据表设计
    5. static:静态文件存储位置如css，js等文件
    6. templates：html文件存储位置
    7. manage.py项目的启动文件
    
    
设计方案：
    django框架搭建便捷，并且可扩展性很强，选用django作为框架可以很快的搭建web服务。
    在前端上选择使用bootstrap框架，可以很快搭建页面结构，维护起来也很方便。

设计细节：
    因为完整跑一次的过程时间很长，所以采用数据入库的方式：
        第一次跑完之后，把数据结果存如数据库中，之后每次运行时，直接从数据库中展示出数据。
    如果是新上传的数据集，会先上传到GraphDTA路径下的upload路径下
    
    

管理员账号：
用户名：adminuser
密码：admin123456

