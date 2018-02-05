import urllib2  
import codecs  
  
  
def ltp_cloud(par1):  
    url_get_base = "http://api.ltp-cloud.com/analysis/?"  
    api_key = 'b1U4M8w9a0sarywuFIXNGNqehuxWhNrteI6hdRZV'   # 用户注册语言云服务后获得的认证标识  
    format0 = 'plain'                                       # 结果格式，有xml、json、conll、plain（不可改成大写）  
    pattern = 'ws'                                          # 指定分析模式，有ws、pos、ner、dp、sdp、srl和all  
    result1 = urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s"  
                              % (url_get_base, api_key, par1, format0, pattern))  
    return result1.read().strip()  
  
f = open(r"test.txt", "r")                            # 待分析文本，已分句，每行一句。  
savef = codecs.open(u"out1.txt", "a", "utf-8")    # 结果存储  
  
linenum = 0  
newline = ""  
for line in f:  
    linenum += 1                                     # 记录处理行数  
    newline += line.strip().replace("#", "")         # 删除行末空白符、干扰符号，以免影响URI  
  
    if line[-1] != "\n":                             # 如果处理到文本最后一行  
        if " and " and " in " in newline:  
            print u"需要更改单词in"  
            newline = newline.replace(" in ", " i.n ")  
        print u"已处理到文本最后一行：", linenum  
        savef.write(ltp_cloud(newline).decode("utf-8") + "\n")  
  
    if len(newline) > 6000:                          # 让文本足够长时再提交处理，最大值在8000左右  
        if " and " and " in " in newline:            # 不能同时含有and和in两个词  
            print u"需要更改单词in"  
            newline = newline.replace(" in ", " i.n ")  
        print u"处理到第" + str(linenum) + u"行"  
        savef.write(ltp_cloud(newline).decode("utf-8") + "\n")  
        newline = ""  
  
savef.close()  
f.close()  