#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Главный модуль, отсюда все запускается
#  

from VKUserExtractor import VKUserExtractor
from VKActivityCatcher import VKActivityCatcher


def main(args):
    vkue = VKUserExtractor()
    vkue.process()
    
    vkac = VKActivityCatcher()
    vkac.process()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
