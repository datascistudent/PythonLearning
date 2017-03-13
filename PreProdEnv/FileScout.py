__author__ = 'gkannappan'

import os
from ftplib import FTP
from os import listdir
import paramiko

path = '/data/DATA_SOURCES/MATT/DS/archive/dat'
client = paramiko.Transport('pprfdaaetlc01.ie.intuit.net')
client.connect(username='deploy', password = 'data2ETL!23')
f = client.open_sftp_client()
f.chdir(path=path)
cwd = f.getcwd()
#print f.getcwd(),"---< Current working diectory"
#print "cwd", cwd

#print f.listdir(path="/data/DATA_SOURCES/lib/python2.7/site-packages/etl-data-sources/MATT/DS/logs")
#print f.list_folder(path)
for i in f.listdir(path):
    print i
#print f.list_folder(path)

#for item in listdir('/data/DATA_SOURCES/lib/python2.7/site-packages/etl-data-sources/MATT/DS/archive/dat/'):
#    print item

'''
try
    client.chdir()
    sftp = client
chdir(path='/data/DATA_SOURCES/MATT/DS/archive/dat')
print "Current working directory:", client.getcwd()
'''
f.close()
client.close()
