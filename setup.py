from setuptools import setup, find_namespace_packages

setup(
    name = 'code',
    version = '1.0',
    packages = ['code', 'code.yelp_parse', 'code.yelp_scraping'],
    package_data = {'code.yelp_parse':['code/yelp_parse.py'], 'code.yelp_scraping':['code/yelp_scraping.py']}
)