import numpy as np
from astropy.table import Table


def url_path(ra, dec, epoch, sr):
    url = "http://vo.imcce.fr/webservices/skybot/skybotconesearch_query.php?EPOCH=" + epoch + "&RA=" + ra + "&DEC=" + dec + "&SR=" + str(sr)

    return url


def read_table(urlpath):
    try:
        t = Table.read(urlpath)
        return t[0]['name'].decode("utf-8"), t[0]['num'].decode("utf-8")
    except ValueError:
        return "NOTFOUND", "NOTFOUND"
    except urlib.error.URLError:
        return "NO_URL_FOUND", "NO_URL_FOUND"
    except:
        return "SOME_OTHER_ERROR", "SOME_OTHER_ERROR"


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


# print(output_file('testInput.csv', 'testOutput.csv', 0.003))







