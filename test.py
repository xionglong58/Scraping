import urllib2
def download(url):
    print "downloading",url
    try:
        html=urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print "Downloading error ",e.reason
        html=None
    return html
print(download("http://www.baidu.com"))
