# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 00:59:53 2017

@author: Administrator
"""
import codecs
import re
from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer


#p1 1 to 2

p1_from_company_trans = []      #股转发生公司1名称
p1_to_company_trans = []        #股转发生公司2名称
ntag_company1 = []
ntag_company2 = []


#p2 1 to 2 and 3

p2_from_company_trans = []      #股转发生公司1名称
p2_to_company2_trans = []        #股转发生公司2名称
p2_to_company3_trans = []         #股转发生公司3名称

#读取待处理文本
'''
    读取的文本格式是encoding参数值，codecs函数将其转化为unicode格式。
'''
#news_files = codecs.open('D:\\input.txt','r',encoding='utf8')
#news_list = news_files.readlines()
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
    
#    print('命名实体开始！')
    recognizer = NamedEntityRecognizer()
    recognizer.load('D:\\ltp_data\\ner.model') #加载模型
    netags = recognizer.recognize(words,postags) #命名实体识别
    for word,ntag in zip(words,netags):
        pass
#        print(word+'/'+ ntag)

#        while(ntag == "B-Ni" or ntag == "I-Ni" or ntag=="E-Ni"):
#            ntag_company1.append(word) 
#            if(ntag=="E-Ni"):
#                break
##                
##
#        while(ntag == "B-Ni" or ntag == "I-Ni" or ntag=="E-Ni"):
#            ntag_company2.append(word) 
#            if(ntag=="E-Ni"):
#                break
    
    recognizer.release()   #释放模型
    nerttags = list(netags)
    nerwords = list(words)
    
    return nerttags,nerwords

str11 = '''
      2007 年 9 月 28 日，承德海润等 4 位股东共同将其所持海润化工的股权全部转让给烟台海升投资有限责任公司（以下简称“海升投资”）。
        '''
str12 = '''
      2008 年 1 月 20 日，海升投资将持有海润化工的 100%股权转让给烟台有色金属股份有限公司（以下简称“烟台有色”）。
       '''

str13 = '''
      2011 年 7 月 18 日，因 2007 年 9 月 28 日的股权转让存在瑕疵，烟台市芝罘区人民法院判决海润化工设立时的 4 名股东将其持有的股权转让给海升投资的协议无效，有色股份应将其持有海润化工的股权退还给 4 名股东。海润化工的股权结构因此变回到设立之初：葛晓鸣出资 14 万元，占 27%；李惠运出资 12 万元，占 24%；陈香伟出资 12 万元，占 24%；林松斌出资 12 万元，占 24%。
       '''
str14 = '''
        2015 年 6 月 5 日，葛晓鸣等 4 位自然人股东将各自持有的海润化工全部股权转让给烟台市国资委下属企业烟台市国有资产经营有限公司，烟台市国资委履行了相应的批复程序（烟国资【2015】47 号）。之后至今，海润化工的股权结构再未发生变更。海润化工实际控制人的变化：海润化工设立时，股权结构相对分散，无实际控制人，后海润化工的股东将股权转让给烟台海升并旋即转让给烟台有色，烟台有色的出资人为烟台市国资委，因此此时实际控制人为烟台市国资委；但考虑到该交易被法院判决无效，因此从 2011 年至 2015 年 6 月之间，公司的股权结构与设立时相同，无实际控制人；2015 年 6 月烟台市国有资产经营有限公司受让海润化工全部股权，成为海润化工的控股股东，由于烟台市国有资产经营有限公司的最终出资人为烟台市国资委，故实际控制人为烟台市国资委。
        '''
        
sents = sentence_splitter(str12)  #分句   
for i in sents:

    if (u"转让给" in i) and (u"年" in i) and (u"月" in i) and (u"日" in i):
#        print(i)

        words = segmentor(i)
        print(words)
        postags = posttagger(words)
        print(postags)
#        ner(words,postags)
        print(ner(words,postags))
        
        

print(''.join(ntag_company1))
print(''.join(ntag_company2))
     