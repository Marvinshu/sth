#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict
from pypinyin import lazy_pinyin

d_source = dict(
    weibo=u"微博热点",
    wenku=u"百度文库",
    zhidao=u"百度知道",
    tianya=u"天涯论坛",
    iqiyi=u"爱奇艺",
    youku=u"优酷",
    tengxun=u"腾讯视频",
)
d_source = OrderedDict(sorted(d_source.items(), key=lambda x: lazy_pinyin(x[1])[0]))


d_cata = dict(
    cata1=u"大师谈",
    cata2=u"一点通",
    cata3=u"风采录",
    cata4=u"分类4",
    cata5=u"分类5"
)
d_cata = OrderedDict(sorted(d_cata.items(), key=lambda x: lazy_pinyin(x[1])[0]))
