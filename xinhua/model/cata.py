#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model._base import Base
from peewee import CharField, PrimaryKeyField, BigIntegerField


class Cata(Base):
    id = PrimaryKeyField()
    title = CharField(index=True)
    name = CharField(index=True)
    view = BigIntegerField(default=0)
    view_ = BigIntegerField(default=0)
