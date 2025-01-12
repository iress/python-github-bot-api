# This file was auto-generated by Shut. DO NOT EDIT
# For more information about Shut, check out https://pypi.org/project/shut/

from __future__ import print_function
import io
import os
import setuptools
import sys

readme_file = 'README.md'
if os.path.isfile(readme_file):
  with io.open(readme_file, encoding='utf8') as fp:
    long_description = fp.read()
else:
  print("warning: file \"{}\" does not exist.".format(readme_file), file=sys.stderr)
  long_description = None

requirements = [
  'PyJWT >=2.0.0,<3.0.0',
  'cryptography >=3.1.1,<4.0.0',
  'requests >=2.25.0,<3.0.0',
  'Deprecated >=1.2.12,<2.0.0',
  'urllib3 >=1.26.6,<2.0.0',
  'nr.functional >=0.2.0,<1.0.0',
]
test_requirements = [
  'PyGithub',
  'types-deprecated',
  'types-flask',
  'types-jwt',
  'types-requests',
]
extras_require = {}
extras_require['test'] = test_requirements

setuptools.setup(
  name = 'github-bot-api',
  version = '0.5.0',
  author = 'Niklas Rosenstein',
  author_email = 'nrosenstein@palantir.com',
  description = 'API for creating GitHub bots and webhooks in Python.',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://niklasrosenstein.github.io/python-github-bot-api/',
  license = 'MIT',
  packages = setuptools.find_packages('src', ['test', 'test.*', 'tests', 'tests.*', 'docs', 'docs.*']),
  package_dir = {'': 'src'},
  include_package_data = True,
  install_requires = requirements,
  extras_require = extras_require,
  tests_require = test_requirements,
  python_requires = '>=3.8.0,<4.0.0',
  data_files = [],
  entry_points = {},
  cmdclass = {},
  keywords = [],
  classifiers = [],
  zip_safe = False,
)
