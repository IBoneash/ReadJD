import urllib2
import re
import time
import logging.handlers
import difflib

# Log File sort by time
tm = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
log_file = '%s.log' % tm

# Log File handler
handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5)
fmt = '%(message)s'
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

logger = logging.getLogger('Comments')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

url = 'https://list.jd.com/list.html?cat=652,654,5012&page=1&delivery=1&sort=sort_totalsales15_desc&trans=1&JL=4_10_0#J_main'
pre_content = urllib2.urlopen(url).read()
e = re.compile(r'<em>\D\D\D<b>(\d)</b>\D\D\D&')
page = re.findall(e, pre_content)
if page:
    page = int(page[0]) + 1
else:
    page = 2

for x in range(1, page):
    url2 = url.replace('&page=1', '&page=%d' % x, 1)
    try:
        content = urllib2.urlopen(url2).read()
        print "Loading Page %d   %s" % (x, url2)
        logger.info("Loading Page %d   %s" % (x, url2))
    except:
        pass

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
                if result2[0][2] >= '0.96' and int(result2[0][1]) > 500:
                    result3.append(result2[0])
            except:
                continue
        print len(result)
        for y in result3:
            print '%s https://item.jd.com/%s.html?dist=jd' % (zip(b[1:], y[1:]), y[0])
            # logger.info(zip(b, y))
            logger.info('%s https://item.jd.com/%s.html?dist=jd' % (zip(b[1:], y[1:]), y[0]))
    except Exception, e:
        print e
    logger.info('\n')