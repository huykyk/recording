# -*- coding: utf-8 -*-
#import os
#LTP_DATA_DIR = 'D:/ltp_data'  # ltp模型目录的路径
#par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`
#from pyltp import Parser
#parser = Parser() # 初始化实例
#parser.load(par_model_path)  # 加载模型
#words = ['元芳', '你', '怎么', '看']
#postags = ['nh', 'r', 'r', 'v']
#arcs = parser.parse(words, postags)  # 句法分析
#
#print(
#"\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs)
#)
#parser.release()  # 释放模型

import re

from datetime import datetime


test_date = '他的生日是2016年12月12日 14:34,是个可爱的小宝贝.二宝的生日是2016-12-21 11:34,好可爱的.'

 

test_datetime = '他的生日是2016年12月12日 14:34,是个可爱的小宝贝.二宝的生日是2016-12-21 11:34,好可爱的.'

 

# date

#mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})",test_date)
#
#print(mat.groups())
#
## ('2016-12-12',)
#
#print(mat.group(0))
#
## 2016-12-12

 

date_all = re.findall(r"(\d{4}年\d{1,2}月\d{1,2}日)",test_date)

for item in date_all:

    print (item)

# 2016-12-12

# 2016-12-21
