##### 使用virtualenv管理python版本变化

+ virtualenv是一个虚拟的Python环境构建器。可以并行创建多个Python环境，从而避免不同版本的库之间的兼容性问题。

**管理不同项目的python版本要求**
1. 本机同时安装python2.7，python3.6，选择其一配置python环境到系统环境path
2. 以下命令用于安装virtualenv
> pip install virtualenv
3. 在已创建的项目根目录下使用 virtualenv 创建虚拟python环境
> 执行以下命令 
> virtualenv --python=[C:\Python27\python.exe]可选路径，2.7还是3.6 [venv]任取虚拟环境文件夹名称
> virtualenv --python=C:\Python27\python.exe venv
> 若不指定--python，则virtualenv会使用默认path配置的python版本创建python虚拟环境

**window下激活虚拟python环境**
+ 激活 .\venv\Scripts\activate.bat
+ 控制台出现（venv）C:\本地路径>，代表执行成功
+ 使用 pip install安装包，则将依赖包安装在本地虚拟环境，而不是全局
+ 退出执行 .\venv\Scripts\deactivate.bat
+ .win下删除虚拟环境,直接将创建的 venv目录删除

**参考**
[win下配置python不同版本的虚拟环境](https://blog.csdn.net/come_dream/article/details/80686548)


##### 使用reqiurement.txt管理python项目依赖包
+ 若存在虚拟环境，请进入虚拟环境执行
+ 项目使用virtualenv环境，直接使用pip freeze即可，将已安装的依赖包加入到requirements.txt
+ 使用pip freeze
> pip freeze > requirements.txt
> 这种方式配合virtualenv 才好使，否则把整个环境中的包都列出来了

+ pipreqs
> 这个工具的好处是可以通过对项目目录的扫描，自动发现使用了那些类库，自动生成依赖清单。
> 缺点是可能会有些偏差，需要检查并自己调整下。
> 安装：pip install pipreqs
+ 在项目的根目录下使用：pipreqs ./   
> 如果是Windows系统，会报编码错误 (UnicodeDecodeError: 'gbk' codec can't decode byte 0xa8 in position 24: illegal multibyte sequence)  
> 使用时，指定编码格式：pipreqs ./ --encoding=utf8 [--force]
> 生成requirements.txt 文件后，可以根据这个文件下载所有的依赖
> 用法：pip install -r requriements.txt

**参考**
[python项目依赖包管理 reqiurement.txt的使用](https://www.cnblogs.com/zhaopanpan/p/9383350.html)


##### Python使用虚拟环境安装Flask

**1. 创建flask项目以及项目下的虚拟环境**
+ mkdir newproj
+ cd newproj
+ virtualenv venv
+ .\venv\Scripts\activate.bat
+ 虚拟环境下安装flask，pip install flask

+ 将安装的依赖包添加到requirements.txt
> pip freeze > requirements.txt

**2. python flask**
+ blueprint
> 
> flask的蓝图就相当于Django的urls.py文件，我们就可以定义多个应用路由来使用，这里的蓝图起的别名就相当于namespace



##### VsCode激活virtualenv报错
+ .\venv\Scripts\activate
+ 报错，无法加载文件 C:\Code\test-flask\venv\Scripts\activate.ps1
+ 在终端，依次执行以下命令
> get-executionpolicy
> set-executionpolicy remotesigned，若报错，使用管理员打开cmd执行或者执行下一步
> Set-ExecutionPolicy -Scope CurrentUser
> 输入：remotesigned即可

