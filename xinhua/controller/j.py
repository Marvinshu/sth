#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import hashlib
import math

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


@route('/j/view/add')
class ViewAddition(JsonBase):
    def post(self):
        li = self.get_argument('li', '')
        li = json.loads(li)
        if li:
            for o in li:
                id = o.get('id', '')
                val = o.get('val', 0)
                if id and val:
                    val = int(val)
                    cata, source = id.split('_')
                    # 更新总数
                    cata_ = Cata_.get(Cata_.cata == cata, Cata_.source == source)
                    cata_.view_ += val
                    cata_.save()

                    # 更新每个 URL
                    li_url = URL_.select().where(URL_.cata == cata, URL_.source == source)
                    if li_url:
                        per = int(math.ceil(float(val) / float(len(li_url))))
                        for o in li_url:
                            o.view_ += per
                            o.save()

        self.finish()
