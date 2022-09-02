import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.2.4'
PACKAGE_NAME = 'weheartpy'
AUTHOR = 'aswinnnn'
AUTHOR_EMAIL = 'aswinsnair028@gmail.com'
URL = 'https://github.com/aswinnnn/weheartpy'

LICENSE = 'MIT License'
DESCRIPTION = 'A comprehensive, realiable API client for weheartit.com.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'requests',
      'beautifulsoup4',
      'lxml',
      'user-agent'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )