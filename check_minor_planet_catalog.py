import numpy as np
from astropy.table import Table
import urllib2


def url_path(ra, dec, epoch, sr):
    url = "http://vo.imcce.fr/webservices/skybot/skybotconesearch_query.php?EPOCH={}&RA={}&DEC={}&SR={}".format(epoch, ra,dec, sr)

    return url


def read_table(urlpath):
    try:
        t = Table.read(urlpath)
        return t[0]['name'], t[0]['num']
    except ValueError:
        return "NOTFOUND", "NOTFOUND"
    except urllib2.URLError:
        return read_table_if_time_out_error(urlpath)

    # except urlib.error.URLError:
    #     return "SOME_OTHER_ERROR", "SOME_OTHER_ERROR"


def read_table_if_time_out_error(urlpath):
    try:
        response = urllib2.urlopen(urlpath, timeout=5)
        html = response.read()
        with open('votable_test.txt', 'w') as f:
            f.write(html)
        t = Table.read('votable_test.txt')
        return t[0]['name'], t[0]['num']
    except urllib2.URLError, e:
        print(e)
        return "NO_URL_FOUND", "NO_URL_FOUND"



def check_catalog(ra, dec, epoch, searchRadius):
    url = url_path(ra, dec, epoch, searchRadius)
    catalogName, catalogNum = read_table(url)

    return catalogName, catalogNum


def output_file(inputFilename, outputFilename, sr):
    infoList = np.genfromtxt(inputFilename, skip_header=1, dtype=None)
    nameList = []

    f = open(outputFilename, 'w')
    f.write("# ID,RA,DEC,EPOCH,DATABASE_NAME,DATABASE_NUM\n")

    for info in infoList:
        title, ra, dec, epoch = str(info).strip("'").split(',')
        url = url_path(ra, dec, epoch, sr)
        outName, outNum = read_table(url)
        nameList.append(outName)

        f.write(str(info.decode("utf-8")) + "," + str(outName) + "," + str(outNum) + "\n")
    f.close()

    return nameList


print(output_file('testInput.csv', 'testOutput.csv', 0.003))







