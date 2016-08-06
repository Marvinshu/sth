#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField


class Task(Base):
    class TYPE(object):
        TODO = 1
        DOING = 2
        DONE = 3

    id = PrimaryKeyField()
    title = CharField(max_length=32)
    percent = IntegerField(default=0)
    create_time = IntegerField(index=True, default=int(time.time()))
    index = IntegerField(index=True, default=0)
    type = IntegerField(default=TYPE.TODO)
