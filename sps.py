import os,nmap
print('welcome to Semple Port Scanner [SPS] - by BDX-s')
def main():
	print('[!]put (1) for your ifconfig')
	print('[!]put (2) for ip descover')
	print('[!]put (3) for exploit ip')
	print('[!]put (exit) for exit')
	ans = input('Enter The value => ')
	if ans == '1' :
		print(os.system('clear'))
		print(os.system('ifconfig'))
		main()
	if ans == '2' :
		print(os.system('netdiscover'))
		main()
	if ans == '3' :
		target_ip = input('put the target ip => ')
		ns = nmap.PortScanner()
		ns.scan(target_ip,'1-1024','-v')
		print(ns.scaninfo())
		print(ns.csv())
		clear = input('do you want to continue ... [y/n] : ')
		if clear == 'y' :
			print(os.system('clear'))
			main()
		if clear == 'n' :
			exit()
		main()
	if ans == 'exit' :
		exit()
main()
		
