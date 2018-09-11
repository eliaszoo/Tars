#!/usr/bin/python
# encoding: utf-8
import subprocess
import tarsLog
import os
from tarsUtil import *
log = tarsLog.getLogger()
def do():
    log.infoPrint("pullFramework start ...")
    pullFramework()
    log.infoPrint("pullFramework success")
    log.infoPrint("pullRapidjson start ...")
    pullRapidjson()
    log.infoPrint("pullRapidjson success")
    log.infoPrint("pullWeb start ...")
    pullRapidjson()
    log.infoPrint("pullWeb success")
    log.infoPrint("build start ...")
    build()
    log.infoPrint("build sucess")
    return

def pullFramework():
    baseDir = getBaseDir()
    if not os.path.exists("{}/TarsFramework/RegistryServer/".format(baseDir)):
        buildCmd("git clone https://github.com/TarsCloud/TarsFramework.git {}/TarsFramework ".format(baseDir))
    return

def pullWeb():
    baseDir = getBaseDir()
    if not os.path.exists("/usr/local/app/web".format(baseDir)):
        doCmd("git clone https://github.com/TarsCloud/TarsWeb.git /usr/local/app/web")
    return

def pullRapidjson():
    baseDir = getBaseDir()
    if not os.path.exists("{}/TarsFramework/thirdparty/rapidjson/bin".format(baseDir)):
        buildCmd("git clone https://github.com/Tencent/rapidjson.git {}/TarsFramework/thirdparty/rapidjson ".format(baseDir))
    return



def build():
    baseDir = getBaseDir()
    doCmd("{}/TarsFramework/build/build.sh cleanall".format(baseDir))
    rCode = buildCmd("{}/cpp/build/build.sh all".format(baseDir))
    if rCode == 0:
        log.info(" build success !!!")
    else:
        log.info(" build error !!!")
    return

def buildCmd(cmd):
    rCode=0
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        if line:
           log.infoPrint(line)
    if p.returncode == 0:
        rCode =0
    else:
        rCode=-1
    p.stdin.close()
    p.stdout.close()
    return rCode

if __name__ == '__main__':
    pass