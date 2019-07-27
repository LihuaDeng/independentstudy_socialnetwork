#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
all_groups = pd.read_csv(r"C:\Users\lunad\Desktop\photo_5000-.csv", usecols = [0,1])

#Get Group_ID to store in a list
df = pd.DataFrame(all_groups)
group_id = df['nsid'].tolist()

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
        'method': 'flickr.groups.pools.getPhotos',
        'group_id': groupid,
        'per_page': '500',
        'page': page,
        'format': 'json',
        'nojsoncallback':'1'     
    }
    consumer = oauth2.Consumer(key='cc6e0093965331473ef6d9be604b5a96', secret='a758040164b10f62')
    token = oauth2.Token(key='72157709455713622-99a678a48136490f', secret='4a13c4e35c898f21')

    params['oauth_consumer_key'] = consumer.key
    params['oauth_token']= token.key


    req = oauth2.Request(method=method, url=url, parameters=params)
    signature_method = oauth2.SignatureMethod_HMAC_SHA1()
    req.sign_request(signature_method, consumer, token)
    return req


# In[ ]:


#Loop through pages and groups
import json as js
photo = []
pagenumber = range(*)        
for i in group_id:     
    print(i)                
    page_result = []       
    for j in pagenumber or []:
        request = build_request('https://www.flickr.com/services/rest', groupid = str(i), page = str(j))
        u = urllib.request.urlopen(request.to_url())
        u = js.loads(u.read())
        page_result.append(u)
    photo.append(page_result)      


# In[ ]:


#Group photo info by group id
dict_photo = {}
for i in range(len(group_id)):
    dict_photo['id_'+str(group_id[i])]= photo[i]


# In[ ]:


#Output JSON storing photo info
p_list = list(dict_photo.items())
for t in p_list:
    for u in range(len(p_list)):
        t = p_list[u]
        u_str = str(u+1)
        file_name = u_str+str(t[0])+ '.json'
        f = open(r"C:\Users\lunad\Desktop\photo_data\photo"+file_name,'w')
        js.dump(t,f)
        f.close()


# In[ ]:


#Extract photo id
from nested_lookup import nested_lookup
dict_id ={}
for i in range(len(photo)):
    l_id = nested_lookup('id', photo[i])
    dict_t[str(group_id[i])] = l_id


# In[ ]:


#Output CSV storing photo id
import pandas as pd
df = pd.DataFrame({ key:pd.Series(value) for key, value in dict_t.items() })
df.to_csv(r"C:\Users\lunad\Desktop\photo_data\PhotoID.csv")

