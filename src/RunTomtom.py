__author__ = 'Jonathan Rubin'

#Runs Tomtom on MEME output

import os

def run(Memedir,database):
    os.system("tomtom " + Memedir + "/dreme.html " + database)