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
    for k, v in d.iteritems():
        d_ = dict(
            title=k,
            name=v,
        )
        Cata.create(**d_)


if __name__ == '__main__':
    main()
