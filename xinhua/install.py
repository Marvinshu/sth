#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import APP
import MySQLdb
from hashlib import md5
import time


def main():
    print 'Starting ...'
    mysql_host = raw_input('Input MySQL host (localhost):')
    mysql_host = mysql_host or 'localhost'

    mysql_user = raw_input('Input MySQL root user:')
    mysql_pwd = raw_input('Input MySQL password:')
    mysql_db = raw_input('Input MySQL database (app):'.format(app=APP))
    mysql_db = mysql_db or APP

    print 'Creating database ...'
    db = MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_pwd)
    c = db.cursor()
    c.execute('CREATE DATABASE `{db}` CHARACTER SET utf8 COLLATE utf8_general_ci;'.format(db=mysql_db))

    db = MySQLdb.connect(host=mysql_host, user=mysql_user,
                         passwd=mysql_pwd, db=mysql_db)
    c = db.cursor()
    c.execute("""CREATE TABLE `{db}`.`user` (
                 `id` INT NOT NULL AUTO_INCREMENT,
                 `user` VARCHAR(32) NULL,
                 `pwd` VARCHAR(32) NULL,
                 `create_time` INT NULL,
                 PRIMARY KEY (`id`));""".format(db=mysql_db))

    user = 'god'
    pwd = md5('OhMyGod20!@').hexdigest()
    create_time = int(time.time())

    c.execute("""INSERT INTO `{db}`.`user` (
                     `user`,
                     `pwd`,
                     `create_time`)
                 VALUES(
                     'god',
                     {pwd},
                     {create_time}); """.format(user_name=user,
                                                pwd=pwd,
                                                creat_time=create_time))

    print 'Done ...'


if __name__ == '__main__':
    main()
