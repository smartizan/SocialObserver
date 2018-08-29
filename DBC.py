#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  DBC.py
#  
#  Copyright 2018 Asus <Asus@DESKTOP-KC1HO4L>
#  
#  Работа с базой данных
#  
#  

import sqlite3
import os
import datetime

class DBC:
    
    def __init__(self):
        self.set_directory()
        self.db_puth = os.path.join(os.getcwd(), 'data', 'main.db')
        self.createTables()
        
    def set_directory(self):
        """ Установить директорию, в которую будет сохраняться база данных """
        self.directory = os.path.join(os.getcwd(), 'data')
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
            
    def createTables(self):
        conn = sqlite3.connect(self.db_puth)
        c = conn.cursor()
        sql = 'CREATE TABLE IF NOT EXISTS `groups` (`gid` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, `group_name` TEXT);'
        c.execute(sql)
        sql = 'CREATE TABLE IF NOT EXISTS `users` (`uid` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, `first_name` TEXT, `last_name` TEXT, `sex` TEXT, `country_title` TEXT, `city_title`	TEXT, `bdate`	TEXT);'
        c.execute(sql)
        sql = 'CREATE TABLE IF NOT EXISTS `users_groups` (`gid`	INTEGER NOT NULL, `uid`	INTEGER NOT NULL, `date` INTEGER, UNIQUE(gid, uid, date));'
        c.execute(sql)
        sql = 'CREATE TABLE IF NOT EXISTS `activity` (`gid`	INTEGER NOT NULL, `pid`	INTEGER NOT NULL, `uid`	INTEGER NOT NULL, UNIQUE(gid, pid, uid));'
        c.execute(sql)
        conn.commit()
        c.close()
        conn.close()
        
    def getNewUsers(self):
        ''' Получить новых пользователей '''
        now = datetime.datetime.now()
        now_date = now.strftime("%Y-%m-%d")
        prev = datetime.date.today()-datetime.timedelta(1)
        prev_date = prev.strftime("%Y-%m-%d")
        conn = sqlite3.connect(self.db_puth)
        c = conn.cursor()
        sql = 'DROP TABLE IF EXISTS users_prev;'
        c.execute(sql)
        sql = 'DROP TABLE IF EXISTS users_now;'
        c.execute(sql)
        sql = 'CREATE TABLE users_prev AS SELECT users_groups.gid, groups.group_name, users_groups.uid, users_groups.date FROM users_groups JOIN groups ON users_groups.gid=groups.gid WHERE users_groups.date=\'' + now_date + '\';'
        c.execute(sql)
        sql = 'CREATE TABLE users_now AS SELECT users_groups.gid, groups.group_name, users_groups.uid, users_groups.date FROM users_groups JOIN groups ON users_groups.gid=groups.gid WHERE users_groups.date=\'' + prev_date + '\';'
        c.execute(sql)
        conn.commit()
        # Новые пользователи
        sql='SELECT * FROM users_now LEFT JOIN users_prev ON users_prev.uid = users_now.uid  WHERE users_prev.uid IS NULL;'
        c.execute(sql)
        rows = c.fetchall()
        sql = 'DROP TABLE IF EXISTS users_prev;'
        c.execute(sql)
        sql = 'DROP TABLE IF EXISTS users_now;'
        c.execute(sql)
        conn.commit()
        c.close()
        conn.close()
        return rows
        
    def getLostUsers(self):
        ''' Получить потерянных пользователей '''
        now = datetime.datetime.now()
        now_date = now.strftime("%Y-%m-%d")
        prev = datetime.date.today()-datetime.timedelta(1)
        prev_date = prev.strftime("%Y-%m-%d")
        conn = sqlite3.connect(self.db_puth)
        c = conn.cursor()
        sql = 'DROP TABLE IF EXISTS users_prev;'
        c.execute(sql)
        sql = 'DROP TABLE IF EXISTS users_now;'
        c.execute(sql)
        sql = 'CREATE TABLE users_prev AS SELECT users_groups.gid, groups.group_name, users_groups.uid, users_groups.date FROM users_groups JOIN groups ON users_groups.gid=groups.gid WHERE users_groups.date=\'' + now_date + '\';'
        c.execute(sql)
        sql = 'CREATE TABLE users_now AS SELECT users_groups.gid, groups.group_name, users_groups.uid, users_groups.date FROM users_groups JOIN groups ON users_groups.gid=groups.gid WHERE users_groups.date=\'' + prev_date + '\';'
        c.execute(sql)
        conn.commit()
        # Новые пользователи
        sql='SELECT * FROM users_prev LEFT JOIN users_now ON users_now.uid = users_prev.uid WHERE users_now.uid IS NULL;'
        c.execute(sql)
        rows = c.fetchall()
        sql = 'DROP TABLE IF EXISTS users_prev;'
        c.execute(sql)
        sql = 'DROP TABLE IF EXISTS users_now;'
        c.execute(sql)
        conn.commit()
        c.close()
        conn.close()
        return rows
        
    def saveActivity(self, gid, pid, uid):
        ''' Сохранить реакцию пользователя '''
        conn = sqlite3.connect(self.db_puth)
        c = conn.cursor()
        res = c.execute('''INSERT OR IGNORE INTO activity (gid, pid, uid) VALUES(?,?,?)''', (gid, pid, uid))
        conn.commit()
        c.close()
        conn.close()
        
    def saveGroup(self, gid, group_name):
        ''' Сохранить id группы '''
        conn = sqlite3.connect(self.db_puth)
        c = conn.cursor()
        # ~ res = c.execute('''INSERT OR IGNORE INTO groups (gid) VALUES(?)''', gid)
        # ~ res = c.execute("INSERT OR IGNORE INTO groups (gid, group_name) VALUES(" + str(gid) + ", " + group_name + ")")
        res = c.execute('''INSERT OR IGNORE INTO groups (gid, group_name) VALUES(?,?)''', (gid, group_name))
        conn.commit()
        c.close()
        conn.close()
        # ~ pass
        
            
    def saveUsers(self, usersPacket):
        ''' Сохраняем пакет пользователей '''
        conn = sqlite3.connect(self.db_puth)
        c = conn.cursor()
        c.execute("begin")
        for userData in usersPacket:
            print(userData)
            uid = userData["uid"]
            first_name = userData["first_name"]
            last_name = userData["last_name"]
            sex = userData["sex"]
            country_title = userData["country_title"]
            city_title = userData["city_title"]
            bdate = userData["bdate"]
            res = c.execute('''INSERT OR IGNORE INTO users (uid, first_name, last_name, sex, country_title, city_title, bdate) VALUES(?,?,?,?,?,?,?)''', (uid, first_name, last_name, sex, country_title, city_title, bdate))
        c.execute("commit")
        c.close()
        conn.close()
            
        
    def saveUsersGroups(self, linksPacket):
        ''' Сохранить связку ГРУППА-ПОЛЬЗОВАТЕЛЬ '''
        now = datetime.datetime.now()
        now_date = now.strftime("%Y-%m-%d")
        conn = sqlite3.connect(self.db_puth)
        c = conn.cursor()
        c.execute("begin")
        for link in linksPacket:
            res = c.execute('''INSERT OR IGNORE INTO users_groups (gid, uid, date) VALUES(?,?,?)''', (link[0], link[1], now_date))
            print (link[0], link[1], now_date)
        c.execute("commit")
        c.close()
        conn.close()
            
        
    def getUser(self, uid):
        ''' Вернуть пользователя по ID '''
        user = {}
        conn = sqlite3.connect(self.db_puth)
        c = conn.cursor()
        sql = 'SELECT * FROM users WHERE `uid`= \'' + str(uid) + '\''
        c.execute(sql)
        row = c.fetchone()
        if not row is None:
            print(row[0])
            user["uid"] = int(row[0])
            user["first_name"] = row[1]
            user["last_name"] = row[2]
            user["sex"] = row[3]
            user["country_title"] = row[4]
            user["city_title"] = row[5]
            user["bdate"] = row[6]
        else:
            user = None
        # ~ conn.commit()
        c.close()
        conn.close()
        return user
        
def main(args):
    dbc = DBC()
    user = dbc.getUser(1)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
