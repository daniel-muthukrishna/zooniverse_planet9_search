from check_minor_planet_catalog import check_catalog
from xy_to_radec import xy_to_radec
from get_date_time import get_date_time

class GetPointInfo():
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.filename = filename
        self.field = self.get_field_from_filename()
        self.epoch = self.get_epoch()
        self.ra, self.dec = self.get_radec()

    def get_field_from_filename(self):
        field = self.filename.split("_")[0].strip("f")

        return field

    def get_radec(self):
        fitsFilename = self.filename.split(".")[0] + ".fits"
        ra, dec = xy_to_radec(fitsFilename, self.x, self.y)

        return ra, dec

    def get_epoch(self):
        epoch = get_date_time(self.field)

        return epoch

    @staticmethod
    def get_catalog_entry(ra, dec, epoch, searchRadius):
        catalogName, catalogNum = check_catalog(ra, dec, epoch, searchRadius)

        return catalogName


