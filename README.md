# AioIP -- Fast Ip Pool Base on Python3.6 
基于python3.6实现的动态ip代理池的sdk，具体内容如下：
-----
# Contents  
- [设计初想](#设计初想) 
- [边码边想边设计](#边码边想边设计)
- [直接上图](#直接上图) 
    - [数据流以及系统架构](#数据流以及系统架构)
    - [功能模块](#功能模块)


# 设计初想
之所以设计这个库，是因为看了很多大神的的设计思路，`@qiyeboy`,`@jhao104`,`@SpiderClub`,自己在融合各位大牛的思路的基础上也总结了一些自己的想法，所以结合自己之前在工作中和项目中使用和掌握到的一些技术，也就顺水推舟的开源这个库让大家来使用和批判。

-----

各位大牛的`github`

1.[haipproxy](https://github.com/SpiderClub/haipproxy)

2.[proxy_pool](https://github.com/jhao104/proxy_pool)

3.[IPProxyPool](https://github.com/qiyeboy/IPProxyPool)

-------

PS；很多人都质疑说我这个库和其他人的有什么不一样，这里统一回答一下：

1. 技术栈

2. 实现的方式

3. 和其他库融合的方式

# 边码边想边设计

具体思考过程大家可以参考我的[WiKi](https://github.com/lateautunm/aioip/wiki/%E5%90%84%E4%BB%A3%E7%90%86%E7%BD%91%E7%AB%99%E7%9A%84ip%E4%BF%A1%E6%81%AF%E7%BB%93%E6%9E%84%E5%88%86%E6%9E%90)

# 直接上图
# 数据流以及系统架构

![数据流以及系统架构](https://github.com/lateautunm/aioip/blob/master/static/%E7%B3%BB%E7%BB%9F%E6%9E%B6%E6%9E%84%E4%BB%A5%E5%8F%8A%E6%95%B0%E6%8D%AE%E6%B5%81%E5%9B%BE.jpg)

# 功能模块

![功能模块](https://github.com/lateautunm/aioip/blob/master/static/%E5%8A%9F%E8%83%BD%E7%BB%93%E6%9E%84%E5%9B%BE.jpg)