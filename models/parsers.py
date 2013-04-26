#-*- coding: utf-8 -*-
import re
from models.const import MAPS
from models.players import Player
from models.log import log

def parseStatus(string):
    if "Use this command when connected to a server" in string:
        log("Can't parse status")
    elif "ShutdownGame" in string:
        PLAYERS = []
        mp = "no_info"
    elif string != None and "ping" in string:
        print(string)
        string = string.split('\n')
        mp = string[0][5:]
        log("%s : %s" % ("Map: ", mp))
        if mp in MAPS.keys():
            log("Valid map")
        string[1] = re.sub("^\s+|\n|\r|\x00| $", '', string[1])
        del(string[-1]);del(string[-1])
        PLAYERS   = []
        for line in string[3:]:
            line   = re.sub(' +', ',', line)
            array  = line.split(',')
            array  = array[1:]
            player = Player(*array)
            PLAYERS.append(player)
        from models.const import VARS
        VARS.players = PLAYERS
    else:
        PLAYERS = None; mp = None
    return PLAYERS, mp

def parseServerInfo(string):
    SERVERSTATUS = {}
    array = re.sub("^\s+|\r|\x00| $", '', string)
    array = re.sub(' +', ',', array)
    array = array.split('\n')
    del(array[-1])
    print(array)
    for line in array:
        lst = list(line.split(','))
        try:
            i = lst[-2]; j = lst[-1]
            SERVERSTATUS[i] = j
        except IndexError:
            try:
                i = lst[0][:-1]; j = lst[0][-1]
                SERVERSTATUS[i] = j
            except TypeError:
                pass
            except IndexError:
                SERVERSTATUS['g_gametype'] = "dm"
                print("GT ERROR")
    gametype = SERVERSTATUS['g_gametype']
    return gametype