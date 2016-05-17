import urllib2
import requests
import re
import csv
from bs4 import BeautifulSoup

myfile = open("myfile.csv",'wb')
spamwriter = csv.writer(open("myfile.csv",'wb'))

url = "file:///C:/Users/Admin/Desktop/p1.html"
i=0
regex = '<div class ="Email">(.+?)</div>'
pattern = re.compile(regex)
while i<len(url):

      htmlfile = urllib2.urlopen(url)
      htmltext = htmlfile.read()
      email = re.findall(pattern,htmltext)
      print email
      i+=1
      break
url = "file:///C:/Users/Admin/Desktop/p1.html"
i=0
regex = '<div class = "CompanyName">(.+?)</div>'
pattern = re.compile(regex)
while i<len(url):

      htmlfile = urllib2.urlopen(url)
      htmltext = htmlfile.read()
      comapanyname = re.findall(pattern,htmltext)
      print comapanyname
      i+=1
      break
url = "file:///C:/Users/Admin/Desktop/p1.html"
i=0
regex = '<div class = "accreditationNumber">(.+?)</div>'
pattern = re.compile(regex)
while i<len(url):

      htmlfile = urllib2.urlopen(url)
      htmltext = htmlfile.read()
      accreditationNumber = re.findall(pattern,htmltext)
      print accreditationNumber
      i+=1
      break
url = "file:///C:/Users/Admin/Desktop/p1.html"
i=0
regex = '<div class = "ContactAddress">(.+?)</div>'
pattern = re.compile(regex)
while i<len(url):

      htmlfile = urllib2.urlopen(url)
      htmltext = htmlfile.read()
      ContactAddress= re.findall(pattern,htmltext)
      try:
            spamwriter.writerow([ContactAddress])
            print ContactAddress
      except IndexError:
            spamwriter.writerow([ContactAddress])
            print ContactAddress
            i+=1
      break

myfile.close()