#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import re

class TransChinese:
    def init(self):
        self.result = {}

    def readFile(self,path):
        with open(path, 'r') as f:
            data = f.readline()
            self.collectWord(data)


    def collectWord(self,text):
        pattern = re.compile(u'(?P<newcn>[\u4e00-\u9fa5]*)', re.M)  
        origin_result = pattern.finditer(text)
        for match in origin_result: 
            print "-----------"
            print (match.groups())


if __name__=="__main__":
    trans= TransChinese() 
    trans.collectWord("<input label='test' field='你好大家好'/>")


    