#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField


class User(Base):
    id = PrimaryKeyField()
    user = CharField(max_length=32, unique=True)
    name = CharField(max_length=32)
    pwd = CharField(max_length=32)
    create_time = IntegerField()

    class Meta:
        indexes = ((('user', 'pwd'), True),)
