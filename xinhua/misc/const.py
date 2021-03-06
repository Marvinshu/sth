#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict
from pypinyin import lazy_pinyin

d_source = dict(
    weibo=u"微博热点",
    wenku=u"百度文库",
    zhidao=u"百度知道",
    youku=u"优酷",
    tengxun=u"腾讯视频",
    toutiao=u"今日头条",
    xici=u"西祠胡同",
    xinlang=u"新浪论坛",
    wangyi=u"网易论坛",
    weixin=u"微信",
)
d_source = OrderedDict(sorted(d_source.items(), key=lambda x: lazy_pinyin(x[1])[0]))


d_cata = dict(
    cata1=u"科技前沿大师谈",
    cata2=u"科学原理一点通",
    cata4=u"科技创新里程碑",
    cata3=u"科技名家风采录",
)

d_cata_sort = dict(
    cata1=0,
    cata2=1,
    cata4=2,
    cata3=3,
    cata5=4
)


d_cata = OrderedDict(sorted(d_cata.items(), key=lambda x: d_cata_sort.get(x[0])))
