#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
import time
import os
import subprocess

parser = argparse.ArgumentParser(description='Best Friend tool to discover RAR passwords')

parser.add_argument("-f", help='rar file (with path) you want to discover the password')
parser.add_argument("-w", help='wordlist file (words separated by newlines \n')
parser.add_argument("-n", help='Use numbers only')
parser.add_argument("-s", help='Start string size', type=int)

parser.parse_args()

