#!/usr/bin/python
#coding=utf-8
import socket
import struct
import random
import json
import thread
import time
import requests
import sys

reload(sys)  
sys.setdefaultencoding('utf-8')

HOST = 'livecmt-2.bilibili.com'
PORT = 788
BUFFER_SIZE = 1024

SEND_URL = 'http://live.bilibili.com/msg/send'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

f = open(r'cookie.txt','r')
cookies = {}
for line in f.read().split(';'):
    name, value = line.strip().split('=', 1)
    cookies[name] = value

def sendDanmuku(content):
    content = content.strip()
    if not content: return
    params = {
        "color":16777215,
        "fontsize":25,
        "mode":1,
        "msg":content,
        "rnd":int(time.time()),
        "roomid":90012
        }
    r = requests.post(SEND_URL, data=params, cookies=cookies)
    #print r.status_code, r.content

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
    # TODO multy packets
    data = struct.unpack('>IHHII', packet[:16])
    #print data
    action = data[3]
    if action == 3:
        pass
        #print 'online:' + str(struct.unpack('>i', packet[16:])[0])
    elif action == 5:
        try:
            raw = json.loads(packet[16:])
            if 'info' in raw:
                info = raw['info']
                print '%s send: %s' % (info[2][1].encode('utf-8'), info[1].encode('utf-8'))
            elif raw['cmd'] == 'SEND_GIFT':
                # TODO freq handle 
                data = raw['data']
                uname = data['uname'].encode('utf-8')
                num = data['num']
                giftName = data['giftName'].encode('utf-8')
                sendDanmuku('谢谢%s送的%d个%s' % (uname, num, giftName))
            else: 
                # TODO SYS_MSG
                print raw
        except Exception, e:
            print 'decode error!'
    else:
        print 'unknown' + packet[16:] + ',' + repr(packet[16:]) 

def recvThread():
    while 1:
        packet = s.recv(BUFFER_SIZE)
        if packet:
            parsePacket(packet)
        else:
            print 'empty'

if joinChannel(90012):
    thread.start_new_thread(heartBeatThread, ())
    thread.start_new_thread(recvThread, ())

    while 1:
        content = raw_input()
        sendDanmuku(content)
