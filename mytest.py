import urllib2
import re

url = 'https://list.jd.com/list.html?cat=9987,653,655&page=1&delivery=1&sort=sort_totalsales15_desc&trans=1&JL=4_10_0#J_main'
content = urllib2.urlopen(url).read()
# print content

a = re.compile(r'href="//item.jd.com/(\d+).html\?dist=jd">')
result = re.findall(a, content)

b = ['ID', 'Good', 'Rate', 'Medium', 'Rate', 'Bad', 'rate']
d = re.compile(
    r'"ProductId":(\d+),.*"GoodCount":(\d+),.*"GoodRate":([0,1].\d*),.*"GeneralCount":(\d+),"GeneralRate":([0,1].\d*),.*"PoorCount":(\d+),"PoorRate":([0,1].\d*),')


try:
    for i in result:
        url2 = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds=' + i + '&callback=jQuery6071575&_=1500133816658'
        html = urllib2.urlopen(url2).read()
        result2 = re.findall(d, html)
        print zip(b, list(result2[0]))
    print len(result)
except Exception, e:
    print e
