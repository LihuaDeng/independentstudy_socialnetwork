#!/usr/bin/env python
# coding: utf-8

# In[63]:


#Extract page1_nature_groups
import urllib.request, json
url="https://www.flickr.com/services/rest/?method=flickr.groups.search&api_key=cc6e0093965331473ef6d9be604b5a96&text=nature&per_page=500&page=1&format=json&nojsoncallback=1"
response = urllib.request.urlopen(url)
page1_data = json.loads(response.read())
page1_parsed = (page1_data['groups']['group'])
#print (page1_parsed)

#Convert to csv
import csv
keys = page1_parsed[0].keys()
with open('page1test.csv', 'w', encoding = 'utf-8') as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(page1_parsed)


# In[71]:


#Extract page2_nature_groups
import urllib.request, json
url="https://www.flickr.com/services/rest/?method=flickr.groups.search&api_key=cc6e0093965331473ef6d9be604b5a96&text=nature&per_page=500&page=2&format=json&nojsoncallback=1"
response = urllib.request.urlopen(url)
page2_data = json.loads(response.read())
page2_parsed = (page1_data['groups']['group'])
print (page2_parsed)

#Convert to csv
import csv
keys = page2_parsed[0].keys()
with open('page2test.csv', 'w', encoding = 'utf-8') as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(page2_parsed)


# In[70]:


#Extract page3_nature_groups
import urllib.request, json
url="http://www.flickr.com/services/rest/?method=flickr.groups.search&api_key=cc6e0093965331473ef6d9be604b5a96&text=nature&per_page=500&page=3&format=json&nojsoncallback=1"
response = urllib.request.urlopen(url)
page3_data = json.loads(response.read())
page3_parsed = (page3_data['groups']['group'])
print (page3_parsed)

#Convert to csv
import csv
keys = page3_parsed[0].keys()
with open('page3test.csv', 'w', encoding = 'utf-8') as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(page3_parsed)


# In[73]:


#http://www.flickr.com/services/rest/?method=flickr.groups.search&api_key=cc6e0093965331473ef6d9be604b5a96&text=nature&per_page=500&page=4&format=json&nojsoncallback=1
#Extract page4_nature_groups
import urllib.request, json
url="http://www.flickr.com/services/rest/?method=flickr.groups.search&api_key=cc6e0093965331473ef6d9be604b5a96&text=nature&per_page=500&page=4&format=json&nojsoncallback=1"
response = urllib.request.urlopen(url)
page4_data = json.loads(response.read())
page4_parsed = (page4_data['groups']['group'])
#print (page4_parsed)

#Convert to csv
import csv
keys = page4_parsed[0].keys()
with open('page4test.csv', 'w', encoding = 'utf-8') as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(page4_parsed)


# In[75]:


#Extract page5_nature_groups
import urllib.request, json
url="https://www.flickr.com/services/rest/?method=flickr.groups.search&api_key=cc6e0093965331473ef6d9be604b5a96&text=nature&per_page=500&page=5&format=json&nojsoncallback=1"
response = urllib.request.urlopen(url)
page5_data = json.loads(response.read())
page5_parsed = (page5_data['groups']['group'])
#print (page5_parsed)

#Convert to csv
import csv
keys = page5_parsed[0].keys()
with open('page5test.csv', 'w', encoding = 'utf-8') as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(page5_parsed)


# In[77]:


#Extract page6_nature_groups
import urllib.request, json
url="https://www.flickr.com/services/rest/?method=flickr.groups.search&api_key=cc6e0093965331473ef6d9be604b5a96&text=nature&per_page=500&page=6&format=json&nojsoncallback=1"
response = urllib.request.urlopen(url)
page6_data = json.loads(response.read())
page6_parsed = (page6_data['groups']['group'])
#print (page6_parsed)

#Convert to csv
import csv
keys = page6_parsed[0].keys()
with open('page6test.csv', 'w', encoding = 'utf-8') as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(page6_parsed)


# In[79]:


#Extract page7_nature_groups
import urllib.request, json
url="https://www.flickr.com/services/rest/?method=flickr.groups.search&api_key=cc6e0093965331473ef6d9be604b5a96&text=nature&per_page=500&page=7&format=json&nojsoncallback=1"
response = urllib.request.urlopen(url)
page7_data = json.loads(response.read())
page7_parsed = (page7_data['groups']['group'])
#print (page7_parsed)

#Convert to csv
import csv
keys = page7_parsed[0].keys()
with open('page7test.csv', 'w', encoding = 'utf-8') as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(page7_parsed)


# In[81]:


#Extract page8_nature_groups
import urllib.request, json
url="https://www.flickr.com/services/rest/?method=flickr.groups.search&api_key=cc6e0093965331473ef6d9be604b5a96&text=nature&per_page=500&page=8&format=json&nojsoncallback=1"
response = urllib.request.urlopen(url)
page8_data = json.loads(response.read())
page8_parsed = (page8_data['groups']['group'])
#print (page8_parsed)

#Convert to csv
import csv
keys = page8_parsed[0].keys()
with open('page8test.csv', 'w', encoding = 'utf-8') as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(page8_parsed)


# In[83]:


#Extract page9_nature_groups
import urllib.request, json
url="https://www.flickr.com/services/rest/?method=flickr.groups.search&api_key=cc6e0093965331473ef6d9be604b5a96&text=nature&per_page=500&page=9&format=json&nojsoncallback=1"
response = urllib.request.urlopen(url)
page9_data = json.loads(response.read())
page9_parsed = (page9_data['groups']['group'])
#print (page9_parsed)

#Convert to csv
import csv
keys = page9_parsed[0].keys()
with open('page9test.csv', 'w', encoding = 'utf-8') as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(page9_parsed)


# In[ ]:




