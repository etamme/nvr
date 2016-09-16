#!/usr/bin/env python

import json, os, subprocess, datetime

with open('config.json') as config_file:    
    config = json.load(config_file)

options = config['options']
cameras = config['cameras']

basedir = options['basedir']
interval = options['interval']
runtime = options['runtime']
cwd = os.getcwd()
today=datetime.date.today()

print "config:\n"
print "base directory: "+ str(basedir)
print "file interval: "+ str(interval) + "\n"
print "total runtime: "+ str(runtime) + "\n"
print "cameras:\n"

for camera in cameras:
  print str(camera['name']) + ' ' + str(camera['url'])
  if not os.path.exists(basedir+camera['name']):
    os.makedirs(basedir+camera['name'])

  os.chdir(basedir+camera['name'])
  print "-v -c -B 10000000 -b 10000000 -4 -Q -f 30 -F \"" + str(today) + "\" -d " + str(runtime) + " -P " + str(interval) + " " + camera["url"]
  subprocess.Popen(["openRTSP", "-v -c -B 10000000 -b 10000000 -4 -Q -f 30 -F \"" + str(today) + "\" -d " + str(runtime) + " -P " + str(interval) + " " + camera["url"]])

os.chdir(cwd)

