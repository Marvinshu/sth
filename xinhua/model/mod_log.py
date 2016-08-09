#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from model._base import Base
from misc.const import d_cata, d_source
from peewee import CharField, IntegerField, PrimaryKeyField, BigIntegerField


class ModLog(Base):
    id = PrimaryKeyField()
    cata = CharField(index=True)
    source = CharField(index=True)
    value = BigIntegerField()
    event_time = IntegerField(index=True, default=int(time.time()))

    class Meta:
        db_table = 'mod_log'

    @property
    def cata_cn(self):
        return d_cata.get(self.cata)

    @property
    def source_cn(self):
        return d_source.get(self.source)

    @property
    def ti(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.event_time))
