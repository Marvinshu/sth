#!/usr/bin/env python
# -*- coding: utf-8 -*-


from _base import Base
from misc._route import route


@route('/login')
class Login(Base):
    def get(self):
        self.render()


@route('/')
class Index(Base):
    def get(self):
        self.render()
