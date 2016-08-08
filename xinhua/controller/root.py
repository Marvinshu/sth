#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
from _base import Base_, Base
from misc._route import route
from model.url import URL
from model.cata import Cata
from service.service import get_template_dict


@route('/login')
class Login(Base_):
    def get(self):
        self.render()


@route('/zhimakaimen')
class IndexShow(Base_):
    def get(self):
        d = get_template_dict()
        for cata in Cata.select():
            d[cata.cata][cata.source] = dict(cata=cata.cata_cn, view=cata.view__)
        self.render(data=d)


@route('/')
class Index(Base):
    def get(self):
        d = get_template_dict()
        for cata in Cata.select():
            d[cata.cata][cata.source] = dict(cata=cata.cata_cn, view=cata.view)
        self.render(data=d)


@route('/url')
class Url(Base):
    def get(self):
        self.render()


@route('/url_mgr')
class UrlMgr(Base):
    def get(self):
        url_li = URL.select().order_by(URL.create_time.desc())
        self.render(url_li=url_li)


@route('/user_mgr')
class UserMgr(Base):
    def get(self):
        self.render()


@route('/logout')
class Logout(Base):
    def get(self):
        self.clear_cookie('user')
        self.redirect('/')
