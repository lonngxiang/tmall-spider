import scrapy
from lxml import etree
import re
import json
import requests


class TmallSpider(scrapy.Spider):
    name = 'tmall1'
    # allowed_domains = ['tmall.com']
    # start_urls = ['http://tmall.com/']
    handle_httpstatus_list = [302]

    def start_requests(self):
        # word_lists = ['海蓝之谜', '莱珀妮', '希思黎', '娇兰', '阿玛尼', '科颜氏', '兰芝', '倩碧', '碧欧泉', '悦木之源', '芭比波朗', '汤姆福特', 'YSL', '魅可', '阿玛尼', '兰芝', '欧莱雅', '馥蕾诗', '雪肌精', '欧莱雅', '玉兰油', '梦妆', '丸美', 'allie', 'sofina', '悦诗风吟', '自然堂', '百雀羚', '美宝莲', '悦诗风吟', '伊蒂之屋', '施华蔻', '滋源', '丝蕴', '阿道夫', '施华蔻', '滋源', 'RYO', '滋源', '黛丝恩', '施华蔻', '芙丽芳丝', '碧柔', '妮维雅洗面', '力士沐浴', '菲诗小铺沐浴', '安宝笛沐浴', '妮维雅男士', '曼秀雷敦男士', '欧莱雅男士', '高夫男士', '妮维雅面霜']
        # word_lists = ["资生堂","香奈儿","CPB","IPSA","NARS","怡丽丝尔","安热沙","珊珂","泊美","姬芮","悠莱","丝蓓绮","惠润","玛馨妮","可悠然","吾诺","水之密语"]
        word_lists = ["悠莱"]
        for j in range(len(word_lists)):
            # def main(word):
            url = "https://list.tmall.com/search_product.htm?q={}".format(word_lists[j])
            print(url)
            headers={
                # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                # "Accept-Encoding": "gzip, deflate, br",
                # "Accept-Language": "zh-CN,zh;q=0.9",
                # "Cache-Control": "max-age=0",
                # "Connection": "keep-alive",
                # "Cookie": "cna=Y/gvEkEdxn8CAXlFS8JxN2dY; _med=dw:1920&dh:1080&pw:1920&ph:1080&ist:0; hng=CN%7Czh-CN%7CCNY%7C156; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; sm4=110114; enc=HO2smibx8TXFWK6FgSZlVd7oT1J3w3asxijvjAPa0BpJFpw85EmeiZuMEbBjxgm8CC7aAUXGTvmEllJjggnhXQ%3D%3D; lid=%E6%B6%9F%E6%BC%AA%E5%9E%84; cq=ccp%3D1; _m_h5_tk=70693ec8f3a9732a9a11d835a046f568_1546507438464; _m_h5_tk_enc=837fb019627bbe93ea6faba6f9ca16df; t=9112f19023b58d6a7e797c127de1caa6; _tb_token_=f0a5b7e86358e; cookie2=1975bf237f6e15d1c382ab846ae07188; res=scroll%3A1903*5711-client%3A1903*969-offset%3A1903*5711-screen%3A1920*1080; pnm_cku822=098%23E1hvmQvUvbpvUvCkvvvvvjiPR2dZzj3EPsqwAj3mPmPOQj1PPLL9gjYbn2c91jEvRphvCvvvvvvPvpvhvv2MMQhCvvOvCvvvphvEvpCWvHe9vvwGFOcnDBmfJ9kx6acEn1vDNr1lYE7re160kE0xkC46NZdptWkQRqwiLO2vqU0QKoZHgRFEDLuTWDAvD7zvdigDNr1lKE0ARdyCvmFMMMMnphvZ2vvv96CvpvQ5vvm2phCvhRvvvUnvphvppvvv9slvpCvIuphvmvvv92B7iGs4kphvC99vvOCzBuwCvvpvvUmm; l=aBZu-uDGysaSOMbBCMaJ0sRy67071vZPnvJy1MamzTEhN7MzkeCXjjro-VwRj_qC5TUy_K-5F; isg=BDo6VelIMpu1kb5OHQxMyKlri2CcQ4y7aBeH2UQz5E2YN9pxLHqk1sZNg4NOpzZd",
                # "Host": "list.tmall.com",
                # "Upgrade-Insecure-Requests": "1",
                # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
                "Cookie":"cna=VBnIFJDwkEMCASvd1de370ca8be; t=f3f486e8fec15f703faa04847847fb90; _tb_token_=33e711a393808; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=W5iHLLyFfXVRCJf5lG0u7A%3D%3D&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=true&pas=0&cookie14=UoTYMbifUJZCrQ%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByE%2BmeDvh%2FG8H4cg%3D&id2=UNJV3228xVRfDw%3D%3D&nk2=DkXelE8vooZY&lg2=VFC%2FuZ9ayeYq2g%3D%3D; tracknick=musicclub; _l_g_=Ug%3D%3D; ck1=""; unb=3242090043; lgc=musicclub; cookie1=BxpWAvSw9Ktp2IDNXcqup0k0qFvqySQ%2FoPdC7GYiGec%3D; login=true; cookie17=UNJV3228xVRfDw%3D%3D; _nk_=musicclub; uss=""; csg=82b43528; skt=f60e5032aeb2207b; enc=CBIgd%2FdVWUkuMA5k6khrCTVUzryDKdlBJUDE0QiYG71RV4sYN4SHz8hDl%2BYDL1gAtuqIenzy%2B94srVmvlW2IHw%3D%3D; _med=dw:1280&dh:720&pw:1920&ph:1080&ist:0; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; swfstore=116691; tt=tmall-main; x=__ll%3D-1%26_ato%3D0; pnm_cku822=098%23E1hvL9vUvbpvUpCkvvvvvjiPR2Swzj1WR25Zgj3mPmPpsjYnR2LwzjnvPLLZ6j3ER2yCvvpvvvvv2QhvCPMMvvvCvpvVvvpvvhCvkphvC99vvOCzBuyCvv9vvUv6juzBpfyCvm9vvvvvphvvvvvv99CvpvkEvvmmvhCvmhWvvUUvphvUI9vv99CvpvkkmphvLv9qsvvjW%2FFp1npXHFXXiXVvQE01Ux8x9WLUjLyDZacEKOmAdcZIYExrA8TrEcqOac7Q%2Bul68NoxfaoKj5lR%2B8c61EyXwyKQ0f0DW3m5vpvhvvmv99%3D%3D; res=scroll%3A1263*5710-client%3A1263*610-offset%3A1263*5710-screen%3A1280*720; whl=-1%260%260%260; isg=BBQUyQZNNIYeqaBKdbCuv5cp5VJGxTkpIul5K671FR8imbXj13mW54JbndGkUHCv",
                # "Cookie": "cna=Y/gvEkEdxn8CAXlFS8JxN2dY; _med=dw:1920&dh:1080&pw:1920&ph:1080&ist:0; hng=CN%7Czh-CN%7CCNY%7C156; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; sm4=110114; enc=HO2smibx8TXFWK6FgSZlVd7oT1J3w3asxijvjAPa0BpJFpw85EmeiZuMEbBjxgm8CC7aAUXGTvmEllJjggnhXQ%3D%3D; lid=%E6%B6%9F%E6%BC%AA%E5%9E%84; cq=ccp%3D1; _m_h5_tk=70693ec8f3a9732a9a11d835a046f568_1546507438464; _m_h5_tk_enc=837fb019627bbe93ea6faba6f9ca16df; t=9112f19023b58d6a7e797c127de1caa6; _tb_token_=f0a5b7e86358e; cookie2=1975bf237f6e15d1c382ab846ae07188; res=scroll%3A1903*5711-client%3A1903*969-offset%3A1903*5711-screen%3A1920*1080; pnm_cku822=098%23E1hvmQvUvbpvUvCkvvvvvjiPR2dZzj3EPsqwAj3mPmPOQj1PPLL9gjYbn2c91jEvRphvCvvvvvvPvpvhvv2MMQhCvvOvCvvvphvEvpCWvHe9vvwGFOcnDBmfJ9kx6acEn1vDNr1lYE7re160kE0xkC46NZdptWkQRqwiLO2vqU0QKoZHgRFEDLuTWDAvD7zvdigDNr1lKE0ARdyCvmFMMMMnphvZ2vvv96CvpvQ5vvm2phCvhRvvvUnvphvppvvv9slvpCvIuphvmvvv92B7iGs4kphvC99vvOCzBuwCvvpvvUmm; l=aBZu-uDGysaSOMbBCMaJ0sRy67071vZPnvJy1MamzTEhN7MzkeCXjjro-VwRj_qC5TUy_K-5F; isg=BDo6VelIMpu1kb5OHQxMyKlri2CcQ4y7aBeH2UQz5E2YN9pxLHqk1sZNg4NOpzZd",
                "authority":"list.tmall.com",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",

            }
            yield scrapy.Request(url=url,headers=headers,callback=self.parse1)


    def parse1(self, response):
        # print(response.text)
        html1 = etree.HTML(response.text)
        print(len(html1.xpath('//div[@class="product-iWrap"]')))
        print("++++++++++++++++++")
        # for i in range(1):
        for i in range(len(html1.xpath('//div[@class="product-iWrap"]'))):
            product_url = html1.xpath(
                '//div[@class="product-iWrap"]//*[@class="productTitle" or contains(@class,"productTitle")]/a[1]/@href')[i]
            print(product_url)
            product_id = re.findall('[&\?]id=(.*?)&', product_url, re.S)[0]
            print(product_id)
            sell_id = re.findall('user_id=(.*?)&', product_url, re.S)[0]
            url1 = "https://detail.tmall.com/item.htm?id={}".format(product_id)
            product_title1 = html1.xpath(
                '//div[@class="product-iWrap"]//*[@class="productTitle" or contains(@class,"productTitle")]/a[1]')[i]
            product_title = product_title1.xpath("string(.)").strip()
            print(product_title)
            print(product_title, product_id, sell_id, product_url, "\n")
            for m in range(2):
                # url="https://rate.tmall.com/list_detail_rate.htm"
                url2 = "https://rate.tmall.com/list_detail_rate.htm?itemId={}&sellerId={}&currentPage={}".format(product_id, sell_id,m + 1)
                print(url2)
                headers1 = {
                    "authority":"rate.tmall.com",
                    "method":"GET",
                    "scheme":"https",
                    "accept":"*/*",
                    "accept-encoding":"gzip, deflate, br",
                    "accept-language":"zh-CN,zh;q=0.9",
                    "cookie":"cna=Y/gvEkEdxn8CAXlFS8Jg=CN%7Czh-CN%7CCNY%7C156; uc1=cookie15=VFC%2FuZ9ayeYq2g%3D%3D; uc3=vt3=F8dByRMGABk%2F9ypnSPI%3D&id2=VAFaC64q7QnX&nk2=okKCgOPi&lg2=V32FPkk%2Fw0dUvg%3D%3D; tracknick=%5Cu6D9F%5Cu6F2A%5Cu5784; lid=%E6%B6%9F%E6%BC%AA%E5%9E%84; _l_g_=Ug%3D%3D; unb=705807873; lgc=%5Cu6D9F%5Cu6F2A%5Cu5784; cookie1=VAYrG4g5P7m343E16lVP62IC5DHsXMLSw0SctPbwLR0%3D; login=true; cookie17=VAFaC64q7QnX; cookie2=157e6a74cd30d191b9059b3db4528c71; _nk_=%5Cu6D9F%5Cu6F2A%5Cu5784; t=9112f19023b58d6a7e797c127de1caa6; sg=%E5%9E%8436; csg=fc322464; _tb_token_=e319fb776eb5e; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; whl=-1%260%260%260; x5sec=7b22726174656d616e616765723b32223a226131663338313366373636376139386230353064393932333633393736383537434c4f436c2b4546454c6134694d75486874477235414561437a63774e5467774e7a67334d7a7378227d; l=aBZu-uDGysaSOrzKzMaY_MNDH707gvfPNK5y1MayQTEhNP3AkeCXjJtoWMsLn_DX7ofhOouHI-a..; isg=BHZ2kDnRNuT9DcIyeWDIPEVfx6y4P7uuVKNbheBffdn2Ixe9SCXd4cbVP7_qjbLp",
                    "referer":"https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15884659123.103.42684d47xxbPpL&id=567935633478&rn=b030d97bc9c089d8c7ed425dc8ca7805&abbucket=17&skuId=3625875477451",
                    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
                }
                yield scrapy.Request(url=url2,headers=headers1, meta={"url1":url1,"context":product_title},callback=self.parse)


    def parse(self, response):
        cotents_all = {}

        html2 = response.text
        html2 = re.findall('jsonp.*?\((.*)\)', html2, re.S)[0]
        new_html2 = json.loads(html2)
        print(html2)
        # page_num = round(int(new_html2['rateDetail']['rateCount']['total']) / 20)
        for w in range(len(new_html2['rateDetail']['rateList'])):
            # for j in range(3):
            name = new_html2['rateDetail']['rateList'][w]['displayUserNick']
            user_id = new_html2['rateDetail']['rateList'][w]['id']
            time = new_html2['rateDetail']['rateList'][w]['rateDate']
            content = new_html2['rateDetail']['rateList'][w]['rateContent']

            cotents_all['url'] = response.meta['url1']
            cotents_all['id'] = user_id
            cotents_all['context'] = response.meta['context']
            cotents_all['content'] = content
            cotents_all['tC'] = time
            cotents_all['user'] = {"displayName": name}

            print(w + 1, name, time, content)

            try:
                # response=requests.post(url="http://service.lavector.com/api/v1/es/bulk",json=lists_all)
                headers2 = {'Content-Type': 'application/json'}
                # headers2 = {"Content-Type": "application/x-www-form-urlencoded"}
                # data=json.dumps(lists_all)
                # response=requests.post(url="http://serv/es/bulk",headers=headers2,json=json.dumps(lists_all,ensure_ascii=False))
                response = requests.post(url="http://service./v1/es/bulk/tmall", headers=headers2,
                                         json=cotents_all)
                print(response.status_code)
                print("++++++++++++++++")
            except:
                pass

```

```
# -*- coding:utf-8 -*-
from scrapy import cmdline
# 方式一：注意execute的参数类型为一个列表
cmdline.execute('scrapy crawl tmall1'.split())
```
