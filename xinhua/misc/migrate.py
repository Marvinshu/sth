#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
from config import MYSQL
from peewee import MySQLDatabase

db = MySQLDatabase(MYSQL.DB, user=MYSQL.USER, password=MYSQL.PWD, host=MYSQL.HOST)


if __name__ == '__main__':
    from model.cata import Cata
    from misc.const import d_cata, d_source

    # 创建交叉表
    for k in d_cata.keys():
        for k1 in d_source.keys():
            c = Cata.select().where(Cata.cata == k, Cata.source == k1)
            if not c:
                print '创建 {k}, {k1}'.format(k=k, k1=k1)

                d_ = dict(
                    cata=k,
                    source=k1,
                )
                Cata.create(**d_)

    # 要删除的字段
    d_source_ = dict(
        maopu=u"猫扑大杂烩",
        tianya=u"天涯论坛",
        iqiyi=u"爱奇艺",
        xinhua=u""
    )

    d_cata_ = dict(
        cata1=u"科技前沿大师谈",
        cata2=u"科学原理一点通",
        cata4=u"科技创新里程碑",
        cata3=u"科技名家风采录",
        cata5=u'cata5',
    )

    for k in d_cata_.keys():
        for k1 in d_source_.keys():
            try:
                c = Cata.get(Cata.cata == k, Cata.source == k1)
                c.delete_instance()
                print '删除 {k}, {k1}'.format(k=k, k1=k1)
            except:
                print ''

    d_cata_ = dict(
        cata5=u'cata5',
    )

    for k in d_cata_.keys():
        for k1 in d_source.keys():
            try:
                c = Cata.get(Cata.cata == k, Cata.source == k1)
                c.delete_instance()
                print '删除 {k}, {k1}'.format(k=k, k1=k1)
            except:
                print ''
