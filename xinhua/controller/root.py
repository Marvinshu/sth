#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa

from _base import BaseHandler, LoginHandler
from misc._route import route

from model.url import URL
from model.cata import Cata
from model.mod_log import ModLog

from service.service import get_template_dict


@route('/login')
class Login(BaseHandler):
    def get(self):
        self.render()


@route('/report')
class IndexShow(BaseHandler):
    def get(self):
        d = get_template_dict()
        for cata in Cata.select():
            d[cata.cata][cata.source] = dict(cata=cata.cata_cn, view=cata.view__)
        self.render(data=d)


@route('/')
class Index(LoginHandler):
    def get(self):
        d = get_template_dict()
        for cata in Cata.select():
            d[cata.cata][cata.source] = dict(cata=cata.cata_cn, view=cata.view)

        self.render(data=d)


@route('/url')
class Url(LoginHandler):
    def get(self):
        self.render()


@route('/url_mgr')
class UrlMgr(LoginHandler):
    def get(self):
        cata = self.get_argument('cata', None)
        source = self.get_argument('source', None)
        limit = int(self.get_argument('limit', 50) or 50)
        page = int(self.get_argument('page', 1) or 1)

        offset = (page - 1) * limit

        url = "{path}?limit={limit}".format(path=self.request.path, page=page, limit=limit)
        q = URL.select()
        if cata:
            q = q.where(URL.cata == cata)
            url = "{url}&cata={cata}".format(url=url, cata=cata)
        if source:
            q = q.where(URL.source == source)
            url = "{url}&source={source}".format(url=url, source=source)

        url_li = q.order_by(URL.create_time.desc()).offset(offset).limit(limit)

        count = q.count()
        page_count = count / limit + (0 if count % limit == 0 else 1)

        self.render(url_li=url_li, url_=url,
                    page_count=page_count, limit=limit,
                    page=page, count=count,
                    cata=cata, source=source)


@route('/user_mgr')
class UserMgr(LoginHandler):
    def get(self):
        self.render()


@route('/log')
class Log(LoginHandler):
    def get(self):
        li = ModLog.select()
        self.render(li=li)


@route('/logout')
class Logout(LoginHandler):
    def get(self):
        self.clear_cookie('user')
        self.redirect('/')
