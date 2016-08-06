#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
from model._base import drop_table, init_db


def main():
    drop_table()
    init_db()


if __name__ == '__main__':
    main()
