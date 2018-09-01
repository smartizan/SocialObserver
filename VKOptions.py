#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Options.py
#  
#  Copyright 2016 master <master@HP>
#  
#  
#  
#  

"""
https://oauth.vk.com/authorize?client_id=APP_ID&scope=offline,group,photos,wall,friends,messages,email,notifications&display=page&response_type=token&redirect_uri=https://oauth.vk.com/blank.html

https://oauth.vk.com/authorize?client_id=5484311&scope=offline,group,photos,wall,friends,messages,email,notifications&display=page&response_type=token&redirect_uri=https://oauth.vk.com/blank.html
https://oauth.vk.com/authorize?client_id=5484311&scope=offline,group,photos,wall,friends,messages,email,notifications&display=page&response_type=token&redirect_uri=https://oauth.vk.com/blank.html

24a2dba4c29ee73fd5bbe31c6526858690945107211b14f3766a524274aee87fc3d712e2c69be5327f4f0
"""

"""
+79264767260
LiquidMagne7
8f009f6236a58e7fdf6404ae36a6367e0ea67370edae49567978adf083d8a2e15e5eec164b4151110dd5a

********* 03 августа 2016 *********

+79299477863
LiquidMagne7
ec45616024975a881256205301fa3f75df4f2036fa46054504d29e52f627b42e55968d9f20ed2449b6da4

+79299643998
LiquidMagne7
53dd8c94cfb11aa05f5496676430626943db7c20bc8d54f8f718229d34c19cfaa2ac7665dd9588daf7cf2

+79811762526
LiquidMagne7
83d6f35bd0bfa8a214d400f3b2427ca1e0c7262750198fc5e6d390c7aa38f79a56a89134e52123b251ceb

+79299503786
LiquidMagne7
7abfa914767e497480f9c5154c59ef6a383a8fab6c45b20cca626be3f1c405640b63839e2823e9ca3e588

+79299888459
LiquidMagne7
06dd8f6ac4550a999af0b2020d376bd1a403ad4348c839d682a549c8e18dc91757a0a6bc4af402c069677


***********************************
"""

class VKOptions:
	
    def __init__(self):
        self.APP_ID = '5484311'
        self.USER_LOGIN = '+79105953106'
        self.USER_PASSWORD = 'LiquidMagne7'
        self.access_token = '7a7d44934e5e219618997d743ee6e0ad524095112ccf3635480121a1a1f63e4d036f1ce5b2e787c2662fc'
        self.sender_tokens = ['24a2dba4c29ee73fd5bbe31c6526858690945107211b14f3766a524274aee87fc3d712e2c69be5327f4f0', 'ec45616024975a881256205301fa3f75df4f2036fa46054504d29e52f627b42e55968d9f20ed2449b6da4', '53dd8c94cfb11aa05f5496676430626943db7c20bc8d54f8f718229d34c19cfaa2ac7665dd9588daf7cf2', '83d6f35bd0bfa8a214d400f3b2427ca1e0c7262750198fc5e6d390c7aa38f79a56a89134e52123b251ceb', '7abfa914767e497480f9c5154c59ef6a383a8fab6c45b20cca626be3f1c405640b63839e2823e9ca3e588', '06dd8f6ac4550a999af0b2020d376bd1a403ad4348c839d682a549c8e18dc91757a0a6bc4af402c069677']
        self.groups = []
        self.groups.append([58533958, "Ника ТВ"])
        self.groups.append([102468629, "Калужские новости"])
        self.groups.append([145771240, "pressa40.ru"])
        self.groups.append([48625596, "К24"])
        self.groups.append([147830639, "МК в Калуге"])
        self.groups.append([27736909, "Калуга-Поиск"])
        self.groups.append([3212465, "Калужский перекресток"])
        
if __name__ == '__main__':
    opt = Options()
    print(opt.APP_ID)
    print(opt.USER_LOGIN)
    print(opt.USER_PASSWORD)
    print(opt.access_token)
