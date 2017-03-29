from check_minor_planet_catalog import check_catalog
from xy_to_radec import xy_to_radec
from get_date_time import get_date_time
import pandas as pd
import json
import csv
import sys


class GetPointInfo(object):
    def __init__(self, x, y, filename, colour):
        self.x = x
        self.y = y
        self.filename = filename
        self.colour = colour
        self.field = self.get_field_from_filename()
        self.epoch, self.julian = self.get_epoch()
        self.ra, self.dec = self.get_radec()
        searchRadiusArcsec = 40.
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
        if (ra, dec) != (0, 0):
            catalogName, catalogNum = check_catalog(ra, dec, julian, searchRadius)
        else:
            catalogName, catalogNum = "NO_FITS_FILE_FOUND", "NO_FITS_FILE_FOUND"

        return catalogName, catalogNum


def read_input_file(csvFile):
    outputLines = []
    df = pd.read_csv(csvFile)

    for row in df.iterrows():
        subjectID = row[1]['subject_id']
        filename = row[1]['png_filename']
        marks = row[1]['marks']
        marks = marks.replace('(', '[').replace(')', ']')
        marks = json.loads(marks)

        for mark in marks:
            outputLine = output_line(mark[0], mark[1], filename, subjectID)
            outputLines.append(outputLine)

    return outputLines


def output_line(x, y, filename, subjectID):
    outLines = []
    for colour in ['r', 'g', 'b']:
        outInfo = GetPointInfo(x, y, filename, colour)
        outLine = [subjectID, filename, colour, float(outInfo.ra), float(outInfo.dec), outInfo.julian, outInfo.catalogName, outInfo.catalogNum]
        outLines.append(outLine)
        print(outInfo.catalogName, filename, subjectID, (outInfo.ra, outInfo.dec), colour, (outInfo.ra, outInfo.dec))

    return outLines


def output_to_file(inCSVFile, outFileName="output-subjects-of-interests.csv"):
    outputTable = read_input_file(inCSVFile)
    if sys.version_info >= (3, 0, 0):
        outFile = open(outFileName, 'w', newline='')
    else:
        outFile = open(outFileName, 'wb')

    wr = csv.writer(outFile)
    wr.writerows(outputTable)

    return outputTable



if __name__ == '__main__':
    csvFile = 'subjects-of-interest.csv'
    print(output_to_file(csvFile))



