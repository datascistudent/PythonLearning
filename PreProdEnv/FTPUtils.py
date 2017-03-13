__author__ = 'gkannappan'

import paramiko
import FileUtils

class FTPUtils():
    #def __init__(self, server, user, pwd, srcdir, tgtdir, file):
    def __init__(self, server, user, pwd, srcdir, tgtdir):
        self.server = server
        self.user = user
        self.pwd = pwd
        self.srcdir = srcdir
        self.tgtdir = tgtdir
        #self.file = file

    def Connect(self):
        self.client = paramiko.Transport(self.server)
        self.client.connect(username=self.user, password = self.pwd)

    def FileGet(self, file):
        ftp = self.client.open_sftp_client()
        ftp.chdir(path=self.srcdir)
        srcfilename = self.srcdir + '/' + file
        tgtfilename = self.tgtdir + '/' + file
        ftp.get(srcfilename, tgtfilename)
        ftp.close()

    def FilePut(self, file):
        ftp = self.client.open_sftp_client()
        ftp.chdir(path=self.tgtdir)
        srcfilename = self.srcdir + '/' + file
        tgtfilename = self.tgtdir + '/' + file
        ftp.put(srcfilename,tgtfilename)
        ftp.close()

    def FileList(self):
        ftp = self.client.open_sftp_client()
        ftp.chdir(path=self.srcdir)
        ListofFiles = ftp.listdir(path=self.srcdir)
        return ListofFiles
        ftp.close()

    def ConnectClose(self):
        self.client.close()

if __name__ == "__main__":
    #destfilelist = ['DS_20170201.tar.gz','DS_20170202.tar.gz','DS_20170203.tar.gz','DS_20170204.tar.gz','DS_20170205.tar.gz']

    '''
    destfilelist = [
        'DS_20170201.tar.gz','DS_20170202.tar.gz','DS_20170203.tar.gz','DS_20170204.tar.gz','DS_20170205.tar.gz',
        'DS_20170206.tar.gz','DS_20170207.tar.gz','DS_20170208.tar.gz','DS_20170209.tar.gz','DS_20170210.tar.gz',
        'DS_20170211.tar.gz','DS_20170212.tar.gz','DS_20170213.tar.gz','DS_20170214.tar.gz','DS_20170215.tar.gz',
        'DS_20170216.tar.gz','DS_20170217.tar.gz','DS_20170218.tar.gz','DS_20170219.tar.gz','DS_20170220.tar.gz',
        'DS_20170221.tar.gz','DS_20170222.tar.gz','DS_20170223.tar.gz','DS_20170224.tar.gz','DS_20170225.tar.gz',
        'DS_20170226.tar.gz','DS_20170227.tar.gz','DS_20170228.tar.gz'
    ]
    '''
    filelist = FileUtils.GenFileList('201702',15)
    print filelist

    #filelist = ["text01.txt", "text02.txt"]
    #filelist = GenFileList('01', 2)
    #print filelist
    #pp = FTPUtils('pprfdaaetlc01.ie.intuit.net','deploy','data2ETL!23','/data/DATA_SOURCES/MATT/DS/archive/dat', '/Users/gkannappan/Desktop')

    get = FTPUtils('pprddaaetlc01.ie.intuit.net','deploy','data2ETL!23', '/data/DATA_SOURCES/MATT/TDES/archive/dat', '/Users/gkannappan/Documents/Intuit/CTG/PreProd Env/MATT/TDES')
    get.Connect()
    destfilelist = get.FileList()
    finalfilelist = FileUtils.PatternMatch(filelist, ".tar.gz", destfilelist)
    #print finalfilelist

    for file in finalfilelist:
        get.FileGet(file)
        #pp.FilePut(file)
    get.ConnectClose()

    put = FTPUtils('pprfdaaetlc01.ie.intuit.net','deploy','data2ETL!23', '/Users/gkannappan/Documents/Intuit/CTG/PreProd Env/MATT/TDES', '/data/data_collection/MATT/TDES')
    put.Connect()
    for file in finalfilelist:
        put.FilePut(file)
    put.ConnectClose()
