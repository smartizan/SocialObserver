#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2018 Asus <Asus@DESKTOP-KC1HO4L>
#  
#  Эта программа предназначена для сбора и анализа состава участников групп VK
#  
#  

import vk
from Options import Options
from DBC import DBC
import time

class UserExtractop():
        ''' Класс собирает пользователей из группы '''

        def __init__(self, gid, group_name):
                ''' Инициируем класс gid - идентификатор группы VK                 '''
                self.gid = str(gid)
                self.group_name = group_name
                self.opt = Options()
                session = vk.Session(access_token=self.opt.access_token)
                self.vk_api = vk.API(session, lang='ru')
                self.dbc = DBC()
                
        def __showUsers(self, users):
                ''' Отобразить пользователей '''
                for user in users:
                        # ~ print(user)
                        if user["sex"] == 1:
                                sex = "женский"
                        else:
                                sex = "мужской"
                        print(user["id"], user["first_name"], user["last_name"])
                        city = ""
                        if "city" in user:
                                city = user["city"]["title"]
                        country = ""
                        if "country" in user:
                                country = user["country"]["title"]
                        bdate = ""
                        if "bdate" in user:
                                bdate = user["bdate"]
                        print("\t", sex, country, city, bdate)
                        print("\n")
                        
                
        def getUsers(self):
                """ Получить всех пользователей, gid - id группы """
                print("Group", self.gid)
                self.dbc.saveGroup(self.gid, self.group_name)
                allUsers = []
                try:
                        of = 0
                        while True:
                                time.sleep(3)
                                res = self.vk_api.groups.getMembers(group_id=self.gid, offset=of, count=1000, v=5.80, fields=['sex', 'bdate', 'city', 'country', 'lists', 'contacts', 'education', 'universities', 'schools', 'status', 'common_count', 'relation', 'relatives', 'counters'])
                                users = res['users']
                                # ~ print(users)
                                self.__showUsers(users)
                                c = res['count']
                                if(len(users) == 0):
                                        break
                                else:
                                        self.saveUsers(users)
                                        allUsers += users
                                        of += 1000
                except vk.exceptions.VkAPIError:
                        #pass
                        t, v, tr = sys.exc_info()
                        print("Туре: ", t)
                        print("Value:", v)
                        print("Trace:", tr)
                finally:
                        pass
                print ("Найдено пользователей", len(allUsers))
                return allUsers
                
        def saveUsers(self, allUsers):
                ''' Сохранить данные о пользователе '''
                usersPacket = []
                linksPacket = []
                for user in allUsers:
                        userData = {}
                        userData["uid"] = user["id"]
                        if "first_name" in user:
                                userData["first_name"] = user["first_name"]
                        else:
                                userData["first_name"] = "Не указано"
                        if "last_name" in user:
                                userData["last_name"] = user["last_name"]
                        else:
                                userData["last_name"] = "Не указано"
                        if "sex" in user:
                                if user["sex"] == 1:
                                        userData["sex"] = "женский"
                                else:
                                        userData["sex"] = "мужской"
                        if "country" in user:
                                userData["country"] = user["country"]["title"]
                        else:
                                userData["country"] = "Не указано"
                        if "country" in user:
                                userData["country_title"] = user["country"]["title"]
                        else:
                                userData["country_title"] = "Не указано"
                        if "city" in user:
                                userData["city_title"] = user["city"]["title"]
                        else:
                                userData["city_title"] = "Не указано"
                        if "bdate" in user:
                                userData["bdate"] = user["bdate"]
                        else:
                                userData["bdate"] = "Не указано"
                        usersPacket.append(userData)
                        linksPacket.append([self.gid, user["id"]])
                self.dbc.saveUsers(usersPacket)
                self.dbc.saveUsersGroups(linksPacket)

def main(args):
        ue = UserExtractop(58533958, "Ника ТВ")
        allUsers = ue.getUsers()
        ue.saveUsers(allUsers)
        
        ue = UserExtractop(102468629, "Калужские новости")
        allUsers = ue.getUsers()
        ue.saveUsers(allUsers)
        
        ue = UserExtractop(145771240, "pressa40.ru")
        allUsers = ue.getUsers()
        ue.saveUsers(allUsers)
        
        ue = UserExtractop(48625596, "К24")
        allUsers = ue.getUsers()
        ue.saveUsers(allUsers)
        
        ue = UserExtractop(147830639, "МК в Калуге")
        allUsers = ue.getUsers()
        ue.saveUsers(allUsers)
        
        ue = UserExtractop(27736909, "Калуга-Поиск")
        allUsers = ue.getUsers()
        ue.saveUsers(allUsers)
        
        ue = UserExtractop(3212465, "Калужский перекресток")
        allUsers = ue.getUsers()
        ue.saveUsers(allUsers)
        return 0

if __name__ == '__main__':
        import sys
        sys.exit(main(sys.argv))
