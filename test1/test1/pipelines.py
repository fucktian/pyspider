import csv



class MyPipeline(object):
    def open_spider(self, spider):
        try:
            self.file = open('My_Data.csv',"w",encoding="UTF-8")
        except Exception as err:
            print(err)


    def process_item(self, item, spider):
        dict_item = dict(item)  #生成字典对象
        # print("**********", type(item['job_title']), type(item['job_title'][0]), item)
        if item['mail']:
            csv_str = item['name'][0]+','+item['job_title'][0]+','+item['education'][0]+','+item['mail'][0]+'\n'
        else:
            csv_str = item['name'][0]+','+item['job_title'][0]+','+item['education'][0]+','+'\n'
        # 生成csv串
        self.file.write(csv_str)
        return item


    def close_spider(self,spider):
        self.file.close()