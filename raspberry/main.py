import os,time,sys
import threading,json,socket

def play_audio(name,c=1):
    order = 'aplay -D plughw:1,0,{1} /home/wav/{0}.wav'.format(name,c)
    os.system(order)

global c 
c=0
def play_bash(name):
    global c
    order = 'bash t1.sh {0} /home/wav/{1}.wav'.format(c,name)
    c= (c+1)%8
    os.system(order)

print('start')
play_bash('step_water2')
time.sleep(0.1)
play_bash('step_grass1')
print('end')

global e 
e = 0

def make_server():
    ip = '192.168.1.100'
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((ip,9998))
    print('Bind UDP on 9998 ',ip)
    while True:
        data,addr = s.recvfrom(1024)
        try:
            data = bytes.decode(data)
            if data == '0':
                global e
                e = 1
                print('Exiting...')
                break
            print(addr,data)
            obj=json.loads(data)
            play_bash(obj['name'])

        except Exception as err:
            print(repr(err))


t = threading.Thread(target=make_server,daemon=True)
t.start()


while True:
    global e
    if e == 1:
        break
    time.sleep(10)




    
