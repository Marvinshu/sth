#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import hashlib
from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField


class User(Base):
    id = PrimaryKeyField()
    user = CharField(max_length=32, unique=True)
    name = CharField(max_length=32)
    pwd = CharField(max_length=32)
    create_time = IntegerField(default=int(time.time()))

    class Meta:
        indexes = ((('user', 'pwd'), True),)

    @classmethod
    def login(cls, user, pwd):
        user_ = None
        try:
            user_ = User.get(User.user == user, User.pwd == hashlib.md5(pwd).hexdigest())
        except User.DoesNotExist:
            # 用户不存在
            user_ = None

        return user_

    def reset(self, new_pwd):
        ''' 重置密码
            params:
                user: 用户名
                new_pwd: 新密码
        '''
        self.pwd = hashlib.md5(new_pwd).hexdigest()
        self.save()
