<!--
 * @Author: zyq
 * @Date: 2024-11-25 15:10:16
 * @LastEditors: zyq
 * @LastEditTime: 2024-11-26 09:03:05
 * @FilePath: /project/wx-miniprogram-gxkjg/README.md
 * @Description: README
 * 
 * Copyright (c) 2024 by zyq, All Rights Reserved. 
-->
## README
### 1.简介
业务需求: 抓取科技馆的相关展品信息数据. 相关数据存放在科技馆的相关展品数据存放在微信小程序"掌上科技馆"当中. 考虑两种方案:
* 通过抓包工具抓取小程序的请求, 然后通过postman模拟请求解析数据, 确定请求头和请求体. 然后通过python的request库发起请求或是调用相关爬虫框架, 拉回数据做后处理
* 通过逆向工程, 将小程序的代码进行逆向工程, 使用微信开发者工具加载源代码编译, 找到请求头和请求体, 然后通过python的request库发起请求或是调用相关爬虫框架, 拉回数据做后处理

### 2. 微信小程序逆向工程
微信小程序的具体逆向工程详细步骤参考该视频: https://www.bilibili.com/video/BV1UP2mYBEhF/?spm_id_from=333.337.search-card.all.click&vd_source=3ac09fd7bc9410fe2c4644e1ab96b1c1

对于本业务需求, 尝试下来主要遇到的问题:
* 问题一: 拿到小程序的源码后, 登录开发者工具, 编译报错. 通过gpt修复后编译成功, 但是运行报错. 报错: `不在request的合法域名列表中`. 问题解决参考: https://cloud.tencent.com/developer/article/2120637
* 问题二: `avataUrl not defined`. 在问题一按照网上方案处理后重编译, 出现报错, 定位原因卡在了微信登录态认证. 该小程序在登录的时候需要去拿到UnionId. 以及调试发现没有带上微信的session_key去请求, 导致登录被拦截.

> 总结

个人认为此方法适用于未有登录态认证的小程序以及开发者需要对js代码有一定基础, 不然在调试前端代码的过程中可能会踩坑.


> 相关工具链接

* uveilr.ext工具: https://www.52pojie.cn/thread-1795645-1-1.html
* 小程序解密工具: https://github.com/Angels-Ray/UnpackMiniApp

### 3. 抓包工具抓取请求
在第一种方式尝试未果后, 使用抓包工具测试抓取小程序的请求, 网上查阅资料发现有三种方式:
* charles+Burp: https://blog.csdn.net/Arched/article/details/135777104
* proxifer+Burp: https://blog.csdn.net/qq_68064663/article/details/133958534
* Fiddler抓包教学: https://search.bilibili.com/all?vt=27084983&keyword=%E5%BE%AE%E4%BF%A1%E5%B0%8F%E7%A8%8B%E5%BA%8F%E6%8A%93%E5%8C%85&from_source=webtop_search&spm_id_from=333.1007&search_source=5

其中1和2方式在测试下来, 出现的问题是一旦开启charles, 本机就会出现无网络的情况, 尝试网上多种解决方案无效. 不确定是不是由于本机开了clash代理或是其他原因所导致. 做对比实验后仍然没有网络. proxifer遇到类似的情况, 最后测试下来Fiddler能实现业务需求, 通过电脑版微信进入小程序, Fiddler抓取请求. 此处感谢b站up马农在跑步的分享.

> 具体步骤
* 安装并配置fiddler. 上述fiddler抓包b站视频中已有做介绍, 此处附fiddler的下载链接, 在教学视频的评论区中up也分享过. fiddler: https://pan.wlphp.com/
* 通过pc版微信登录小程序, 并在fiddler中找对应的请求链接
* 复制请求头和请求体, 并通过postman模拟请求, 确定可行性
* 通过python模拟请求, 并做数据后处理. 此处case by case处理, 可以用requests也可以用scrapy等爬虫框架实现类似效果
    * get_kjg_info.py: 抓取科技馆的相关展品信息数据
    * json_parser.py: 后处理解析原生数据
