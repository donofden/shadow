#!/usr/bin/python
import sys
import os

from configparser import ConfigParser

# DataBase Config
def mailConfig(filename='config.ini', section='gmail'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    mailInfo = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            mailInfo[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return mailInfo
