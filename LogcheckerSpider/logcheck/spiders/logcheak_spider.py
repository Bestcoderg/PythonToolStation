import scrapy
from urllib.parse import quote
import re



class logcheck(scrapy.Spider):

    name = "logcheck"
    months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51',
            #使用密码登陆后，找到网站的cookie
            'Cookie': ''
        }
        urls = []
        year = "2020"
        if(int(year)%4 == 0 and int(year)%100 != 0):
            self.months[2] = 29;

        url1 = "https://gameadm-lzg-tw.game.koramgame.com/zh-hans/mobile-oper-bill-dn/auction-flow?platform=dn_kunlun_formal&group_id=1&stat_day="
        url2 = "&role_id="

        for month in range(4, 9):
            for day in range(1, self.months[month]+1):
                urls.append(url1+year+'-'+str(month).rjust(2, '0')+'-'+str(day).rjust(2, '0')+url2)
        for day in range(1,15):
            urls.append(url1 + year + '-09-' + str(day).rjust(2, '0') + url2)

        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):

        logout1 = response.xpath('//div[@class=$val1]//table//tbody//tr', val1='table-responsive')
        for tr in logout1:
            # 注意这个 . ,只有使用相对路径节点，才能够正确的取到子节点
            liststr = tr.xpath('.//td//text()').extract()
            strx = ' '.join(liststr)
            if strx == "暂无数据":
                continue
            self.log(strx)
            with open("spiderout.txt", "a+") as f:
                f.write(strx + '\n')



        # self.log(logout1)
        #
        #
        # with open("spiderout.txt", 'a+') as f:
        #
        #     f.write(' '.join(logout1)+'\n')
        # self.log('test of spider')



