#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
from model._base import drop_table, init_db


def main():
    drop_table()
    init_db()

    from model.cata import Cata
    d = dict(
        cata1="大师谈",
        cata2="一点通",
        cata3="风采录",
        cata4="分类4",
        cata5="分类5"
    )
    for k in d.keys():
        d_source = dict(
            weibo="微博热点",
            wenku="百度文库",
            zhidao="百度知道",
            tianya="天涯论坛",
            iqiyi="爱奇艺",
            youku="优酷",
            tengxun="腾讯视频",
        )
        for k1 in d_source.keys():
            d_ = dict(
                cata=k,
                source=k1,
            )
            Cata.create(**d_)


if __name__ == '__main__':
    # main()
    init_db()
