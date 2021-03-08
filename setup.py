from setuptools import setup, find_packages

PACKAGES = find_packages()

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]


NAME = "Yelp Reviews"
DESCRIPTION = "A data science project using Yelp Fusion API and Web Scraping"
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

if __name__ == '__main__':
    setup(**opts)
