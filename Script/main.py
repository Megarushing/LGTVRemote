#!/usr/bin/env python

__author__ = "Megarushing"
__credits__ = ["Megarushing", "ubaransel", "omz"]
__license__ = "GPL"
__version__ = "1.0"

import ui
import requests
import xml.etree.ElementTree as etree
import socket
import re

lgtv = {}
headers = {"Content-Type": "application/atom+xml"}

from objc_util import *
NSUserDefaults = ObjCClass('NSUserDefaults')

#grab pairing key
lgtv["pairingKey"] = str(NSUserDefaults.standardUserDefaults().stringForKey_("code"))
if lgtv["pairingKey"] == "None":
	lgtv["pairingKey"] = "TVCODE"

def send_custom_code(sender):
    dismiss()
    try:
        handleCommand(v["customCommand"].text)
    except Exception as e:
        v["messageLabel"].text = "Error: {}".format(e)

def send_code(sender):
    dismiss()
    try:
        handleCommand(str(sender.code))
    except Exception as e:
        v["messageLabel"].text = "Error: {}".format(e)

def textfield_action(sender):
    if sender.name == "codeField":
        code = sender.text
        lgtv["pairingKey"] = code
        NSUserDefaults.standardUserDefaults().setObject_forKey_(code,"code")
        start_session()

def getip():
    strngtoXmit =   'M-SEARCH * HTTP/1.1' + '\r\n' + \
    'HOST: 239.255.255.250:1900'  + '\r\n' + \
    'MAN: "ssdp:discover"'  + '\r\n' + \
    'MX: 2'  + '\r\n' + \
    'ST: urn:schemas-upnp-org:device:MediaRenderer:1'  + '\r\n' +  '\r\n'
    
    bytestoXmit = strngtoXmit.encode()
    sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    sock.settimeout(3)
    found = False
    gotstr = 'notyet'
    i = 0
    ipaddress = None
    sock.sendto( bytestoXmit,  ('239.255.255.250', 1900 ) )
    while not found and i <= 1 and gotstr == 'notyet':
        try:
            gotbytes, addressport = sock.recvfrom(512)
            gotstr = gotbytes.decode()
        except:
            i += 1
            sock.sendto( bytestoXmit, ( '239.255.255.250', 1900 ) )
        if re.search('LG', gotstr):
            ipaddress, _ = addressport
            found = True
        else:
            gotstr = 'notyet'
        i += 1
    sock.close()
    if not found :
        v["messageLabel"].text = "Lg TV not found!"
        return ""
    else:
        v["messageLabel"].text = ""
    return ipaddress


def displayKey():
    reqKey = "<?xml version=\"1.0\" encoding=\"utf-8\"?><auth><type>AuthKeyReq</type></auth>"
    req = requests.request("POST", "http://"+lgtv["ipaddress"]+":8080/hdcp/api/auth", data=reqKey, headers=headers)
    if req.reason != "OK" :
        dialogMsg = "Network Error!"
        v["messageLabel"].text = dialogMsg
    return req.reason


def getSessionid():
    pairCmd = "<?xml version=\"1.0\" encoding=\"utf-8\"?><auth><type>AuthReq</type><value>" \
    + lgtv["pairingKey"] + "</value></auth>"
    req = requests.request("POST", "http://"+lgtv["ipaddress"]+":8080/hdcp/api/auth", data=pairCmd, headers=headers)
    if req.reason != "OK" :
        return ""
    tree = etree.XML(req.content)
    v["messageLabel"].text = ""
    return tree.find('session').text


def getPairingKey():
    displayKey()
    dialogMsg = "Please enter the pairing key\nyou see on your TV screen\n"
    v["messageLabel"].text = dialogMsg

def handleCommand(cmdcode):
    if lgtv["ipaddress"] == "" or lgtv["session"] == "":
        start_session()
    if lgtv["ipaddress"] == "" or lgtv["session"] == "":
        return False
    
    cmdText = "<?xml version=\"1.0\" encoding=\"utf-8\"?><command><session>" \
    + lgtv["session"]  \
    + "</session><type>HandleKeyInput</type><value>" \
    + str(cmdcode) \
    + "</value></command>"
    req = requests.request("POST", "http://"+lgtv["ipaddress"]+":8080/hdcp/api/dtv_wifirc", data=cmdText, headers=headers)
    return req.reason

def start_session():
    lgtv["session"] = ""
    lgtv["ipaddress"] = ""
    lgtv["ipaddress"] = getip()
    if lgtv["ipaddress"] == "":
        return False
    try:
        lgtv["session"] = getSessionid()
    except Exception as e:
        v["messageLabel"].text = "TV connection error"
        return False
    if lgtv["session"] == "" :
        getPairingKey()

def dismiss():
    v["codeField"].end_editing()
    v["customCommand"].end_editing()

#ui configs
v = ui.load_view('lgtv')
v.present(style='sheet',animated=False,orientations=('portrait'),hide_title_bar=True,title_bar_color='black',title_color='white')
v["backgroundImage"].image = ui.Image.named("bg.png")
v["codeField"].action = textfield_action
v["codeField"].text = lgtv["pairingKey"]
v["codeField"].autocapitalization_type = ui.AUTOCAPITALIZE_ALL
v["customCommand"].keyboard_type = ui.KEYBOARD_NUMBER_PAD

start_session()
