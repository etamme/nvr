#!/usr/bin/env python

import json, os, subprocess, datetime

with open('config.json') as config_file:    
    config = json.load(config_file)

options = config['options']
cameras = config['cameras']

openrtsp = str(options['openrtsp'])
basedir = str(options['basedir'])
interval = str(options['interval'])
runtime = str(options['runtime'])
cwd = os.getcwd()

today="\""+str(datetime.date.today())+"\""
print("config:\n")
print("openRTSP: "+ str(openrtsp))
print("base directory: "+ str(basedir))
print("file interval: "+ str(interval))
print("total runtime: "+ str(runtime) + "\n")
print("cameras:\n")

for camera in cameras:
  print(str(camera['name']) + ' ' + str(camera['url']))
  if not os.path.exists(basedir+camera['name']):
    os.makedirs(basedir+camera['name'])

  os.chdir(basedir+camera['name'])
  url=camera["url"]
  width=str(camera["width"])
  height=str(camera["height"])
  args=" -B 10000000 -b 10000000 -4 -f 30 -w "+width+" -h "+height+" -F "+today+" -d "+runtime+" -P "+interval+" "
  print(openrtsp+args+url)
  subprocess.Popen([openrtsp+args+url],shell=True)

os.chdir(cwd)

