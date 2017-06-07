#!/usr/bin/python

import argparse
import os
import json
from subprocess import call

def loadConfig(location="/etc/mcfly.conf"):
    try:
        configFile = open(location)
    except IOError:
        quit("Could not open config file, exiting.")
    else:
        try:
            config = json.load(configFile)
        except ValueError:
            quit("Config file does not contain valid json, exiting.")
        else:
            return config       

parser = argparse.ArgumentParser(description='mcfly is a simple backup tool that copies folders located on remote servers to a locally defined backup folder.')
parser.add_argument("-i", "--init", help="Creates a basic config file, !!WARNING!! this will overwrite a config file if there is one.", action="store_true")
parser.add_argument("-v", "--verbose", help="Increase output verbosity.", action="store_true")
parser.add_argument("-c", "--config", help="Run using alternative config file, default location is /etc/mcfly.conf.", type=loadConfig)
args = parser.parse_args()


if __name__ == "__main__":
    config = loadConfig()
    for server in config["servers"]:
        print(server)
        for dir in config["servers"][server]:
            print("\t" + dir)
