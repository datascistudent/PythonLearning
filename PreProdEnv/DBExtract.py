__author__ = 'gkannappan'

#!/usr/bin/env python
import subprocess
import logging
import os

logger = logging.getLogger('')


class VSQL:
    def __init__(self, hostname, password, username, database):
        self.hostname = hostname
        self.password = password
        self.uname = username
        self.database = database
        self.env = dict(os.environ)
        self.env['VSQL_PASSWORD'] = password.replace("'", "")
        self.connectionString = 'vsql -U ' + self.uname + ' -h ' + self.hostname + ' -d ' + self.database

    def executeSQL(self, filename, vsql_error_filename, vsql_out_filename, out_file_name=None, delim=","):
        executeString = self.connectionString + ' -e -At -f ' + filename + ' -v ON_ERROR_STOP=on'

        if vsql_out_filename:  #out_file_name:
            executeString = executeString + ' 1> ' + vsql_out_filename  #out_file_name
        if vsql_error_filename:  #out_file_name:
            executeString = executeString + ' 2> ' + vsql_error_filename  #error_file_name

        ret_code = subprocess.call(executeString, env=self.env, shell=True)

        if ret_code == 0:
            if os.path.isfile(vsql_out_filename) and os.path.getsize(vsql_out_filename) > 0:
                outfile = open(vsql_out_filename,'r')
                logger.debug(outfile.read())
                outfile.close()
                os.remove(vsql_out_filename)
                if os.path.isfile(vsql_error_filename):
                    if os.path.getsize(vsql_error_filename) > 0 :
                        errfile = open(vsql_error_filename,'r')
                        logger.debug(errfile.read())
                        errfile.close()
                    os.remove(vsql_error_filename)
                return ret_code
        else:
            return -1

    def exportToCSV(self, export_query, vsql_error_filename, vsql_out_filename, out_file_name, delim=','):
        executeString = self.connectionString + " -F $',' -At -o " + out_file_name + " -f  '" + export_query + "' -e -v ON_ERROR_STOP=on"
        if vsql_out_filename:  #out_file_name:
            executeString = executeString + ' 1> ' + vsql_out_filename  #out_file_name
        if vsql_error_filename:  #out_file_name:
            executeString = executeString + ' 2> ' + vsql_error_filename  #error_file_name

        ret_code = subprocess.call(executeString, env=self.env, shell=True)

        if ret_code == 0:
            return ret_code
        else:
            return -1

    def exportToFile(self, filename, vsql_error_filename, vsql_out_filename, out_file_name, delim=chr(30)):
        executeString = self.connectionString + " -F " + delim + " -At -o " + out_file_name + " -f '" + filename + "' -e -v ON_ERROR_STOP=on"
        #print executeString
        if vsql_out_filename:  #out_file_name:
            executeString = executeString + ' 1> ' + vsql_out_filename  #out_file_name
        if vsql_error_filename:  #out_file_name:
            executeString = executeString + ' 2> ' + vsql_error_filename  #error_file_name

        ret_code = subprocess.call(executeString, env=self.env, shell=True)

        if ret_code == 0:
            return ret_code
        else:
            return -1

    def executeCopyLocal(self, copy_local_sql, vsql_error_filename, vsql_out_filename, out_file_name=None, delim=","):
        executeString = self.connectionString + " -F $',' -At -f " + copy_local_sql + " -e -v ON_ERROR_STOP=on"
        if vsql_out_filename:  #out_file_name:
            executeString = executeString + ' 1> ' + vsql_out_filename  #out_file_name
        if vsql_error_filename:  #out_file_name:
            executeString = executeString + ' 2> ' + vsql_error_filename  #error_file_name

        ret_code = subprocess.call(executeString, env=self.env, shell=True)

        if ret_code == 0:
            return ret_code
        else:
            return -1

if __name__ == "__main__":
    sqlfilelist = [
                #"matt_stg.PSA_EFS_FILING_STATUS_CHANGE"
                "matt_stg.PSA_EFS_FILING_PAYMENT",
                "matt_stg.PSA_EFS_RISK_SCORE"
                ]

    #v = VSQL('pprfdaavth-vip.ie.intuit.net', 'Intuit13', 'aggmod_etl', 'Analytics')
    v = VSQL('pprddaavth-vip.ie.intuit.net', 'Intuit10', 'aggmod_etl', 'Analytics')
    for file in sqlfilelist:
        sqlfile = "/Users/gkannappan/Documents/Intuit/CTG/PreProdEnv/MATT/EFS/"+file+".sql"
        print sqlfile
        txtfile = "/Users/gkannappan/Documents/Intuit/CTG/PreProdEnv/MATT/EFS/"+file+".txt"
        print txtfile
    #v.exportToFile("/Users/gkannappan/Documents/Intuit/CTG/PreProdEnv/CARE/SFDC/CARE_STG.STG_SF_CASE.sql", "/Users/gkannappan/Documents/Intuit/CTG/PreProdEnv/CARE/SFDC/err.txt","/Users/gkannappan/Documents/Intuit/CTG/PreProdEnv/CARE/SFDC/vout.txt", "/Users/gkannappan/Documents/Intuit/CTG/PreProdEnv/CARE/SFDC/CARE_STG.STG_SF_CASE.txt")
        v.exportToFile(sqlfile, "/Users/gkannappan/Documents/Intuit/CTG/PreProdEnv/MATT/EFS/err.txt","/Users/gkannappan/Documents/Intuit/CTG/PreProdEnv/MATT/EFS/vout.txt", txtfile)
