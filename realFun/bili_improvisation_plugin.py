#coding=utf-8
import sys
import json

reload(sys)  
sys.setdefaultencoding('utf8')

block_lst = ['圆舞曲', '肖邦', '钟']
to_play_lst = []
pending_lst = []
completed = {}

def loadConfig():
    print '初始化...'
    global block_lst, to_play_lst, pending_lst
    with open('config.json') as f:
        block_lst += [s.encode('utf8') for s in json.loads(f.readline())]
        to_play_lst += [s.encode('utf8') for s in json.loads(f.readline())]
        pending_lst += [s.encode('utf8') for s in json.loads(f.readline())]
    print '初始化完成'

loadConfig()

def saveConfig():
    global block_lst, to_play_lst, pending_lst
    with open('config.json', 'w') as f:
        block_lst = list(set(block_lst))
        f.write(json.dumps(block_lst) + '\n')
        f.write(json.dumps(to_play_lst) + '\n')
        f.write(json.dumps(pending_lst) + '\n')

def clear():
    print("\033c")

def output_help():
    print('操作指南: f-收藏,b-屏蔽,c-已弹奏,d-删除,s-显示详细列表,q-退出,')

def output_all():
    clear()
    print '当前待演奏列表：'
    for i, s in enumerate(to_play_lst):
        print '%d.\t%s' % (i+1, s)
    print '--------------------------------'
    print '当前收藏列表：'
    for i, s in enumerate(pending_lst):
        print '%d.\t%s' % (i+1, s)
    print '--------------------------------'
    print '已弹奏列表：'
    for k in completed.keys():
        print k, '\t', completed[k], '次'
    print '--------------------------------'
    output_help()

output_all()

def output():
    clear()
    print '当前待演奏列表：'
    for i, s in enumerate(to_play_lst):
        print '%d.\t%s' % (i+1, s)

def parseDanmuku(s):
    global block_lst, to_play_lst, pending_lst
    s = s.strip()
    #print 'recv danmuku', s
    if s[:6] == '点歌': content = s[6:].strip()
    else: return
    if any([1 for keyword in block_lst if keyword in content]): return
    if content in pending_lst or content in to_play_lst: return
    to_play_lst += [content]
    output()

def parseCommand(s):
    global block_lst, to_play_lst, pending_lst
    s = s.strip()
    idx = s[1:]
    if not idx: idx = 0
    else: idx = int(idx) - 1

    if s == 's': 
        pass
    elif s[0] == 'd': 
        if idx < len(to_play_lst): 
            to_play_lst.pop(idx)
    elif s[0] == 'b': 
        if idx < len(to_play_lst): 
            content = to_play_lst[idx] 
            block_lst += [content]
            to_play_lst.pop(idx)
    elif s[0] == 'f':
        if idx < len(to_play_lst): 
            content = to_play_lst[idx] 
            pending_lst += [content]
            to_play_lst.pop(idx)
    elif s[0] == 'c':
        if idx < len(to_play_lst): 
            content = to_play_lst[idx] 
            completed[content] = completed.get(content, 0) + 1
            to_play_lst.pop(idx)
    elif s[0] == 'q':
        saveConfig()
        output_all()
        sys.exit(0)
    output_all()

if __name__ == '__main__':
    output_help()
    while 1:
        s = raw_input()
        if s == '': parseCommand('c')
        elif s[0] in 'sbfcq': parseCommand(s)
        else: parseDanmuku(s)
        
