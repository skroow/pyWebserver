from pylgtv import WebOsClient

import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

try:
    webos_client = WebOsClient('192.168.1.81')
    # webos_client.send_button("HOME")
    webos_client.launch_app_with_content_id("pl.cda", 1134029801)
    webos_client.key

except:
    print("Error connecting to TV")


def pause():
    try:
        webos_client = WebOsClient('192.168.1.81')
        webos_client.pause()
    except:
        print("Error connecting to TV")


def getAllApps():
    try:
        temp = 0
        json_sss = {}
        webos_client = WebOsClient('192.168.1.81')
        for app in webos_client.get_apps():
            # new_data = {}
            # print(app)
            json_sss["app" + str(temp)] = app
            # print(json_sss)
            temp += 1
        print(json_sss)
        return json_sss
    except:
        print("Error connecting to TV")


def launch_app(appid):
    try:
        webos_client = WebOsClient('192.168.1.81')
        webos_client.launch_app(appid)
    except:
        print("Error connecting to TV")
