import os
import time
import requests
import json


def get_status():
    response = requests.request("GET", url)
    status_dict = json.loads(response.text)
    data_dict = status_dict['data']
    return data_dict


def print_progress_bar(percentage):
    percentage_value = float(percentage.strip('%'))
    filled_width = int(50 * percentage_value / 100)
    progress_bar = '#' * filled_width + '-' * (50 - filled_width)
    print(f'\r进度: |{progress_bar}| {percentage}', flush=True)


QQ = input("输入QQ：")
url = "http://api.tzick.club/Api?QQ=" + QQ
os.system("title QQ: " + QQ)

while True:
    status = get_status()
    os.system('cls')

    leftList = status['Left'].split('|')
    print_progress_bar(leftList[2])
    print(f"\r共有: {leftList[1]} 已测: {leftList[0].split(':')[1]}", flush=True)

    speedList = status['Estimated_hourly'].split('|')
    print(f"\r每小时测卡： {speedList[0]} 每分钟: {speedList[1]}", flush=True)

    print(f"\r已经测了: {status['Checkertime']}", flush=True)
    print(f"\r出了Hit: {status['Microsoft_Hit']} 张 有 {status['Microsoft_Ban_Hit']} 张是banHit", flush=True)
    print(f"\rMC有: {status['Minecraft']} 张")
    print(f"\rHypixelUnban有 {status['Minecraft_Unban']} 张 有 {status['Minecraft_Banned']} 张是Banned", flush=True)
    print(f"\r21+的卡有 {status['Minecraft_Hypixel_Level_21']} 张 Rank有 {status['Minecraft_Hypixel_Rank']} 张", flush=True)

    time.sleep(1)
