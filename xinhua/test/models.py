#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
from model._base import drop_table, init_db


def main():
    init_db()
    drop_table()


if __name__ == '__main__':
    main()
