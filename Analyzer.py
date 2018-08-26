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
    CREATE TABLE nika_prev AS SELECT users_groups.gid, groups.group_name, users_groups.uid, users_groups.date FROM users_groups JOIN groups ON users_groups.gid=groups.gid WHERE groups.gid=58533958 AND users_groups.date='2018-08-25'

    Получить появившихся пользователей
    SELECT * FROM nika_now LEFT JOIN nika_prev ON nika_prev.uid = nika_now.uid WHERE nika_prev.uid IS NULL
    
    А это получиьт ушедших (???)
    SELECT * FROM nika_prev LEFT JOIN nika_now ON nika_now.uid = nika_prev.uid WHERE nika_now.uid IS NULL
    
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
