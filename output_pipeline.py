from check_minor_planet_catalog import check_catalog
from xy_to_radec import xy_to_radec
from get_date_time import get_date_time
import pandas as pd
import json
import csv
import sys
from astropy.time import Time
import datetime


class GetPointInfo(object):
    def __init__(self, x, y, filename, colour):
        self.x = x
        self.y = y
        self.filename = filename
        self.colour = colour
        self.field = self.get_field_from_filename()
        self.epoch, self.julian = self.get_epoch()
        self.ra, self.dec = self.get_radec()
        searchRadiusArcsec = 20.
        searchRadiusDeg = searchRadiusArcsec/3600.
        self.catalogName, self.catalogNum = self.get_catalog_entry(self.ra, self.dec, self.julian, searchRadiusDeg)

    def get_field_from_filename(self):
        field = self.filename.split("_")[0].strip("f")

        return field

    def get_radec(self):
        f = self.filename.split(".")[0].split('-')[0].split('_')[0]
        c = self.filename.split(".")[0].split('-')[0].split('_')[1]
        fitsFilename = f + '_' + 'e2_' + c + '.fits'
        filePath = '../' + self.field + '/' + fitsFilename

        ra, dec = xy_to_radec(filePath, self.x, self.y)

        return ra, dec

    def get_epoch(self):
        epoch, julian = get_date_time(str(self.field), self.colour)

        return epoch, julian

    @staticmethod
    def get_catalog_entry(ra, dec, julian, searchRadius):
        if (ra, dec) == (0, 0):
            catalogName, catalogNum = "NO_FITS_FILE_FOUND", "NO_FITS_FILE_FOUND"
        elif (julian == 0):
            catalogName, catalogNum = "NO_DATE_FOUND", "NO_DATE_FOUND"
        else:
            catalogName, catalogNum = check_catalog(ra, dec, julian, searchRadius)

        return catalogName, catalogNum


def read_input_file(csvFile):
    outputLines = []
    findOrbLines = []
    df = pd.read_csv(csvFile)

    for row in df.iterrows():
        subjectID = row[1]['subject_id']
        filename = row[1]['png_filename']
        marks = row[1]['marks']
        marks = marks.replace('(', '[').replace(')', ']')
        marks = json.loads(marks)

        for mark in marks:
            outputLine, findOrbLine = output_line(mark[0], mark[1], filename, subjectID)
            outputLines.append(outputLine)
            findOrbLines.append(findOrbLine)

    return outputLines, findOrbLines


def output_line(x, y, filename, subjectID):
    outLines = []
    findOrbLines = []
    for colour in ['r', 'g', 'b']:
        outInfo = GetPointInfo(x, y, filename, colour)
        outLine = [subjectID, filename, colour, float(outInfo.ra), float(outInfo.dec), float(outInfo.x), float(outInfo.y), outInfo.julian, outInfo.catalogName, outInfo.catalogNum]
        outLines.append(outLine)
        print(outInfo.catalogName, filename, subjectID, (float(outInfo.ra), float(outInfo.dec)), colour, (float(outInfo.x), float(outInfo.y)))

        findOrbLine = findorb_write_line(subjectID, outInfo.julian, outInfo.ra, outInfo.dec)
        findOrbLines.append(findOrbLine)

    return outLines, findOrbLines


def output_to_file(inCSVFile, outFileName="output-subjects-of-interests.csv", findOrbFile = "findOrbInput.txt"):
    outputTable, findOrbLines = read_input_file(inCSVFile)
    if sys.version_info >= (3, 0, 0):
        outFile = open(outFileName, 'w', newline='')
        findOrbFile = open(findOrbFile, 'w', newline='')
    else:
        outFile = open(outFileName, 'wb')
        findOrbFile = open(findOrbFile, 'wb')

    wr = csv.writer(outFile)
    wr.writerows(outputTable)
    outFile.close()

    for IDList in findOrbLines:
        for line in IDList:
            findOrbFile.write(line)
    findOrbFile.close()

    return outputTable


def findorb_write_line(subjectID, julian, ra, dec):
    t = Time([julian], format='jd')
    time = t.tt.fits[0].split('-')
    year = time[0]
    month = time[1]
    day = time[2].split('T')[0]
    (h, m, s) = time[2].split('T')[1].strip('(').split(':')
    timeFraction = round((int(h) * 3600 + int(m) * 60 + float(s)) / (24 * 60 * 60.), 5)
    timeFractionAsStr = str(round(timeFraction, 5)).strip('0.')
    raHour = int(ra/360.)
    raMin = int((ra/360 * 60) % 60)
    raSec = float((ra/360 * 3600) % 60)
    decDeg = int(dec)
    decHour = int((float(dec) - int(dec)) * 60)
    decMin = ((float(dec) - int(dec)) * 60 - decHour)*60



    row = "     {0}  J{1} {2} {3}.{4} {5:2d} {6:2d} {7:.2f} {8:2d} {9:2d} {10:.1f}                      260\n".format(subjectID, year, month, day, timeFractionAsStr, raHour, raMin, raSec, decDeg, decHour, decMin)
#row = "     8410550  J2014 08 31.65338 23 58 23.09 -01 57 41.5                      260"
    return row


def create_findorb_input_file(subjectID):
    header = "Name~~~~~~~~Date~~~~~~~~~~~~~~~~RA~~~~~~~~~~DEC~~~~~~~~~Blanks~~~~~~~~~~~~~~~ObservatoryID"
    row = findorb_write_line()



if __name__ == '__main__':
    csvFile = 'subjects-of-interest.csv'
    print(output_to_file(csvFile))



