import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'weheartit'
AUTHOR = 'aswinnnn'
AUTHOR_EMAIL = 'xaswinsnairx@gmail.com'
URL = 'https://github.com/aswinnnn/weheartit'

LICENSE = 'MIT License'
DESCRIPTION = 'A fast, realiable API wrapper for weheartit.com, in Python.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'requests',
      'beautifulsoup4'
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