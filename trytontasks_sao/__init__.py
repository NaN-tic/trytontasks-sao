#This file is part of trytontasks_sao. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
import os
import webbrowser
from invoke import task
from blessings import Terminal
from trytontasks_modules import read_config_file

t = Terminal()

@task
def install():
    'Install SAO'
    os.chdir('sao')
    os.system('npm install')
    os.system('bower install')

    print t.bold('Done')

@task
def grunt():
    'Grunt SAO'
    os.chdir('sao')
    os.system('grunt')

    print t.bold('Done')

@task
def locales():
    'Locales SAO'
    os.chdir('sao')
    os.system('grunt po2json')

    print t.bold('Done')

@task
def open(server):
    'Open SAO in browser'
    Servers = read_config_file('servers.cfg', type='servers')
    servers = Servers.sections()
    servers.sort()

    if not server in servers:
        print 'Not found %s' % server
        return

    url = Servers.get(server, 'sao')
    if url:
        webbrowser.open(url, new=1)
