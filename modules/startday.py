#!/usr/bin/python
import os
import sys
import webbrowser
import subprocess
import appscript
import webbrowser
import inspect

# This is to import config from ROOT Directory
from inspect import getsourcefile
import os.path

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]
sys.path.insert(0, parent_dir)
# ------- Import Config Ends --------- #

from config import startDayConfig

# This is name of the module
moduleName = "startday"

# These are the words you must say for this module to be executed
commandWords = ["start", "day"]

# This is the main function which will be execute when the above command words are said
def execute(command):
    params = startDayConfig()
    appscript.app('Terminal').do_script('say "Hi Boss, Please wait while i configure system for you."')

    # To Open Terminal commands which are configured in config
    if params.get('terminal') and params['terminal'] != 'NULL':
        terminal = params['terminal'].split(',')
        for terminal_command in terminal:
            appscript.app('Terminal').do_script(terminal_command)

    # To Open Web Browser which are configured in config
    if params.get('browser') and params['browser'] != 'NULL':
        browser = params['browser'].split(',')
        for web_urls in browser:
            webbrowser.open(web_urls, new=2)

    # To Open Installed apps which are configured in config
    if params.get('app') and params['app'] != 'NULL':
        app = params['app'].split(',')
        for launch_app in app:
            subprocess.call(["/usr/bin/open", "-W", "-n", "-a", launch_app])

    # To Open Installed apps which are configured in config
    if params.get('remove_trash') and params['remove_trash'] == 'yes' or params['remove_trash'] == 'YES':
        appscript.app('Terminal').do_script('rm -rf ~/.Trash/*')

    appscript.app('Terminal').do_script('say "WOW..., system configured, ready to use"')
    # Shutdown system command 'sudo shutdown -h now'
    return

#execute("day")
