import sys

try:
    from osgeo import gdal
    from osgeo import osr
except:
    import gdal
    print('You are using "old gen" bindings. gdal2tiles needs "new gen" bindings.')
    sys.exit(1)

import os
import math

os.system(gdal2tiles.py -h)