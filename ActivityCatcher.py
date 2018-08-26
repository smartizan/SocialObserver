#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ActivityCatcher.py
#  
#  Выявляем активность пользователей в группах ВК
#  
#  

class ActivityCatcher:
    
    def __init__(self, gid, group_name):
        ''' Инициируем класс gid - идентификатор группы VK                 '''
        self.gid = str(gid)
        self.group_name = group_name
        self.opt = Options()
        session = vk.Session(access_token=self.opt.access_token)
        self.vk_api = vk.API(session, lang='ru')

def main(args):
    ac = ActivityCatcher(58533958, "Ника ТВ")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
