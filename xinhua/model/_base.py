#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import hashlib
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
    from model.url import URL
    from model.cata import Cata
    from model.mod_log import ModLog
    from misc.const import d_cata, d_source

    # 创建表
    db.create_tables([User, URL, Cata, ModLog])

    # 新建用户
    data = dict(
        user="admin",
        name="admin",
        pwd=hashlib.md5('admin').hexdigest(),
    )
    User.create(**data)

    # 创建交叉表
    for k in d_cata.keys():
        for k1 in d_source.keys():
            d_ = dict(
                cata=k,
                source=k1,
            )
            Cata.create(**d_)


def drop_table():
    from model.user import User
    from model.url import URL
    from model.cata import Cata
    from model.mod_log import ModLog

    db.drop_tables([User, URL, Cata, ModLog])

if __name__ == '__main__':
    from model.mod_log import ModLog
    db.create_tables([ModLog])
    # db.create_tables([User, URL, Cata, ModLog])
