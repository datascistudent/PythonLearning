__author__ = 'gkannappan'

from FTPUtils import FTPUtils

if __name__ == "__main__":

    finalfilelist = ["FILING_COPY.txt.gz"]
    put = FTPUtils('pprfdaaetlc01.ie.intuit.net','deploy','data2ETL!23', '/Users/gkannappan/Documents/Intuit/CTG/PreProdEnv/MATT/EFS', '/data/data_collection/MATT/EFS')
    put.Connect()
    for file in finalfilelist:
        put.FilePut(file)
    put.ConnectClose()
