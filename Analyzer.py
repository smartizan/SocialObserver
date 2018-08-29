#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Analyzer.py
#  
# Тут мЫ БУДЕМ АНАЛИЗИРОВАТЬ ВСЯКОЕ
#  
#  

'''

    Создать таблицу для группы и дня
    DROP TABLE IF EXISTS nika_prev;
    CREATE TABLE nika_prev AS SELECT users_groups.gid, groups.group_name, users_groups.uid, users_groups.date FROM users_groups JOIN groups ON users_groups.gid=groups.gid WHERE groups.gid=58533958 AND users_groups.date='2018-08-25';
	CREATE TABLE nika_now AS SELECT users_groups.gid, groups.group_name, users_groups.uid, users_groups.date FROM users_groups JOIN groups ON users_groups.gid=groups.gid WHERE groups.gid=58533958 AND users_groups.date='2018-08-27';
	
    Получить появившихся пользователей
    SELECT * FROM nika_now LEFT JOIN nika_prev ON nika_prev.uid = nika_now.uid WHERE nika_prev.uid IS NULL
    
    А это получиьт ушедших (???)
    SELECT * FROM nika_prev LEFT JOIN nika_now ON nika_now.uid = nika_prev.uid WHERE nika_now.uid IS NULL
    
    Без разбивки по группам
    DROP TABLE IF EXISTS users_prev;
	DROP TABLE IF EXISTS users_now;
	CREATE TABLE users_prev AS SELECT users_groups.gid, groups.group_name, users_groups.uid, users_groups.date FROM users_groups JOIN groups ON users_groups.gid=groups.gid WHERE users_groups.date='2018-08-27';
	CREATE TABLE users_now AS SELECT users_groups.gid, groups.group_name, users_groups.uid, users_groups.date FROM users_groups JOIN groups ON users_groups.gid=groups.gid WHERE users_groups.date='2018-08-28';
	--- Новые
	SELECT * FROM users_now LEFT JOIN users_prev ON users_prev.uid = users_now.uid  WHERE users_prev.uid IS NULL;
	--- Ушедшие
	SELECT * FROM users_prev LEFT JOIN users_now ON users_now.uid = users_prev.uid WHERE users_now.uid IS NULL;
    
    
    Самые активные пользователи
    SELECT COUNT(activity.pid) AS c, users.first_name, users.last_name  FROM activity JOIN users ON activity.uid=users.uid GROUP BY activity.uid ORDER BY c DESC;
    
    
    Что будет дальше?
    Отлавливать добавившихся и ушедших пользователей, заносить их в список для формирования рекламы в ВК. 
    Проверять целевую группу и тех, кто в нее вступил, удалять из списка для показа рекламы. 
    Следить в группах за темм, кто сколько лайкает и комментит, чтобы определить самых активных пользователей. 
'''


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
