#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import MYSQL
from peewee import Model, MySQLDatabase
from playhouse.shortcuts import model_to_dict, dict_to_model

db = MySQLDatabase(MYSQL.DB, user=MYSQL.USER, password=MYSQL.PWD, host=MYSQL.HOST)


class Base(Model):

    def to_dict(self):
        return model_to_dict(self)

    @classmethod
    def from_dict(cls, d):
        return dict_to_model(cls, d) if d else None

    class Meta:
        database = db


def init_db():
    from model.user import User
    from model.task import Task
    db.create_tables([User, Task])


def drop_table():
    from model.user import User
    from model.task import Task
    db.drop_tables([User, Task])
