""" Convert xy pixels to ra dec """

from astropy.wcs import WCS


def xy_to_radec(filename, x, y):
    w = WCS(filename)
    ra, dec = w.all_pix2world(x, y, 0)

    return ra, dec

# print(xy_to_radec('f245_e2_c845.fits', 0, 0))
