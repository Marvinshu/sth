#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests

import json

from extract import extract

reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    pass

    # url = 'http://weibo.com/p/1008086447e72026b53b1321c9ec1cd9a5e549?k=%E5%8C%97%E4%BA%AC%E6%8F%90%E4%B8%AA%E9%86%92%E5%84%BF&from=501&_from_=huati_topic'
    # print weibo_spider(url)

    # url = 'http://wenku.baidu.com/view/57b4a8e1524de518964b7d77.html?from=search'
    # print wenku_spider(url)

    # url = 'http://zhidao.baidu.com/question/135630117010643285.html?fr=iks&word=%D6%AA%B5%C0&ie=gbk'
    # print zhidao_spider(url)

    # url = 'http://bbs.tianya.cn/post-funinfo-7022011-1.shtml'
    # print tianya_spider(url)

    # url = 'http://www.iqiyi.com/v_19rrkyywoo.html?src=focustext_1_20130410_14#curid=468199400_9f4cf89365eede42a2f600e8a5c9b9c1'
    # print iqiyi_spider(url)

    # url = 'http://v.youku.com/v_show/id_XMTQ3MDU2MzA5Ng==.html?from=s1.8-3-1.1'
    # print youku_spider(url)

    url = 'http://v.qq.com/x/cover/kgs4kzwb987o4cf.html?vid=l0318msoh9o'
    print tengxun_spider(url)


def weibo_spider(url):
    ''' 微博热点话题爬虫 '''
    cookies = dict(
        _s_tentry="-",
        ALF="1471057608",
        Apache="1626248766746.27.1470452752564",
        Hm_lvt_b9435dbda402e06581dd35b7fbb6b299="1462168148",
        login_sid_t="3b3f77bb23781986615fdd72e3843e87",
        SCF="AvdOId1m5vongD8CTJTzUzwBjrWsF4qL5ZnlbDCNLlJrV4ci2u3Mg-uTKyoSXLU5ZPcRY2KMpRuLqK1g4BV8sTM.",
        SINAGLOBAL="9691216484643.52.1444141565833",
        SSOLoginState="1470452813",
        SUB="_2A256oSQcDeTxGedL41AY-S3JzDiIHXVZ1xLUrDV8PUNbmtBeLVfgkW9WcYcgZ-a-VvfUjmIpQ4EMur0gFA..",
        SUBP="0033WrSXqPxfM725Ws9jqgMF55529P9D9WWOdsO-lcc6agqe.jwGqFFY5JpX5K2hUgL.Fo2f1hz41KefS0B2dJLoINRLxK-L12-L1-qLxKqL1-BLBK-LxKML1-eL1-qLxKML1-2L1hBLxKqL1-eL1h.LxKnLB.qL1K.LxKBLBo.L1hnLxK.L1K-LB.qLxKML1-2L1hBLxK-LB.-LB--LxK-L12BL1-2LxKqL1KnLBo-LxKMLBKMLBo5LxK-L1K-L122t",
        SUHB="0QSIVNqPn1akMs",
        ULV="1470452753567:19:1:1:1626248766746.27.1470452752564:1463831355622",
        un="tonghuashuai@126.com",
        UOR="www.pythontab.com,widget.weibo.com,auto.ifeng.com",
        WBStore="4561a2111a75ddae|undefined",
        WBtopGlobal_register_version="90c4d37e0334154f",
    )

    r = requests.get(url, cookies=cookies)

    if r.status_code == 200:
        # 需要转换单位
        return extract('<strong class=\\"W_f12\\">', '<\/strong>', r.text)


def wenku_spider(url):
    ''' 百度文库爬虫 '''
    doc_id = extract('http://wenku.baidu.com/view/', '.html', url)
    url_ = 'http://wenku.baidu.com/doc/interface/docCount?doc_id={doc_id}'.format(doc_id=doc_id)

    r = requests.get(url_)
    if r.status_code == 200:
        txt = r.text
        data = json.loads(txt) or dict()

        return data.get('viewCount', 0)


def zhidao_spider(url):
    ''' 百度知道爬虫 '''
    id = extract('http://zhidao.baidu.com/question/', '.html', url)
    url_ = 'http://zhidao.baidu.com/api/qbpv?q={id}'.format(id=id)
    r = requests.get(url_)
    if r.status_code == 200:
        return r.text


def tianya_spider(url):
    ''' 天涯爬虫 '''
    r = requests.get(url)
    if r.status_code == 200:
        return extract(u'<span>点击：', '</span>', r.text)


def iqiyi_spider(url):
    ''' 爱奇艺爬虫 '''
    r = requests.get(url)
    if r.status_code == 200:
        v_id = extract('data-player-tvid="', '"', r.text)
        url_ = 'http://mixer.video.iqiyi.com/jp/mixin/videos/{v_id}'.format(v_id=v_id)
        r = requests.get(url_)
        if r.status_code == 200:
            return extract('"playCount":', ',"', r.text)


def youku_spider(url):
    ''' 优酷视频爬虫 '''
    r = requests.get(url)
    if r.status_code == 200:
        v_id = extract("var videoId = '", "';", r.text)
        url_ = 'http://v.youku.com/QVideo/~ajax/getVideoPlayInfo?id={v_id}&type=vv'.format(v_id=v_id)
        r = requests.get(url_)
        if r.status_code == 200:
            data = json.loads(r.text)
            return data.get('vv', 0)


def tengxun_spider(url):
    ''' 腾讯视频爬虫 '''
    r = requests.get(url, )
    if r.status_code == 200:
        return extract('class="num">', "</em>", r.text).encode('ISO-8859-1').encode('utf-8')
    # 需要转换单位


if __name__ == '__main__':
    main()
