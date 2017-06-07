#!/usr/bin/python

import os
import json

def loadConfig():
    try:
        configFile = open("/etc/mcfly.conf")
    except IOError:
        quit("Could not open config file, exiting.")
    else:
        try:
            config = json.load(configFile)
        except ValueError:
            quit("Config file does not contain valid json, exiting.")
        else:
            return config       

if __name__ == "__main__":
    config = loadConfig()
    for server in config["servers"]:
        print(server)
        for dir in config["servers"][server]:
            print("\t" + dir)
