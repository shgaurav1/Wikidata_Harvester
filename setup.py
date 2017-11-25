from setuptools import setup
setup(
  name = 'wikidata',
  packages = ['wikidata'], # this must be the same as the name above
  version = '0.1',
  description = 'An API for exploiting Wikidata dump',
  author = 'Jacques Fize, Gaurav Shrivastava',
  author_email = 'jacques.fize@cirad.fr, gauravsh033@gmail.com',
  keywords = ['api', 'wikidata', 'LOD'], # arbitrary keywords
  classifiers = [
      "Development Status :: 4 - Beta",
      "Programming Language :: Python :: 3"
      "Programming Language :: Python :: 3.6",
      "Operating System :: Microsoft",
      "Operating System :: MacOS",
      "Operating System :: Unix",
      "Topic :: Utilities",
      "License :: OSI Approved :: MIT License"
  ],
  install_requires=[
            'python-dateutil'
        ],
)