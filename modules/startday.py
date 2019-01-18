#!/usr/bin/python
import os
import webbrowser
import subprocess
import appscript
import webbrowser

#This is name of the module
moduleName = "startday"

#These are the words you must say for this module to be executed
commandWords = ["start","day"]

#This is the main function which will be execute when the above command words are said
def execute(command):
	webbrowser.open('http://google.com', new=2)
	appscript.app('Terminal').do_script('ssh-add -K && ls')  # or any other command you choose
	subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Slack.app"])
	#subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/PhpStrom.app"])
	return

#execute("day")
