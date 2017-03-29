""" Convert xy pixels to ra dec """

from astropy.wcs import WCS
import os.path


def xy_to_radec(filename, x, y):
    if os.path.isfile(filename):
        w = WCS(filename)
        ra, dec = w.all_pix2world(x, y, 0)

        return ra, dec
    else:
        print("NO FILE %s EXISTS" %filename)
        return 0, 0



# print(xy_to_radec('f150_e2_c441.fits', 414, 249))
