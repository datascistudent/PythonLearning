__author__ = 'gkannappan'

import re
import os

def GenFileList(startdate, numdays):
    i = 1
    filelist = []
    while i <= numdays:
        last2 = startdate[-6:]
        filelist.append(startdate+str('{:02d}'.format(i)))
        #filelist.append('{:06d}'.format(int(last2) + i))
        i=i+1
    return filelist

def PatternMatch(f, e, d):
    filelist = f
    extn = e
    dfilelist = d
    #dr = d #
    #allfiles = os.listdir(dr)
    destfilelist = []

    for srcfile in filelist:
        for destfile in dfilelist:
            if re.search(srcfile+extn, destfile):
                destfilelist.append(destfile)
    return destfilelist

if __name__ == "__main__":
    filelist = GenFileList('01',2)
    print filelist
    destfilelist = PatternMatch(filelist, ".txt", '/Users/gkannappan/Desktop/')
    print destfilelist
