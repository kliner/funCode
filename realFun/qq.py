#coding=utf-8
import sys
import tornado.ioloop
import tornado.web
import json
import time
import requests
import urllib
import thread
import random

reload(sys)  
sys.setdefaultencoding('utf8')

#DEBUG = True 
DEBUG = not True

cities = set()
with open('city.json') as f:
    cities = json.loads(f.read().decode('string_escape'))
    cities = [c.encode('utf-8') for c in cities]
cities = set(cities) | set(['北京','上海','重庆','天津','香港'])

lastContent = ''

u_sera = 3373579732
u_me = 2414479098

cache = {}
expire_threshold = 30

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class QQHandler(tornado.web.RequestHandler):
    keyWords = ['早安','早上好','午安','中午好','下午好','晚上好','晚安','摸摸','么么','挥挥','灰灰','mua','muah','拜拜','哦哈哟','哦呀斯密','蠢','帅','帥','除夕快乐','新年快乐','新年好','春节快乐']
    kaomoji = ['(｡･ω･)','(・∀・)','(′▽`〃)','( ^ω^)','(≧ω≦)','( ´ ▽ ` )b','(´・ω・｀)','( ⸝⸝•ᴗ•⸝⸝ )੭⁾⁾','(„ᵕᴗᵕ„)','(灬╹ω╹灬)',''] # '(◕‿◕✿)'
    nicknameDct = {3373579732:'Seraaa大哥大', 349646651:'酸奶白', 326754125:'青青', 2214201227:'阿娇小哥哥', 876865661:'笑笑姐'}

    def post(self):
        raw_data = self.request.body
        if DEBUG: print raw_data
        data = json.loads(raw_data)
        date_format = '%H:%M:%S'
        group_msg_format = '[%s] %s : %s'
        chat_msg_format = '[%s] \033[91m%s\033[0m : \033[94m%s\033[0m'
        tm = ''
        if 'time' in data: tm = time.strftime(date_format, time.localtime(data['time']))

        if 'sender_uid' not in data: data['sender_uid'] = 19 # just some magic number
        if data['sender_uid'] == 3373579732: data['sender'] = '♥︎'

        if 'event' in data and data['event'] == 'new_group_member':
            groupid = data['params'][1]['uid']
            nickname = data['params'][0]['name']
            if groupid in [592749174, 228767011]:
                replyWord = '欢迎' + nickname
                print 'Auto Reply: ' + replyWord
                requests.post('http://127.0.0.1:5000/openqq/send_group_message?uid=%s&content=%s' % (groupid, replyWord))
                replyWord = '@%s 麻煩你在群名片填上b站名字喔( ´▽` )ﾉ' % nickname
                print 'Auto Reply: ' + replyWord
                requests.post('http://127.0.0.1:5000/openqq/send_group_message?uid=%s&content=%s' % (groupid, replyWord))


        if 'group_uid' in data and data['group_uid'] in [592749174, 228767011]: # my test group, qiaobai group
            #print '\033[91m%s\033[0m : \033[94m%s\033[0m' % (raw_data, data['content'])
            print group_msg_format % (tm, data['sender'], data['content'])
            global lastContent 
            if DEBUG: print lastContent
            if data['sender_uid'] in self.nicknameDct: data['sender'] = self.nicknameDct[data['sender_uid']] 
            if data['content']: data['content'] = data['content'].strip()
            if data['sender_uid'] == u_me: return
            replyWord = ''
            if lastContent and lastContent == data['content']:
                replyWord = lastContent
                lastContent = ''
            elif 'kli' in data['content'] and any(x in data['content'] for x in ['机器', '程序']): replyWord = random.choice(['？？？？', '你说啥？', '你再说一遍？'])
            elif data['content'] == 'kli早安' and data['sender_uid'] == u_sera: replyWord = data['sender'] + '早，kli一晚上都在想你喔，親親臉龐muah~ 你是我噠啦' + random.choice(self.kaomoji)
            elif data['content'] == 'kli午安' and data['sender_uid'] == u_sera: replyWord = '你吵到我睡午覺了，%s壞' % (data['sender']) + random.choice(self.kaomoji)
            elif data['content'] == 'kli晚安' and data['sender_uid'] == u_sera: replyWord = 'kli拉%s手手拖去床上，kli幫你脫鞋鞋，kli幫你捶捶，%s晚安，啵～' % (data['sender'], data['sender']) + random.choice(self.kaomoji)
            elif data['content'] == 'kli洗澡' and data['sender_uid'] == u_sera: replyWord = '好喔～%s幫我刷背背，kli轉身偷喝洗澡水，咳咳，嗆到了' % (data['sender']) + random.choice(self.kaomoji)
            elif data['content'] == 'boom' and data['sender_uid'] == 747303801: replyWord = '抓住' + random.choice(self.kaomoji)
            elif data['content'] == '|ω•`)': replyWord = '抓住' + random.choice(self.kaomoji)
            elif data['content'] in ['', '冒泡', '。']: replyWord = '戳' 
            elif data['content'] in ['噗']: replyWord = 'poi' 
            elif data['content'] in ['poi']: replyWord = 'nico' 
            elif data['content'] in ['nico']: replyWord = 'poi' 
            elif data['content'] in ['niconiconi']: replyWord = 'nicopoiduang' 
            elif data['content'] in ['QwQ', 'o.o']: replyWord = random.choice(self.kaomoji)
            elif data['content'] in ['QAQ']:
                #if data['sender_uid'] == 326754125: replyWord = random.choice(['打一生风向这个坏蜀黍', '向风老人家又欺负你了？', '摸摸' + data['sender'] +'，不哭不哭']) + random.choice(self.kaomoji)
                replyWord = '摸摸' + data['sender'] +'，不哭不哭' + random.choice(self.kaomoji)
            elif '人生啊' in data['content']:
                if data['sender_uid'] in [2332268138]: replyWord = random.choice(['如一丝青烟','风拂过你的头发','随风前行'])
                else: replyWord = random.choice(['人生苦短，及时行乐','人生若只如初见'])
            elif '找cp' in data['content']:
                if data['sender_uid'] in [2318175241]: replyWord = random.choice(['老毒你不是有向风的哥哥了吗','老毒加油']) + random.choice(self.kaomoji)
                else: replyWord = '老毒还没有cp, 快去跟他凑一对' + random.choice(self.kaomoji)
            elif data['content'].lower() == 'kli':
                if data['sender_uid'] == 3422762834: replyWord = data['sender'] + '(◕‿◕✿)'
                elif data['sender_uid'] == 3373579732: replyWord = 'S大哥大！kli只要你，只屬於你，抱抱不分開，蹭蹭' + random.choice(self.kaomoji)
                else: replyWord = data['sender'] + random.choice(self.kaomoji)
            elif data['content'].lower() == 'klikli':
                replyWord = data['sender'] + random.choice(self.kaomoji)
            elif data['content'].lower() == 'kil':
                replyWord = data['sender'] + '是在说kli吗，kli叫kli'
            elif any([1 for k in self.keyWords if k in data['content']]) and any([1 for k in ['大家', 'kli', 'Kli'] if k in data['content']]):
                replyWord = data['sender'] + ''.join([k for k in self.keyWords if k in data['content']]) + random.choice(self.kaomoji)
            elif data['content'][:3].lower() == 'kli':
                query = data['content'][3:]
                #if data['sender_uid'] in [1141119208]:  replyWord = data['sender'] + '大坏蛋'
                #elif data['sender_uid'] in [2829162871]:  replyWord = '请%s注意弹幕礼仪哦！' % data['sender']
                if query in ['我爱你', '我愛你']: replyWord = 'kli也爱你' + random.choice(self.kaomoji)
                elif any(k in query for k in ['內衣','內褲','内裤','胖次','大哥', '大佬', '主人', '女仆']): replyWord = 'kli听不懂啦' + random.choice(self.kaomoji)
                elif query in ['在吗', '在不在', '在嗎']:  replyWord = '不在' + random.choice(self.kaomoji)
                elif query[0] in ['说', '說']:  
                    if data['sender_uid'] == 303412733: replyWord = query[1:] + random.choice(self.kaomoji)
                    else: replyWord = 'kli不说' + random.choice(self.kaomoji)
                else: replyWord = data['sender'] + query + random.choice(self.kaomoji)
            if data['content'][:11] == '@kliMusume ':
                query = data['content'][11:].strip()
                if data['sender_uid'] == 303412733:
                    if '乖' in query:
                        replyWord = '乖～' + random.choice(self.kaomoji)
                if '天气' in query:
                    global cities
                    city = [k for k in cities if k and k in query]
                    if DEBUG: print city
                    if city: replyWord = weather(city[0])
                    else: replyWord = "找不到的天气信息呢"
                        
                #else: replyWord = data['sender'] + query + random.choice(self.kaomoji)

            if data['content']: lastContent = data['content']
            if replyWord:
                if replyWord in cache and time.time() - cache[replyWord] < expire_threshold:
                    print 'Auto Reply too frequently, ' + replyWord 
                else:
                    cache[replyWord] = time.time()
                    print 'Auto Reply: ' + replyWord
                    requests.post('http://127.0.0.1:5000/openqq/send_group_message?uid=%d&content=%s' % (data['group_uid'], replyWord))
        if not 'group_uid' in data and data['sender_uid'] == 3373579732: # sera
            print chat_msg_format % (tm, data['sender'], data['content'])

SEND_TYPE = 1

def weather(city):
    url = "https://api.thinkpage.cn/v3/weather/daily.json?key=02do80qt1s51oejl&location=%s&language=zh-Hans&unit=c&start=0&days=2" % city
    respose = requests.get(url)
    data = respose.json()
    if 'status_code' in data: return '找不到%s的天气信息呢' % city 
    else: 
        today = data['results'][0]['daily'][0]
        tomorrow = data['results'][0]['daily'][1]
        result = '%s今天的天气是%s，%s～%s度；明天的天气是%s，%s～%s度。' % (city, today['text_day'], today['low'], today['high'], tomorrow['text_day'], tomorrow['low'], tomorrow['high'])
        if int(today['low']) < 10: result += '哇好冷啊～注意多穿衣服哦～'
        elif int(today['high']) > 30: result += '热死了～'
        else: result += '大概是个好天气呢？'
        return result

def input_thread():
    global SEND_TYPE
    if SEND_TYPE == 1: print 'To ♥︎: ',
    else: print 'To group: ',
    w = raw_input().strip()
    if len(w) == 0: return
    if DEBUG: print w
    if w[0] == '#':
        cmd = w[1:]
        if cmd == '1': SEND_TYPE = 1
        elif cmd == '0': SEND_TYPE = 0
    else:
        txt = urllib.quote_plus(w)
        if SEND_TYPE == 1: requests.post('http://127.0.0.1:5000/openqq/send_friend_message?uid=3373579732&content=%s' % txt)
        elif SEND_TYPE == 0: requests.post('http://127.0.0.1:5000/openqq/send_group_message?uid=228767011&content=%s' % txt)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/api", QQHandler),
    ])

def web_thread():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    thread.start_new_thread(web_thread, ())
    while 1:
        input_thread()
