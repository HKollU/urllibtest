import urllib.request
theURL = 'https://www.youtube.com'
webUrl = urllib.request.urlopen(theURL)
print('Attempting to open' + theURL)
if webUrl.getcode() != 200:
        print('Opening' + theURL + 'Failed')
        quit()
data = webUrl.read()
print(data)
