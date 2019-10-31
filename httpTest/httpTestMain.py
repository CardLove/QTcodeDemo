#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2019/11/23 23:57
# @Author : wang huixi
# @File   : update.py
import Queue
import atexit
import base64
import hashlib

import pickle
import socket
import sqlite3
import ssl
import stat
import struct
import threading
import time
import logging
import os
import uuid
import urllib2
from lxml import etree
import xml.etree.ElementTree as ET

# 组织结构信息查询
def query_unitinfo_request(ServerIp, ServerPort):
    content = None
    try:
        get_deptlist_xml = ''
        parser = etree.XMLParser(remove_blank_text=True)
        with open(os.getcwd() + '/getDeptList.xml') as obj:
            elem = etree.XML(obj.read(), parser=parser)
            get_deptlist_xml = '<?xml version="1.0" encoding="UTF-8"?>' + etree.tostring(elem, encoding="utf-8")

        post_data = get_deptlist_xml.format(id=str(uuid.uuid4()), gentime="2019-10-09 10:55:32.214", sendtime="2019-10-09 10:55:32.214")
        url = 'http://{}:{}/ClientServer/loginserver/rest/client/requestDepAndPer'.format( ServerIp, ServerPort)
        req = urllib2.Request(url, data=post_data, headers={'Content-Type': 'text/Plain'})
        try:
            sc_get_req = urllib2.urlopen(req)
            content = sc_get_req.read()
            logging.debug("服务器返回值： {}".format(content))
        except urllib2.HTTPError, e:
            logging.error(e)
        except urllib2.URLError, e:
            logging.error(e)
        except Exception, e:
            logging.error(e)
    except Exception as e:
        logging.error(e, exc_info=True)
    try:
        root = ET.XML(content)
        lists = root.findall("Body/Respond/DepList/")  #在当前指定目录下遍历
        department =[]
        for list in lists:
            department.append(list.find("DepName").text)
            logging.debug("获取部门： {}".format(department))
        return  department
    except Exception as e:
        logging.error(e, exc_info=True)



if __name__ == '__main__':
    lists = query_unitinfo_request("192.168.28.88","8089")
    for list in lists:
        print list