#!/usr/bin/python
from configparser import ConfigParser

# DataBase Config
def mailConfig(filename='config.ini', section='gmail'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    mailinfo = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            mailinfo[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return mailinfo


# DataBase Config
def startDayConfig(filename='config.ini', section='start-day'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    mailinfo = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            mailinfo[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return mailinfo
