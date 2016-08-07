#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from model._base import Base
from misc.const import d_cata, d_source
from peewee import CharField, IntegerField, PrimaryKeyField, BigIntegerField


class URL(Base):
    id = PrimaryKeyField()
    title = CharField()
    url = CharField()
    url_md5 = CharField(index=True, max_length=32)
    create_time = IntegerField(index=True, default=int(time.time()))
    cata = CharField(index=True)
    source = CharField(index=True)
    view = BigIntegerField(default=0)
    view_ = BigIntegerField(default=0)

    @property
    def cata_cn(self):
        return d_cata.get(self.cata)

    @property
    def source_cn(self):
        return d_source.get(self.source)

    @property
    def ti(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.create_time))
