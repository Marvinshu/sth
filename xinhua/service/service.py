#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import time
from os import path
from model.url import URL
from model.cata import Cata
from spider import Spider
from misc.const import d_cata, d_source


def get_template_dict():
    d_ret = dict()
    for k in d_cata.keys():
        d_ = dict()
        for k1 in d_source.keys():
            d_[k1] = 0

        d_ret[k] = d_

    return d_ret


def get_url_view_count():
    data = get_template_dict()
    with open('/var/log/xinhua/xinhua_spider.log', 'a+') as f:
        spider = Spider()
        for url in URL.select():
            try:
                view = getattr(spider, "{source}_spider".format(source=url.source))(url.url)
                if view:
                    view = int(view)
                    url.view = view
                    url.view_ = view
                    url.save()
                    data[url.cata][url.source] += view
            except Exception as e:
                d = dict(
                    url=url.url,
                    time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
                    cata=url.cata_cn,
                    source=url.source_cn,
                    view=url.view
                )
                s = ('Error: {time},{cata},{source},{view},{url}\n').format(**d)
                print s
                f.write(s)
                f.write(str(e))
                f.write('\n')

    return data


def save_statistic(d):
    for k, v in d.iteritems():
        for k1, v1 in v.iteritems():
            cata = Cata.get(Cata.cata == str(k), Cata.source == str(k1))
            if cata:
                v1 = int(v1)
                cata.view = v1
                cata.view_ = v1
                cata.save()


def export_report(view):
    d = get_template_dict()
    for cata in Cata.select():
        d[cata.cata][cata.source] = dict(cata=cata.cata_cn, view=getattr(cata, view))

    header = '#,微博热点,百度文库,百度知道,天涯论坛,爱奇艺,优酷,腾讯视频\n'
    path_ = path.join(path.dirname(path.abspath(__file__)), '../static/report/')
    fi = '{path}data_{view}.csv'.format(path=path_, view=view)
    with open(fi, 'w+') as f:
        f.write(header)
        for k, v in d.iteritems():
            d = dict(
                cata=v.get('weibo').get('cata', ''),
                weibo=v.get('weibo').get('view', ''),
                wenku=v.get('wenku').get('view', ''),
                zhidao=v.get('zhidao').get('view', ''),
                tianya=v.get('tianya').get('view', ''),
                iqiyi=v.get('iqiyi').get('view', ''),
                youku=v.get('youku').get('view', ''),
                tengxun=v.get('tengxun').get('view', '')
            )
            f.write('{cata},{weibo},{wenku},{zhidao},{tianya},{iqiyi},{youku},{tengxun}\n'.format(**d))


def main():
    d = get_url_view_count()
    save_statistic(d)
    for view in ['view', 'view_']:
        export_report(view)


if __name__ == '__main__':
    main()
