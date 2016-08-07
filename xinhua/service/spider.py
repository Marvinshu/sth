#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa

import sys
import requests
import json
from extract import extract

reload(sys)
sys.setdefaultencoding('utf-8')


class Spider():
    def weibo_spider(self, url):
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
            count = extract('<strong class=\\"W_f12\\">', '<\/strong>', r.text)
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
        r = requests.get(url)
        if r.status_code == 200:
            v_id = extract("var videoId = '", "';", r.text)
            url_ = 'http://v.youku.com/QVideo/~ajax/getVideoPlayInfo?id={v_id}&type=vv'.format(v_id=v_id)
            r = requests.get(url_)
            if r.status_code == 200:
                data = json.loads(r.text)
                return data.get('vv', 0)

    def tengxun_spider(self, url):
        ''' 腾讯视频爬虫 '''
        r = requests.get(url, )
        if r.status_code == 200:
            count = extract('class="num">', "</em>", r.text).encode('ISO-8859-1').encode('utf-8')
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
    url = 'http://v.youku.com/v_show/id_XMTY3NDUwODE5Ng==.html?f=27840131&from=y1.3-idx-beta-1519-23042.223465.4-1'
    print Spider().youku_spider(url)


if __name__ == '__main__':
    main()
