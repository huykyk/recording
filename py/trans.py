# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 00:17:44 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-

import codecs
import re
from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer

#读取待处理文本
'''
    读取的文本格式是encoding参数值，codecs函数将其转化为unicode格式。
'''
news_files = codecs.open('D:\\input.txt','r',encoding='utf8')
news_list = news_files.readlines()
#type(news_list[1].encode('utf-8'))


#分句
'''
此函数参数输入的格式必须为str格式，所以直接获取的list里的参数值需要
通过encode('utf-8')，从Unicode转换为str
'''
def sentence_splitter(sentence):
    sents = SentenceSplitter.split(sentence)
#    print('\n'.join(sents))
    sents_list = list(sents)
    return sents_list
    

#分词   
def segmentor(sentence):
    segmentor =  Segmentor()
    segmentor.load('D:\\ltp_data\\cws.model')#加载模型
    words = segmentor.segment(sentence) #分词
    #默认可以这样输出
#    print('\t'.join(words))
    #可以转化成List输出
    word_list = list(words)
    segmentor.release()#释放模型
    return word_list 

#词性标注
def posttagger(words):
    postagger = Postagger()
    postagger.load('D:\\ltp_data\\pos.model')
    posttags=postagger.postag(words)  #词性标注
    postags = list(posttags)
    postagger.release() #释放模型
#    print(type(postags))
    return postags

#命名实体识别
def ner(words,postags):
    print('命名实体开始！')
    recognizer = NamedEntityRecognizer()
    recognizer.load('D:\\ltp_data\\ner.model') #加载模型
    netags = recognizer.recognize(words,postags) #命名实体识别
    for word,ntag in zip(words,netags):
        if(ntag == "S-Nh"):
            to_company_trans.append(word)
        print(word+'/'+ ntag)
    recognizer.release()   #释放模型
    nerttags = list(netags)
    return nerttags



date_meeting = []       #股东会召开时间
company_meeting = []    #股东会公司名称

date_trans = []         #股转发生时间
from_company_trans = []      #股转发生公司1名称
to_company_trans = []

percent_trans = []       #股转发生比例
amount_trans = []       #股转发生金额


f = codecs.open('D:\input.txt','r+',encoding='utf-8')
str = f.read()
sents = sentence_splitter(str)  # 分句


str = str.replace(' ', '')
#print('\n'.join(sents))
for i in sents:

    if (u"转让给" in i) and (u"年" in i) and (u"月" in i) and (u"日" in i):
        

        words = segmentor(i)
        postags = posttagger(words)
        ner(words,postags)

        
        
        i = i.replace(' ', '')
        print(i)
        
        
        date_trans.append(re.findall(r"(\d{4}年\d{1,2}月\d{1,2}日)",i))
        
#        date_trans.append(re.findall(r"(\d{4}年\d{1,2}月\d{1,2}日)",i))
     
#        percent_trans.append(re.findall(r"(\d{2}%)|(\d{2}.\d{2}%)",i))
       
        percent_trans.append(re.findall(r"(\d{2}%)",i))
        
#        amount_trans.append(re.findall(r"(\d{+}万)|(\d{+}.\d{+}万)",i))
        
        amount_trans.append(re.findall(r"(\d+万)",i))
      
#        amount_trans.append(re.findall(r"(\d+万)|(d+.d+万)",i))
        
       
        


for item in date_trans:
    print (item)

for item in to_company_trans:
    print (item)

for item in percent_trans:
    print (item)


for item in amount_trans:
    print (item)    