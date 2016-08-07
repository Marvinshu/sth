#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField


class URL(Base):
    id = PrimaryKeyField()
    url = CharField()
    url_md5 = CharField(index=True, max_length=32)
    create_time = IntegerField(index=True, default=int(time.time()))
    cata = CharField(index=True)
    source = CharField(index=True)
    view = IntegerField(default=0)

    @property
    def cata_cn(self):
        return dict(
            cata1="大师谈",
            cata2="一点通",
            cata3="风采录",
            cata4="分类4",
            cata5="分类5"
        ).get(self.cata)

    @property
    def source_cn(self):
        return dict(
            weibo="微博热点",
            wenku="百度文库",
            zhidao="百度知道",
            tianya="天涯论坛",
            iqiyi="爱奇艺",
            youku="优酷",
            tengxun="腾讯视频",
        ).get(self.source)

    @property
    def ti(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.create_time))
