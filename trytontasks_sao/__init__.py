#This file is part of trytontasks_sao. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
import os
from invoke import task
from blessings import Terminal

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
