from astropy.io import fits
from astropy.wcs import WCS
from astropy.table import Table
import argparse
import urllib
import warnings

DEFAULT_SR = 100  # Default search radius in arcsec


def skybot_url(ra, dec, epoch, radius):
    sr = radius / 3600.
    url = "http://vo.imcce.fr/webservices/skybot/skybotconesearch_query.php?EPOCH={}&RA={}&DEC={}&SR={}".format(epoch, ra, dec, sr)
    return url


def identify_body(ra, dec, epoch, radius):
    """Returns name and number if a body is known."""
    url = skybot_url(ra, dec, epoch, radius)
    try:
        t = Table.read(url)
        return t[0]['name'].decode("utf-8"), t[0]['num'].decode("utf-8")
    except ValueError:
        return "NOTFOUND", "NOTFOUND"
    except urllib.error.URLError:
        return "URLERROR", "URLERROR"
    except:
        return "ERROR", "ERROR"


def watplanet_main(args=None):
    warnings.filterwarnings('ignore')

    parser = argparse.ArgumentParser(description="WATPLANET?!")
    parser.add_argument("-r", "--radius", metavar='degrees',
                        nargs="?", type=float, default=DEFAULT_SR,
                        help="Search radius in arcsec (default: 30 arcsec).")
    parser.add_argument('fitsfile', nargs=1,
                        help="Path to a FITS file.")
    parser.add_argument('x', nargs=1, type=float,
                        help="FITS pixel x coordinate.")
    parser.add_argument('y', nargs=1, type=float,
                        help="FITS pixel y coordinate.")
    parser.add_argument('timestamp', nargs=1,
                        help="ISO timestamp, example 2017-01-01T12:00:00.")
    args = parser.parse_args(args)

    x, y = float(args.x[0]), float(args.y[0])
    f = fits.open(args.fitsfile[0])
    mywcs = WCS(f[0].header)
    ra, dec = mywcs.all_pix2world([[x, y]], 0)[0]
    name, num = identify_body(ra, dec, args.timestamp[0], args.radius)
    print('(ra, dec) = ({}, {})'.format(ra, dec))
    print('Search radius: {:.0f} arcsec'.format(args.radius))
    print('Object name: {}  (number: {})'.format(name, num))


if __name__ == '__main__':
    watplanet_main()
