# -*- coding: utf-8 -*-
from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse
from os.path import basename,dirname,join
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyFilesPipeline(FilesPipeline):
    # def process_item(self, item, spider):
    #     return item
    # # def file_path(self,request,response=None,info=None):
    #     if not isinstance(request,Request):
    #         _warn()
    #         url=request
    #     else:
    #         url=request.url
    #     if not hasattr(self.file_key,'_base'):
    #         _warn()
    #         return self.file_key(url)
    #     media_guid=hashlib.sha1(to_bytes(url)).hexdigest()
    #     media_ext=os.path.splitext(url)[1]
    #     return 'full/%s%s'%(media_guid,media_ext)
    def file_path(self,request,response=None,info=None):
        # print("*"*50)
        path=urlparse(request.url).path

        # print("路径是:",path)
        return join(basename(dirname(path)),basename(path))