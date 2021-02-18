from boto3.session import Session
from osgeo import gdal
from pathlib import Path
import os
import boto3

def get_extent(gt, cols, rows):
    ''' Return list of corner coordinates from a geotransform

        @type gt:   C{tuple/list}
        @param gt: geotransform
        @type cols:   C{int}
        @param cols: number of columns in the dataset
        @type rows:   C{int}
        @param rows: number of rows in the dataset
        @rtype:    C{[float,...,float]}
        @return:   coordinates of each corner
    '''
    ext = []
    xarr = [0, cols]
    yarr = [0, rows]

    for px in xarr:
        for py in yarr:
            x = gt[0]+(px*gt[1])+(py*gt[2])
            y = gt[3]+(px*gt[4])+(py*gt[5])
            ext.append([x, y])
        yarr.reverse()
    return ext


def get_coordinates_from_tif(filename):
    ACCESS_KEY = os.environ["AWS_ACCESS_KEY"]
    SECRET_KEY = os.environ["AWS_SECRET_KEY"]
    BASE_DIR = Path(__file__).resolve().parent
    BUCKET = 'skyprecison'

    NEW_FILE_PATH = BASE_DIR.parent / 'tif_files' / filename

    # Only download the file if it doesn't already exist
    if not NEW_FILE_PATH.exists():
        s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)
        s3.download_file(BUCKET, filename, str(NEW_FILE_PATH))


    source = gdal.Open(str(NEW_FILE_PATH))
    a = source.GetGeoTransform()
    b = source.RasterXSize
    c = source.RasterYSize

    TOP_LEFT = 0
    BOTTOM_LEFT = 1
    BOTTOM_RIGHT = 2
    TOP_RIGHT = 3

    LONGITUDE = 0
    LATITUDE = 1

    coords = get_extent(a, b, c)

    return[coords[TOP_LEFT][LATITUDE], coords[BOTTOM_RIGHT][LATITUDE], coords[TOP_LEFT][LONGITUDE], coords[BOTTOM_RIGHT][LONGITUDE]]

if __name__ == "__main__":
    filename = 'isaacmiller_Blenheim_2019_10_06_ndvi_0.tif'
    print(get_coordinates_from_tif(filename))
