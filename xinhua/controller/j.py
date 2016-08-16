#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import hashlib
import math

from _base import JsonBaseHandler
from misc._route import route

from model._base import db
from model.url import URL as URL_
from model.cata import Cata as Cata_
from model.user import User
from model.mod_log import ModLog

from service.service import export_report


@route('/j/login')
class Login(JsonBaseHandler):
    def post(self):
        user = self.get_argument('username')
        pwd = self.get_argument('password')

        user_ = User.login(user, pwd)
        if user_:
            user_dict = dict(
                user=user,
                name=user_.name
            )
            self.set_secure_cookie("user", json.dumps(user_dict))
            ret = dict(login=True, msg="")
        else:
            ret = dict(login=False, msg="用户名密码错误")

        self.finish(ret)


@route('/j/user/reset_pwd')
class Pwd(JsonBaseHandler):
    def post(self):
        pwd = self.get_argument('pwd')
        new_pwd = self.get_argument('new_pwd')
        re_pwd = self.get_argument('re_pwd')

        ret = dict(result=False, msg="")

        if pwd and new_pwd and re_pwd:
            if new_pwd == re_pwd:
                user = User.login(self.current_user.user, pwd)
                if user:
                    user.reset(new_pwd)
                    ret = dict(result=True, msg="修改成功！")
                else:
                    ret = dict(result=False, msg="原密码输入错误！")

            else:
                ret = dict(result=False, msg="两次输入密码不一致！")
        else:
            ret = dict(result=False, msg="全部为必填项不可为空！")

        self.finish(ret)


@route('/j/url')
class URL(JsonBaseHandler):
    def post(self):
        url = self.get_argument('url', '')
        cata = self.get_argument('cata', '')
        source = self.get_argument('source', '')
        try:
            if url:
                url = url.replace(' ', '__##__')
                url_li = url.split()
                if url_li:
                    for u in url_li:
                        title, url_ = u.split(',')
                        data = dict(
                            cata=cata,
                            source=source,
                            url=url_,
                            title=title.replace('__##__', ' '),
                            url_md5=hashlib.md5(url_).hexdigest()
                        )
                        URL_.create(**data)

                ret = dict(result=True)
            else:
                ret = dict(result=False, msg="链接不可为空")
        except:
            ret = dict(result=False, msg="批量链接格式错误")

        self.finish(ret)


@route('/j/url/rm')
class URL_rm(JsonBaseHandler):
    def post(self):
        id = self.get_argument('id', '')
        if id:
            url = URL_.get(URL_.id == id)
            if url:
                url.delete_instance()

        self.finish()


@route('/j/cata')
class Cata(JsonBaseHandler):
    def post(self):
        cata = self.get_argument('cata', '')
        view = self.get_argument('view', 'view')

        cata_ = ''
        li = list()

        for c in Cata_.select().where(Cata_.cata == cata):
            li.append(dict(name=c.source_cn, value=getattr(c, view)))
            cata_ = c.cata_cn

        d = dict(
            li=li,
            cata=cata_
        )

        self.finish(data=d)


@route('/j/view/add')
class ViewAddition(JsonBaseHandler):
    def post(self):
        li = self.get_argument('li', '')
        li = json.loads(li)
        if li:
            with db.atomic():
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

                        # 写 log
                        ModLog.create(cata=cata, source=source, value=val)

            # 重新生成报表
            for view in ['view', 'view__']:
                export_report(view)

        self.finish()
