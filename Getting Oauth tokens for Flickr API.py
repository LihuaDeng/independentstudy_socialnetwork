#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Get Request Token
import oauth2
import time
import urllib.request

def build_request(url, method='GET'):
    params = {                                            
        'oauth_version': "1.0",
        'oauth_nonce': oauth2.generate_nonce(),
        'oauth_timestamp': int(time.time())
    }
    consumer = oauth2.Consumer(key='cc6e0093965331473ef6d9be604b5a96', secret='a758040164b10f62')
    params['oauth_consumer_key'] = consumer.key

    req = oauth2.Request(method=method, url=url, parameters=params)
    signature_method = oauth2.SignatureMethod_HMAC_SHA1()
    req.sign_request(signature_method, consumer, None)
    return req


# In[8]:


#Call the request
request = build_request('https://www.flickr.com/services/oauth/request_token')
u = urllib.request.urlopen(request.to_url())
print (u.readlines())


# In[32]:


#Exchange to Access Token
import oauth2
import time
import urllib.request

def build_request(url, method='GET'):
    params = {                                            
        'oauth_version': "1.0",
        'oauth_nonce': oauth2.generate_nonce(),
        'oauth_timestamp': int(time.time()),
        'oauth_verifier':'1d0991fb241e5261'
    }
    consumer = oauth2.Consumer(key='cc6e0093965331473ef6d9be604b5a96', secret='a758040164b10f62')
    token = oauth2.Token(key='72157709454122801-ebec0c28c3ce5f76', secret='0cae333c490ad04e')

    params['oauth_consumer_key'] = consumer.key
    params['oauth_token']= token.key


    req = oauth2.Request(method=method, url=url, parameters=params)
    signature_method = oauth2.SignatureMethod_HMAC_SHA1()
    req.sign_request(signature_method, consumer, token)
    return req


# In[34]:


#Call the request
request = build_request('https://www.flickr.com/services/oauth/access_token')
u = urllib.request.urlopen(request.to_url())
print (u.readlines())


# In[ ]:




