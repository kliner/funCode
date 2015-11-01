import os, time

a = [
'adb shell sendevent /dev/input/event2 0003 0057 00008174',
'adb shell sendevent /dev/input/event2 0003 0053 00000547', # x pos
'adb shell sendevent /dev/input/event2 0003 0054 00001327', # y pos
'adb shell sendevent /dev/input/event2 0003 0058 00000054',
'adb shell sendevent /dev/input/event2 0003 0050 00000004',
'adb shell sendevent /dev/input/event2 0003 0051 00000004',
'adb shell sendevent /dev/input/event2 0003 0057 00000000',
'adb shell sendevent /dev/input/event2 0000 0000 00000000',
'adb shell sendevent /dev/input/event2 0003 0057 4294967295',
'adb shell sendevent /dev/input/event2 0000 0000 00000000',
]

def touchAgain():
    for ex in a:
        os.system(ex)

if __name__ == '__main__':
    for i in range(100000):
        touchAgain()
        time.sleep(0.2)
        print i

