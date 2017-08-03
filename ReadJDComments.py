import urllib2
import re

url = ''
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
        try:
            html = urllib2.urlopen(url2).read()
            result2 = re.findall(d, html)
            # print zip(b, list(result2[0]))
            if result2[0][2] >= '0.95' and int(result2[0][1]) > 40000:
                result3.append(result2[0])
        except:
            continue
    print len(result)
    for y in result3:
        print zip(b, y)
except Exception, e:
    print e
