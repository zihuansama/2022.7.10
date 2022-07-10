import urllib.request

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1657439637747_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'


headers ={
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1629789477003_137&jsoncallback=jsonp138&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': ' text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': ' gzip, deflate, br',
    'accept-language': ' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': ' ariaDefaultTheme=undefined; cna=hPJCGyaTDUsCAXWPcIKLY1/Z; _m_h5_tk=277b3c1d323213f79ba03efe016636b9_1656926836517; _m_h5_tk_enc=083389e096c2c29625ad1e27615dcef1; t=9739faa20b7f96cbae03101ee807228b; sgcookie=E1009SctYwJ4rRzGswkrtPiRj55uEMYKWfxHJNnLPyhjdZ69WREhnb%2F6dYi8xU%2Fn9vSgaJuSZSY8S2LZP2By1sBGJzProTS0eiCc0l6dFkFwZr0%3D; uc3=lg2=UIHiLt3xD8xYTw%3D%3D&nk2=F5RCZV0L1FMj0%2BqD&id2=UoH4HWrtOW9Bng%3D%3D&vt3=F8dCvCPWTg8fAWNdMmk%3D; lgc=tb7058432_22; uc4=nk4=0%40FY4Ji3A7DGGkm7KZwtWNE0BcehiPlB4%3D&id4=0%40UOnnGFiHcSujs1p2ySqDop81RJCC; tracknick=tb7058432_22; _cc_=V32FPkk%2Fhw%3D%3D; enc=zsfwaG6QCEQQEU5uU7LeX9slmISBu17U5ea%2Frg9t4s1o1QIWiLfhda5a0SY2vMFb1jPxTCAnbsx7Uk28XNFV1A%3D%3D; cookie2=104687855d0e90f0b1703719e215d342; v=0; _tb_token_=e581393e7e6bb; xlly_s=1; tfstk=cKUCBNYpGpvQTFONh41NYP7FiLgPZGRjNMM3OOHm_ath-AFCi1YqhdNbqL3rwf1..; l=eBOKCZjqLlE96kcWBO5Cnurza77T4Idb8sPzaNbMiInca6gltF98XNCH_WD9SdtjgtfFAetrJ6FVXdFBJM4p0giMW_N-1NKDJYp6-; isg=BGNjVXZCBYCkicnCgXQmtJHh8qcNWPeacFwKSZXBYkI51IL2HSg16ggCzqRa9E-S',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': ' " Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': ' ?0',
    'sec-ch-ua-platform': ' "Windows"',
    'sec-fetch-dest': ' empty',
    'sec-fetch-mode': ' cors',
    'sec-fetch-site': ' same-origin',
    'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
    'x-requested-with': ' XMLHttpRequest',
}

request =urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)