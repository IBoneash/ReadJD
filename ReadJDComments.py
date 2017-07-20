import urllib2
import re

url = 'http://list.jd.com/list.html?cat=737,752,753&page=1&delivery=1&sort=sort_totalsales15_desc&trans=1&JL=4_10_0#J_main'
content = urllib2.urlopen(url).read()
# print content

a = re.compile(r'href="//item.jd.com/(\d+).html\?dist=jd">')
result = re.findall(a, content)

b = ['ID', 'Good', 'Rate', 'Medium', 'Rate', 'Bad', 'rate']
d = re.compile(
    r'"ProductId":(\d+),.*"GoodCount":(\d+),.*"GoodRate":([0,1].\d*),.*"GeneralCount":(\d+),"GeneralRate":([0,1].\d*),.*"PoorCount":(\d+),"PoorRate":([0,1].\d*),')

result3 = []
try:
    for i in result:
        url2 = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds=' + i + '&callback=jQuery6071575&_=1500133816658'
        html = urllib2.urlopen(url2).read()
        result2 = re.findall(d, html)
        # print zip(b, list(result2[0]))
        if result2[0][2] >= '0.976' and int(result2[0][1]) > 15000:
            result3.append(result2[0])
    print len(result)
    for y in result3:
        print y
except Exception, e:
    print e
