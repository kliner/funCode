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

reload(sys)  
sys.setdefaultencoding('utf-8')

HOST = 'livecmt-2.bilibili.com'
PORT = 788
BUFFER_SIZE = 1024

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
                print '在线灵魂数:' + str(onlineNum)
                cnt = 0
        elif action == 5:
            try:
                raw = json.loads(body)
                tm = time.strftime(date_format, time.localtime(time.time()))
                if 'info' in raw:
                    info = raw['info']
                    print '[%s] \033[91m%s\033[0m : \033[94m%s\033[0m' % (tm, info[2][1].encode('utf-8'), info[1].encode('utf-8'))
                elif raw['cmd'] == 'SEND_GIFT':
                    data = raw['data']
                    uname, num, giftName = data['uname'].encode('utf-8'), data['num'], data['giftName'].encode('utf-8')
                    LOCK.acquire()
                    gifts += [(uname, num, giftName)]
                    LOCK.release()
                elif raw['cmd'] in ['SYS_GIFT', 'SYS_MSG']: pass
                else: print raw
            except Exception, e:
                print 'decode error!', e
        else:
            print 'unknown action,' + repr(packet) 
        packet = packet[packetLength:]

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
            bili_sender.sendDanmuku('谢谢%s送的%d个%s' % (uname, num, giftName))
            while gifts: gifts.pop()
        LOCK.release()
        time.sleep(2)

def recvThread():
    while 1:
        packet = s.recv(BUFFER_SIZE)
        if packet: parsePacket(packet)

if __name__ == '__main__':
    if joinChannel(90012):
        thread.start_new_thread(heartBeatThread, ())
        thread.start_new_thread(recvThread, ())
        thread.start_new_thread(giftResponseThread, ())
    
        while 1:
            content = raw_input()
