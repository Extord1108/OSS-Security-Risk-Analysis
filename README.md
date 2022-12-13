# 开源供应链安全风险分析

## 项目简述

​	npm是JavaScript的包管理工具，现代js开发中大部分第三方库的下载都是通过npm进行的，开源开发者们也乐意将自己得库上传到npm上。近些年许多攻击者针对流行的软件包管理器以及他们的用户进行供应链攻击，npm就包括在其中。在2021年，通过利用开源软件的供应链，安全攻击的数量同比增长了650%。

​	论文[What are Weak Links in the npm Supply Chain?](https://arxiv.org/abs/2112.10165v2)中对npm供应链的安全风险做了比较详细的分析，但是其中仍然有些不足，比如作者分析的后三种风险并没有得到从业者的认可，而作者通过调研得到的从业者的观点却没有得到深入分析，另外论文所使用的数据也有些过时了。因此本项目希望在此篇论文的基础上，结合自己的调研和讨论，从六个方面分析npm供应链的安全风险。

## 预览

[开源供应链安全风险分析](http://ossd.retools.space/)

[项目设计文档](https://blog.csdn.net/weixin_47231648/article/details/127876587)

[项目实现文档](https://blog.csdn.net/weixin_47231648/article/details/128306848)

[用户手册](https://blog.csdn.net/weixin_47231648/article/details/128303204)


## 准备

#### 数据层

* 框架：scrapy
* 数据库：Mysql
* 语言版本：python 3.10
* python模块：
  * scrapy
  * pymysql
  * twist

#### 后端

- 框架：Flask
- 语言版本：python 3.10
- python模块：
  - requests：2.28.1
  - flask：2.2.2
  - flask-sqlacodegen：1.1.8
  - flask-sqlalchemy：3.0.2
  - gevent：21.8.0
  - pymysql：1.0.2
  - sqlalchemy：1.4.44

#### 前端

* 框架：vue.js
* ui库：element-ui
* 图表：echarts
* 包管理器：yarn

## 使用

#### 获取项目代码

```
git clone git@github.com:Re-Li-fe/OSS-Security-Risk-Analysis.git
```

#### 启动爬虫

在Linux环境下创建配置并且激活虚拟环境

```bash
conda create -n ossd python=3.10
conda activate ossd
```

在根目录下运行

```bash
scrapy crawl ossd
```

#### 后端部署

运行backend目录下的wsgi.py即可运行项目

```
python wsgi.py
```

项目的运行端口和域名可以在wsgi.py中进行配置

#### 前端部署

- 安装依赖

```
yarn install
```

- 运行

```
yarn dev
```

- 打包

```
yarn build
```

## 开发任务

我们目前已完成了如下任务：

 - [x] 数据爬取，通过npm官方提供的接口爬取所有包的相关数据用于进一步分析。

 - [x] 数据清洗，在爬取的数据中有部分不符合我们的需求或者无法用于分析，这部分数据需要剔除。
 - [x] 数据存储。实际操作中发现由于npm管理着百万级的第三方包，每次爬取都需要花费相当多的时间，因此我们将数据以一定组织形式存储起来。
* 数据处理，通过得到的数据分析npm供应链的安全风险，主要分为六个方面。
  - [x] 过期的维护者域。如果维护者的域已过期，并且在其帐户上没有设置2FA身份验证，则攻击者可以劫持一个组件。
  - [x] 安装脚本。攻击者可以使用安装脚本，通过软件包安装步骤来运行执行恶意行为的命令。
  - [x] 未维护的包。攻击者可以针对那些更有可能因为缺乏维护而偷偷侵入恶意软件的软件包。
  - [x] 第三方包的代码仓库。代码仓库与npm中的代码版本不一致，或者代码仓库长时间没有提交。
  - [x] 名称相似的恶意软件。
  - [x] 宽松的开源许可证。
 - [x] 后端，由于本项目规模不大，无需搭建复杂的后端框架，因此选择flask作为我们的后端框架。
 - [x] 前端，使用vue.js框架搭建，用于直观展示一些数据。

## 开发者

https://github.com/shilogic0929

https://github.com/BX511021

https://github.com/Re-Li-fe
