import base64
import json

import requests

from settings import *

# MIB details - VM Superhub model is 'ARRIS TG2492LG-85 Router'
arris_router_mib = '1.3.6.1.4.1.4115.1.20.1'

# Set base url for requests
base_url = 'http://' + ROUTER_IP + '/'


def get_login_cookie():
    cred = USERNAME + ':' + PASSWORD
    encoded = base64.b64encode(cred.encode())
    login_arg = encoded.decode()
    url = base_url + 'login?arg={}&_n=12345'.format(login_arg)
    try:
        r = requests.get(url)
        if r.content:
            decoded_cookie = json.loads(base64.b64decode(r.content).decode())
            cookie = r.content.decode()
            print(json.dumps(decoded_cookie, indent=4, sort_keys=True))
            print('Logged in successfully!')
            return cookie
        else:
            print('Could not get cookie, incorrect credentials?')

    except requests.exceptions.RequestException as err:
        print(err)


def snmp_walk(oids):
    url = base_url + 'walk' + '?' + 'oids=' + oids + ';' + '&_n=12345'
    cookies = dict(credential=cookie)
    try:
        r = requests.get(url, cookies=cookies)
        print(r.text)
    except requests.exceptions.RequestException as err:
        print(err)


def snmp_get(oid):
    url = base_url + 'snmpGet' + '?' + 'oids=' + oid + ';' + '&_n=12345'
    cookies = dict(credential=cookie)
    try:
        r = requests.get(url, cookies=cookies)
        # print(r.text)
        print(json.dumps(r.json(), indent=4, sort_keys=True))
    except requests.exceptions.RequestException as err:
        print(err)


def get_wifi_details():
    ssid_oid = arris_router_mib + '.1.3.22.1.2.10001'
    password_oid = arris_router_mib + '.1.3.26.1.2.10001'
    snmp_get(ssid_oid)
    snmp_get(password_oid)
    # snmp_get('1.3.6.1.4.1.4115.1.20.1.1.3.26.1.2.10001')
    # snmp_walk(ssid_oid)
    # snmp_walk(password_oid)
    # snmp_get(ssid_oid)
    # snmp_get(password_oid)
    # walk('1.3.6.1.4.1.4115.1.20.1.1.6.7')
    # snmp_get('1.3.6.1.4.1.4115.1.20.1.1.3.42')
    # walk('1.3.6.1.4.1.4115.1.20.1.1.3.42')
    # snmp_walk(arris_router_mib)


cookie = get_login_cookie()

if cookie:
    # walk('1.3.6.1.4.1.4115.1.20.1')
    get_wifi_details()

decoded_cookie = None

print('done')
