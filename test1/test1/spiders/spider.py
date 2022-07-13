import scrapy

from test1.items import MyItem
class mySpider(scrapy.spiders.Spider):
    name = "bupt_teacher"
    allowed_domains = ["teacher.bupt.edu.cn/"]
    for j in range(1,8):
        start_urls = [f"https://teacher.bupt.edu.cn/xyjslb.jsp?totalpage=22&PAGENUM={j}&urltype=tsites.CollegeTeacherList&wbtreeid=1004&id=2367&lang=zh_CN"]

        def parse(self, response):
            item = MyItem()  # 生成对象用于接收爬取的数据
            for i in range(1, 7, 1):
                item['name'] = response.xpath('/html/body/div/div[2]/div[2]/div[2]/ul/li[{}]/a/div[2]/h2/text()'.format(i)).extract()
                item['job_title'] = response.xpath('/html/body/div/div[2]/div[2]/div[2]/ul/li[{}]/a/div[2]/p[1]/text()'.format(i)).extract()
                item['education'] = response.xpath('/html/body/div/div[2]/div[2]/div[2]/ul/li[{}]/a/div[2]/p[2]/text()'.format(i)).extract()
                item['mail'] = response.xpath('/html/body/div/div[2]/div[2]/div[2]/ul/li[{}]/a/div[2]/p[4]/text()'.format(i)).extract()


                print("------",item['name'], item['job_title'], item['education'], item['mail'])
                yield(item)
