import os
from setuptools import setup, find_packages, find_namespace_packages
PACKAGES = find_packages()

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = " "
# Long description will go up on the pypi page
long_description = """

"""

NAME = "Yelp Reviews"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = ""
DOWNLOAD_URL = ""
LICENSE = ""
AUTHOR = "Tommy Chen | Emily | Sindhu"
AUTHOR_EMAIL = ""
PLATFORMS = ""
VERSION = "__version__ 1.0"
PACKAGE_DATA = {}
REQUIRES = ["numpy", "pandas", "requests", "bs4", "nltk"]

opts = dict(name=NAME,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            url=URL,
            download_url=DOWNLOAD_URL,
            license=LICENSE,
            classifiers=CLASSIFIERS,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            platforms=PLATFORMS,
            version=VERSION,
            packages=PACKAGES,
            install_requires=REQUIRES,
            requires=REQUIRES)

'''
setup(
    name = 'code',
    version = '1.0',
    packages = ['code', 'code.yelp_parse', 'code.yelp_scraping'],
    package_data = {'code.yelp_parse':['code/yelp_parse.py'], 'code.yelp_scraping':['code/yelp_scraping.py']}
)
'''

if __name__ == '__main__':
    setup(**opts)