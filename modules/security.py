#!/usr/bin/python
import os
from subprocess import call

#T his is name of the module
moduleName = "security"

# These are the words you must say for this module to be executed
commandWords = ["prime", "sleep"]

# This is the main function which will be execute when the above command words are said
def execute(command):
	os.system('pmset displaysleepnow')
	return
