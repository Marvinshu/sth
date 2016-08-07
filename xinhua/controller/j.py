#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import hashlib

from _base import JsonBase
from misc._route import route
from model.url import URL as URL_
from model.cata import Cata as Cata_


@route('/j/login')
class Login(JsonBase):
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        if username == 'tonghs' and password == 'tonghs':
            user = dict(
                username=username,
                passowrd=password
            )
            self.set_secure_cookie("user", json.dumps(user))
            ret = dict(login=True, msg="")
        else:
            ret = dict(login=False, msg="用户名密码错误")

        self.finish(ret)


@route('/j/url')
class URL(JsonBase):
    def post(self):
        url = self.get_argument('url', '')
        if url:
            data = {k: ''.join(v) for k, v in self.request.arguments.iteritems()}
            url_md5 = hashlib.md5(url).hexdigest()
            data.update(url_md5=url_md5)
            URL_.create(**data)

            ret = dict(result=True)
        else:
            ret = dict(result=False, msg="链接不可为空")

        self.finish(ret)


@route('/j/url/rm')
class URL_rm(JsonBase):
    def post(self):
        id = self.get_argument('id', '')
        if id:
            url = URL_.get(URL_.id == id)
            if url:
                url.delete_instance()

        self.finish()


@route('/j/cata')
class Cata(JsonBase):
    def post(self):
        cata = self.get_argument('cata', '')

        cata_ = ''
        li = list()

        for c in Cata_.select().where(Cata_.cata == cata):
            li.append(dict(name=c.source_cn, value=c.view))
            cata_ = c.cata_cn

        d = dict(
            li=li,
            cata=cata_
        )

        self.finish(data=d)
