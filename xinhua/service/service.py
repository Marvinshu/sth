#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import time
from model.url import URL
from model.cata import Cata
from spider import Spider
from collections import defaultdict


def get_url_view_count():
    data = defaultdict(int)
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
                    data[url.cata] += view
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
        cata = Cata.get(Cata.name == str(k))
        if cata:
            v = str(v[0])
            cata.view = v
            cata.view_ = v
            cata.save()


def main():
    # d = get_url_view_count()
    d = dict(
        cata1=1000,
        cata2=3000
    )
    save_statistic(d)


if __name__ == '__main__':
    main()
