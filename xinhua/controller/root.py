#!/usr/bin/env python
# -*- coding: utf-8 -*-


from _base import Base_, Base
from misc._route import route
from model.url import URL


@route('/login')
class Login(Base_):
    def get(self):
        self.render()


@route('/')
class Index(Base):
    def get(self):
        self.render()


@route('/url')
class Url(Base):
    def get(self):
        self.render()


@route('/url_mgr')
class UrlMgr(Base):
    def get(self):
        url_li = URL.select().order_by(URL.create_time.desc())
        self.render(url_li=url_li)
