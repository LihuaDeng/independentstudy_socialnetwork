#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Extract Group_ID from Group Info
import pandas as pd
all_groups = pd.read_csv(r"C:\Users\*\Desktop\All_Nature_Groups.csv", usecols = [0,1])

#Get Group_ID to store in a list
df = pd.DataFrame(all_groups)
group_id = df['nsid'].tolist

import oauth2
import time
import urllib.request
import pandas as pd

#Define function to call data through API
def build_request(url, method='GET', groupid = None, page = None):
    params = {                                            
        'oauth_version': "1.0",
        'oauth_nonce': oauth2.generate_nonce(),
        'oauth_timestamp': int(time.time()),
        'method': 'flickr.groups.members.getList',
        'group_id': groupid,
        'perpage': '500',
        'page': page,
        'format': 'json',
        'nojsoncallback':'1'     
    }
    consumer = oauth2.Consumer(key='cc6e0093965331473ef6d9be604b****', secret='a758040164b1****')
    token = oauth2.Token(key='72157709455713622-99a678a481364***', secret='4a13c4e35c898***')

    params['oauth_consumer_key'] = consumer.key
    params['oauth_token']= token.key


    req = oauth2.Request(method=method, url=url, parameters=params)
    signature_method = oauth2.SignatureMethod_HMAC_SHA1()
    req.sign_request(signature_method, consumer, token)
    return req


# In[ ]:


#Loop through Group_ID and Pages
import json as js
member = []
pagenumber = range(n)
for i in group_id:   
    print(i)               #To be aware of the progress 
    page_result = []       #Store info of all pages grouped by group_id
    for j in pagenumber or []:
        request = build_request('https://www.flickr.com/services/rest', groupid = str(i), page = str(j))
        u = urllib.request.urlopen(request.to_url())
        u = js.loads(u.read())
        page_result.append(u)
    member.append(u)       


# In[ ]:


#Combine Group_ID and Member info with dictionary
dict_member = {}
for i in range(len(groupid_list)):
    dict_member['id_'+str(i)]= member[i]


# In[ ]:


#Output as json files
list_ = list(dict_member.items())
for t in list_:
    for u in range(len(list_)):
        t = list_[u]
        u_str = str(u+1)
        file_name = u_str+str(t[0])+ '.json'
        f = open(r"C:\Users\lunad\Desktop\member_data\naturegroup"+file_name,'w')
        js.dump(t,f)
        f.close()


# In[ ]:


#Extract Member_ID to store in CSV for further data collection
import glob
import os
import json as js

#Load json files as list
file_list = glob.glob(os.path.join(os.getcwd(), "*.json"))
memberlist = []

for file_path in file_list:
    with open(file_path) as file_input:
        data = js.load(file_input)
        memberlist.append(data)


# In[ ]:


#Parse the list
ID_Dict = {}
for info in memberlist:
    memberinfo = info[1]
    Dict_1 = {}
    list_0 = []
    print(info[0])                                   #Be aware of the progress
    for i in range(len(memberinfo)):
        a = memberinfo[i]
        na = a["members"]['member']
        list_1.append(na)
        list_2 = []
        for sublist in list_2:
            for item in sublist:
                list_3.append(item)
                list_4 = []
                for j in list_3:
                    b = str(j['nsid'])
                    list_4.append(b)
                    ID_Dict[str(info[0])] = list_4


# In[ ]:


#Dataframe for storing the Member_ID grouped by Group_ID
import pandas as pd
df = pd.DataFrame({ key:pd.Series(value) for key, value in ID_Dict.items() })
#To CSV
df.to_csv(r"C:\Users\lunad\Desktop\member_data\MemberID.csv")

#### Same way to get Topics and Photos using GroupID
