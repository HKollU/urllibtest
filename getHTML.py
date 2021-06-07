import urllib.request
theURL = 'https://www.youtube.com'
webUrl = urllib.request.urlopen(theURL)
print('Attempting to open' + theURL)
if webUrl.getcode() != 200:
	print('Opening' + theURL + 'Failed')
	quit()
data = webUrl.read()
data=data.decode('utf-8')
print(data)
data = data.replace('10px','100px')

f = open('output.html','wt',encoding='utf-8')
f.write(data)
