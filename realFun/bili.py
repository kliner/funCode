#!/usr/bin/python
#coding=utf-8
import socket
import struct
import random
import json
import thread
import time
import sys
import threading
import bili_sender
import bili_improvisation_plugin

reload(sys)  
sys.setdefaultencoding('utf-8')

#roomid = input()
#if roomid not in [60000, 30040, 90012, 376637]: roomid = 90012
roomid = 90012

HOST = 'livecmt-2.bilibili.com'
PORT = 788
BUFFER_SIZE = 128 * 1024

IMPROVISATION = True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

cnt = 9

LOCK = threading.Lock()
gifts = []

date_format = '%H:%M:%S'

def makePacket(action, body):
    playload = body.encode('utf-8')
    packetLength = len(playload) + 16
    head = struct.pack('>IHHII', packetLength, 16, 1, action, 1)
    packet = head + playload
    #print packet
    return packet
    
def joinChannel(channelId):
    uid = int(1e14 + 2e14 * random.random())
    body = {'roomid':channelId, 'uid': uid}
    body = json.dumps(body, separators=(',',':'))
    s.send(makePacket(7, body))
    return 1

def heartBeatThread():
    while 1:
        s.send(makePacket(2, ''))
        time.sleep(30)

def parsePacket(packet):
    global cnt, gifts
    try:
        while packet:
            #print repr(packet)
            header = struct.unpack('>IHHII', packet[:16])
            packetLength = int(header[0])
            body = packet[16:packetLength]
            action = header[3]
            if action == 3:
                onlineNum = struct.unpack('>i', body)[0]
                cnt += 1
                if cnt >= 10: 
                    if IMPROVISATION: pass
                    else: print '在线灵魂数:' + str(onlineNum)
                    cnt = 0
            elif action == 5:
                raw = json.loads(body)
                tm = time.strftime(date_format, time.localtime(time.time()))
                if 'info' in raw:
                    info = raw['info']
                    if IMPROVISATION: 
                        bili_improvisation_plugin.parseDanmuku(info[1].encode('utf-8'))
                    else:
                        print '[%s] \033[91m%s\033[0m : \033[94m%s\033[0m' % (tm, info[2][1].encode('utf-8'), info[1].encode('utf-8'))
                elif raw['cmd'] == 'SEND_GIFT':
                    data = raw['data']
                    uname, num, giftName = data['uname'].encode('utf-8'), data['num'], data['giftName'].encode('utf-8')
                    LOCK.acquire()
                    gifts += [(uname, num, giftName)]
                    LOCK.release()
                elif raw['cmd'] == 'WELCOME': pass 
                elif raw['cmd'] == 'WELCOME_GUARD': pass 
                elif raw['cmd'] in ['SYS_GIFT', 'SYS_MSG']: pass
                else: print raw
            else:
                if not IMPROVISATION:
                    print 'unknown action,' + repr(packet) 
            if packetLength > len(packet):
                print 'packetLengthError!', packetLength, len(packet), repr(packet[:packetLength]), repr(packet[packetLength:])
                break
            packet = packet[packetLength:]

    except Exception, e:
        print 'decode error!', e

def giftResponseThread():
    global gifts
    while 1:
        LOCK.acquire()
        if gifts:
            uname, num, giftName = gifts[0]
            for t_uname, t_num, t_giftName in gifts[1:]:
                num = '好多'
                if t_uname != uname: uname = '大家'
                if t_giftName != giftName: giftName = '礼物'
            bili_sender.sendDanmuku(roomid, '谢谢%s送的%s个%s' % (uname, str(num), giftName))
            while gifts: gifts.pop()
        LOCK.release()
        time.sleep(2)

def recvThread():
    while 1:
        packet = s.recv(BUFFER_SIZE)
        if packet: parsePacket(packet)

if __name__ == '__main__':
    if joinChannel(roomid):
        thread.start_new_thread(heartBeatThread, ())
        thread.start_new_thread(recvThread, ())
        if roomid in [30040, 90012]: thread.start_new_thread(giftResponseThread, ())
    
        while 1:
            content = raw_input()
            if IMPROVISATION: 
                bili_improvisation_plugin.parseCommand(content)
            else:
                bili_sender.sendDanmuku(roomid, content)
