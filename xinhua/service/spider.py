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
        if '?' in url:
            url = '{url}&beta&'.format(url=url)
        else:
            url = '{url}?beta&'.format(url=url)

        r = requests.get(url)
        vid = 0
        if r.status_code == 200:
            vid = extract('videoId:"', '"', r.text)

        if vid:
            url_ = 'http://v.youku.com/action/getVideoPlayInfo?beta&vid={vid}'.format(vid=vid)
            r = requests.get(url_)
            if r.status_code == 200:
                data = json.loads(r.text)
                vv = data.get('data', dict()).get('stat', dict()).get('vv', 0)
                return int(vv.replace(',', ''))

    def tengxun_spider(self, url):
        ''' 腾讯视频爬虫 '''
        r = requests.get(url)
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

    def xinlang_spider(self, url):
        ''' 新浪论坛爬虫 '''
        r = requests.get(url)
        if r.status_code == 200:
            count = extract('<font color="#ff0000"> ', '</font>', r.text)

            return int(count.replace(',', ''))

    def wangyi_spider(self, url):
        ''' 网易论坛爬虫 '''
        r = requests.get(url)
        if r.status_code == 200:
            return int(extract('<span class="red">', '</span> 浏览', r.text))

    def xici_spider(self, url):
        ''' 西祠胡同爬虫 '''
        return 0


def main():
    url = 'http://bbs.news.163.com/bbs/society/615189648.html'
    print Spider().wangyi_spider(url)


if __name__ == '__main__':
    main()
