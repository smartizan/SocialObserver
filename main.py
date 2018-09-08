#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Главный модуль, отсюда все запускается
#  

from VKUserExtractor import VKUserExtractor
from VKActivityCatcher import VKActivityCatcher
from VKAnalyzer import VKAnalyzer

def main(args):
    vkue = VKUserExtractor()
    vkue.process()

    vkac = VKActivityCatcher()
    vkac.process()

    vkanlz = VKAnalyzer()
    newUsers = vkanlz.getNewUsers()
    print(len(newUsers))
    
    lostUsers = vkanlz.getLostUsers()
    print(len(lostUsers))
    
    activeUsers = vkanlz.getMostActive()
    print(len(activeUsers))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
