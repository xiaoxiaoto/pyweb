# -*- coding:utf-8 -*-

import urllib
import urllib.request
import re
import xlwt

def getData(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    request=urllib.request.Request(url=url, headers=header)
    response = urllib.request.urlopen(request)
    html = response.read().decode('UTF-8')
    return html

def filterData(data,regexp):
    regexpObj=re.compile(regexp,re.S)
    return regexpObj.findall(data)
def writeToExcl(fileName,sheetName,data):
    file = xlwt.Workbook()  # 注意这里的Workbook首字母是大写
    sheet=file.add_sheet(sheetName)  # 新建一个sheet
    if 'title' in data:
        title=data["title"]
        for i in range(len(title)):
            sheet.write(0,i,title[i])
    if 'data' in data:
        rows=data["data"]
        for i in range(len(rows)):
            row=rows[i]
            for j in range(len(row)):
                print(row[j])
                sheet.write(i+1, j, row[j])
    # file.save(fileName)  # 保存文件

url='http://edu.51cto.com/course/courseList/id-78.html'
data=getData(url)
regexp='<dl>.*?<dt.*?>.*?<a.*?href="(.*?)".*?title="(.*?)".*?>.*?</a>.*?</dt>.*?<dd>讲师:.*?<a.*?>(.*?)</a>.*?</dd>.*?</dl>'
title=["网址","课程名称","讲师姓名"]
res={"title":title}

filterData=filterData(data,regexp)
for item in filterData:
    row=[item[0].rstrip(),item[1].rstrip(),item[2].rstrip()]
    rows=[row]
    re = {"data": rows}
    res.update(re)
    writeToExcl("demo.xls", "sheet1", res)
