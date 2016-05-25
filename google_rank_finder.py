### Website Scraper by Slava Rybalka on March 20th, 2015
### Python 3.4.2

### You feed a keyword and a domain to this script and it tells you if any page
### of the given domain is ranking on Google and at which position.


import urllib
import http.client
from urllib.parse import urlparse
import urllib.request
from urllib.error import URLError, HTTPError
import socket
from socket import timeout

import re
import time

clients_domain = input("Enter the domain starting with www or without it: ...")
keyword = input("Enter the keyword: ...")
simple_query = "https://www.google.com/search?num=100&ion=1&espv=&ie=UTF-8&q="
opener = urllib.request.FancyURLopener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
socket.setdefaulttimeout(10)

print('Checking if any page of '+ clients_domain + ' is ranking on Google...\n')

##########--------Request to Google ----------###################

try:
   se_req = opener.open(simple_query + keyword.replace(' ','%20'))
   results = se_req.read()
   with open('test.txt', mode='w', encoding='utf-8') as a_file:
     a_file.write(results.decode("UTF-8"))               
   #print(results)
   links = re.findall(b'bottom:2px"><cite>([^"]+)</cite>', results)
   for i in links[:10]:
     print(i)
except HTTPError as e:
   print('HTTP error:', e.code)
   pass
except URLError as e:
   print('We failed to reach a server:', e.reason)
   pass
except socket.timeout:
   print('socket timeout')
   pass
except http.client.BadStatusLine as e:
   print('HTTP error not recognized, error code not given')
   pass
except ValueError as e:
   print('Error:', e)
   pass

##########--- Finding the element in the list of retrieved Google Top 100 results ---########

for i in links:
   x = i.decode('UTF-8').replace('</b>', '').replace('<b>', '')
   #print(i)
   if clients_domain in x:
       #print(x)
       output = "Website page " + x + " is ranking at position " + str(int(links.index(i))+1) + ' for keyword ' + '"'+str(keyword)+'"'
       break

   else:
       output = "Website is not in Top 100 Google for keyword " + '"' + str(keyword) + '"'

print(output)



