#!/usr/bin/env python

import json, os
from pprint import pprint

with open('config.json') as config_file:    
    config = json.load(config_file)

options = config['options']
cameras = config['cameras']

basedir = options['basedir']
interval = int(options['interval'])

print "config:\n"
print "base directory: "+ str(basedir)
print "file interval: "+ str(interval) + "\n"
print "cameras:\n"
for camera in cameras:
  print str(camera['name']) + ' ' + str(camera['url'])
