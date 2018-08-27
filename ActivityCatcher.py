#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ActivityCatcher.py
#  
#  Выявляем активность пользователей в группах ВК
#  
#  

import vk
from Options import Options
from DBC import DBC
import time

class ActivityCatcher:
    
    def __init__(self, gid, group_name):
        ''' Инициируем класс gid - идентификатор группы VK                 '''
        # ~ print(gid, group_name)
        self.gid = str(gid)
        self.group_name = group_name
        self.opt = Options()
        session = vk.Session(access_token=self.opt.access_token)
        self.vk_api = vk.API(session, lang='ru')
        self.dbc = DBC()
        
    def getPosts(self):
        ''' Получить посты. Пока будем брать 100 последних '''
        try:
            res = self.vk_api.wall.get(owner_id = '-'+ self.gid, offset=0, count=100, filter='owner', extended=0, v=5.80)
            # ~ print(res)
            items = res['items']
            for item in items:
                # ~ print(item['id'])
                print(self.gid, self.group_name, item['id'])
                if item['comments']['count'] > 0:
                    self.getCommenters(self.gid, item['id'])
                if item['likes']['count'] > 0:
                    self.getLikes(self.gid, item['id'], item['post_type'])
                time.sleep(3)
                print("\n")
        except vk.exceptions.VkAPIError:
            #pass
            t, v, tr = sys.exc_info()
            print("Туре: ", t)
            print("Value:", v)
            print("Trace:", tr)
        finally:
            pass
            
    def getLikes(self, gid, pid, ptype):
        try:
            res = self.vk_api.likes.getList(type=ptype, owner_id='-'+self.gid, item_id=pid, friends_only=0, extended=1, offset=0, count=1000,  v=5.80)
            items = res['items']
            print('Лайки')
            for item in items:
                print(item['id'], item['first_name'], item['last_name'])
                self.dbc.saveActivity(gid, pid, item['id'])
        except vk.exceptions.VkAPIError:
            #pass
            t, v, tr = sys.exc_info()
            print("Туре: ", t)
            print("Value:", v)
            print("Trace:", tr)
        finally:
            pass
            
    def getCommenters(self, gid, pid):
        ''' Получаем комментаторов '''
        try:
            res = self.vk_api.wall.getComments(owner_id='-'+self.gid, post_id=pid, need_likes=0, extended=1, offset=0, count=100,  v=5.80)
            print('Комментаторы')
            for profile in res['profiles']:
                print(profile['id'], profile['first_name'], profile['last_name'])
                self.dbc.saveActivity(gid, pid, profile['id'])
        except vk.exceptions.VkAPIError:
            #pass
            t, v, tr = sys.exc_info()
            print("Туре: ", t)
            print("Value:", v)
            print("Trace:", tr)
        finally:
            pass

def main(args):
    ac = ActivityCatcher(58533958, "Ника ТВ")
    ac.getPosts()
    ac = ActivityCatcher(102468629, "Калужские новости")
    ac.getPosts()
    ac = ActivityCatcher(145771240, "pressa40.ru")
    ac.getPosts()
    ac = ActivityCatcher(48625596, "К24")
    ac.getPosts()
    ac = ActivityCatcher(147830639, "МК в Калуге")
    ac.getPosts()
    ac = ActivityCatcher(27736909, "Калуга-Поиск")
    ac.getPosts()
    ac = ActivityCatcher(3212465, "Калужский перекресток")
    ac.getPosts()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
