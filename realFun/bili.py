#!/usr/bin/python
import socket
import struct
import random
import json
import thread
import time

HOST = 'livecmt-2.bilibili.com'
PORT = 788
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def makePacket(action, body):
    playload = body.encode('utf-8')
    packetLength = len(playload) + 16
    head = struct.pack('>IHHII', packetLength, 16, 1, action, 1)
    packet = head + playload
    print packet
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
    data = struct.unpack('>IHHII', packet[:16])
    print data
    action = data[3]
    if action == 3:
        print 'online:' + str(struct.unpack('>i', packet[16:])[0])
    elif action == 5:
        print 'recv msg:' + packet[16:]
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
        raw_input()
