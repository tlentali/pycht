import io
import os

from setuptools import find_packages
from setuptools import setup


# Package meta-data.
NAME = 'cheshire'
DESCRIPTION = 'Streetart by clustering.'
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'
URL = 'https://github.com/tlentali/cheshire'
EMAIL = 'thomas.lentali@gmail.com'
AUTHOR = 'Thomas Lentali'
REQUIRES_PYTHON = '>=3.6.0'
LICENCE='MIT'
VERSION = '0.1'

# Package requirements.
base_packages = [
    'numpy==1.21.0',
    'opencv-python==3.4.3.18',
    'pandas==0.20.1',
    'pytz==2018.5',
    'six==1.11.0',
    ]

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name=NAME,
    packages=find_packages(),
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    version=VERSION,
    license=LICENCE,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    python_requires=REQUIRES_PYTHON,
    keywords=['data-science', 'machine-learning', 'clustering','statistics', 'streetart', 'stencil', 'art'],
    install_requires=base_packages,
    classifiers=[
    # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    ],
)
