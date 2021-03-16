from setuptools import setup, find_packages

PACKAGES = find_packages()

CLASSIFIERS = ["Environment :: Console",
               "Intended Audience :: Science/Research",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Yelp Reviews"]

NAME = "Yelp Reviews"
DESCRIPTION = "A data science project using Yelp Fusion API and Web Scraping"
URL = "https://github.com/tommycqy/Yelp-Reviews"
AUTHOR = "Tommy Chen | Emily Yamauchi| Sindhu Madhadi"
AUTHOR_EMAIL = "qingyuc@uw.edu, eyamauch@uw.edu, sindhu09@uw.edu"
PLATFORMS = "Linux, Windows and MacOS"
VERSION = "__version__ 1.0"
REQUIRES = ["numpy", "pandas", "requests",
            "bs4", "nltk", "mapboxgl"]

opts = dict(name=NAME,
            description=DESCRIPTION,
            url=URL,
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
