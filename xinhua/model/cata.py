#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model._base import Base
from misc.const import d_cata, d_source
from peewee import CharField, PrimaryKeyField, BigIntegerField


class Cata(Base):
    id = PrimaryKeyField()
    cata = CharField(index=True)
    source = CharField(index=True)
    view = BigIntegerField(default=0)
    view_ = BigIntegerField(default=0)  # 手动增量

    @property
    def cata_cn(self):
        return d_cata.get(self.cata)

    @property
    def source_cn(self):
        return d_source.get(self.source)

    @property
    def view__(self):
        return self.view + self.view_
