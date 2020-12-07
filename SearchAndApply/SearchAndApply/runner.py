import os
from scrapy.cmdline import execute

os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    execute([
        'scrapy',
        'crawl',
        'af'  # change this to the spider of choice
    ])

except SystemExit:
    pass