import sys
sys.path.append(r'C:\programs\qualys\password')
from password import *

import requests
import re
import os

base_url = "https://qualysapi.qualys.eu/qps/rest/2.0/get/am/tag/"

tag_id = '12345678'     # level 2 tag. query up to 2 levels of chlid tags.

url1 = (base_url + tag_id)

# -- get request --
rget = requests.get(url1, auth=(un, pw))

html = rget.content.decode('utf-8') # convert html (a byte-like object) into a string
#print (html)

f = open('./temp/list.txt', 'w')                # write the list to a txt file.
f.write(html)


f = open('./temp/list.txt', 'r')

f1 = open('./temp/list1.txt', 'w')                # write the list to a txt file.

for line in f.readlines():
    if re.search('<id>', line, re.I):
        #print (line)
        f1.write(line)

f.close()
f1.close()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - 

f = open('./temp/list1.txt', 'r')

f2 = open('./temp/tag_list_l2.txt', 'w')

# -- strip html --
def html_tags(line):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', line)

#print (html_tags(line))


for line in f.readlines():
    res = html_tags(line)
    line1 = res.replace(' ', '')
    #print (line1)

    f2.write(line1)

f.close()
f2.close()
# = = = = = = = = = = = = = = = = = = = = = = = = = =

a_file = open("./temp/tag_list_l2.txt", "r")   # get list of lines
lines = a_file.readlines()
a_file.close()

del lines[0]

new_file = open("./temp/sample.txt", "w")

for line in lines:
    new_file.write(line)

new_file.close()


# = = = = = = = = = = = = = = = = = = = = = = = = = =

f = open('./temp/sample.txt', 'r')
f1 = f.readlines()
f.close()

f = open('./temp/list2.txt', 'a')                # write the list to a txt file.

for line in f1:
    tag_id = line.rstrip()
    url1 = (base_url + tag_id)
    print (url1)

    # -- get request --
    rget = requests.get(url1, auth=(un, pw))

    html = rget.content.decode('utf-8') # convert html (a byte-like object) into a string
    #print (html)
    f.write(html)


f = open('./temp/list2.txt', 'r')

f1 = open('./temp/list3.txt', 'w')                # write the list to a txt file.


for line in f.readlines():
    if re.search('<id>', line, re.I):
        #print (line)
        f1.write(line)

f.close()
f1.close()



f = open('./temp/list3.txt', 'r')

f2 = open('./temp/tag_list_l3.txt', 'w')

# -- strip html --
def html_tags(line):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', line)

#print (html_tags(line))


for line in f.readlines():
    res = html_tags(line)
    line1 = res.replace(' ', '')
    print (line1)

    f2.write(line1)

f.close()
f2.close()


# = = = = = = = = = = = = = = = = = = = = = = = = = =


f2 = open('final.txt', 'a')                # write the list to a txt file.

f = open('./temp/tag_list_l3.txt', 'r')
f1 = f.readlines()
f.close()

for line in f1:
    tag_id = line.rstrip()

    url1 = (base_url + tag_id)

    # -- get request --
    rget = requests.get(url1, auth=(un, pw))

    html = rget.content.decode('utf-8') # convert html (a byte-like object) into a string
    #print (html)

    f2.write(html)

f2.close()




"""
# -- strip html --
#def html_tags(html):
#    clean = re.compile('<.*?>')
#    return re.sub(clean, '', html)
#
#print (html_tags(html))
"""
