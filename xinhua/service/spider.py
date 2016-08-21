#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa

import sys
import requests
import json
import re
from extract import extract
from weibo_login import login

reload(sys)
sys.setdefaultencoding('utf-8')


class Spider():
    def weibo_spider(self, url):
        ''' 微博热点话题爬虫 '''
        username = 'tonghuashuai@126.com'
        password = 'OhMyGod20!@'
        session = login(username, password)

        url = "{url}&retcode=6102".format(url=url)
        r = session.get(url)

        if r.status_code == 200:
            p = '<strong class=\\\\"W_f1[0-9]\\\\">(.*?)<\\\/strong>'
            m = re.findall(p, r.text)
            if m:
                count = m[0]

            return self.deal_unit(count)

    def wenku_spider(self, url):
        ''' 百度文库爬虫 '''
        doc_id = extract('http://wenku.baidu.com/view/', '.html', url)
        url_ = 'http://wenku.baidu.com/doc/interface/docCount?doc_id={doc_id}'.format(doc_id=doc_id)

        r = requests.get(url_)
        if r.status_code == 200:
            txt = r.text
            data = json.loads(txt) or dict()

            return data.get('viewCount', 0)

    def zhidao_spider(self, url):
        ''' 百度知道爬虫 '''
        id = extract('http://zhidao.baidu.com/question/', '.html', url)
        url_ = 'http://zhidao.baidu.com/api/qbpv?q={id}'.format(id=id)
        r = requests.get(url_)
        if r.status_code == 200:
            return r.text

    def tianya_spider(self, url):
        ''' 天涯爬虫 '''
        r = requests.get(url)
        if r.status_code == 200:
            return extract(u'<span>点击：', '</span>', r.text)

    def iqiyi_spider(self, url):
        ''' 爱奇艺爬虫 '''
        r = requests.get(url)
        if r.status_code == 200:
            v_id = extract('data-player-tvid="', '"', r.text)
            url_ = 'http://mixer.video.iqiyi.com/jp/mixin/videos/{v_id}'.format(v_id=v_id)
            r = requests.get(url_)
            if r.status_code == 200:
                return extract('"playCount":', ',"', r.text)

    def youku_spider(self, url):
        ''' 优酷视频爬虫 '''
        url_ = "https://openapi.youku.com/v2/videos/show_basic.json?video_url={url}&client_id=66655b02396537f4".format(url=url)
        r = requests.get(url_)
        if r.status_code == 200:
            data = json.loads(r.text)
            return data.get('view_count', 0)

    def tengxun_spider(self, url):
        ''' 腾讯视频爬虫 '''
        r = requests.get(url, )
        if r.status_code == 200:
            count = extract('class="num">', "</em>", r.text)

            # 腾讯视频变态的编码不确定
            if r.encoding == 'ISO-8859-1':
                count = count.encode('ISO-8859-1').encode('utf-8')

            return self.deal_unit(count)

    def deal_unit(self, count):
        ''' 单位转换 '''
        if count:
            d_unit = {'亿': 100000000, '万': 10000}
            for k, v in d_unit.iteritems():
                if k in count:
                    count = int(float(count.replace(k, '')) * v)
                    break
        return count


def main():
    url = 'http://weibo.com/p/100808dc16b2f5eb002e9558b916f31b59cb6a?k=%E4%B8%80%E5%9D%97%E6%8A%95%E5%90%A7&from=501&_from_=huati_topic'
    print Spider().weibo_spider(url)


if __name__ == '__main__':
    main()
