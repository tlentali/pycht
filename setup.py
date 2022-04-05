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

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name=NAME,
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    # Needed to actually package something
    packages=['cheshire'],
    # Needed for dependencies
    install_requires=['pandas==0.20.1',
                      'numpy==1.15.2',
                      'opencv-python==3.4.3.18',
                      'python-dateutil==2.7.3',
                      'pytz==2018.5',
                      'six==1.11.0'],
    version=VERSION,
    license=LICENCE,
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
     keywords=['data-science', 'machine-learning', 'clustering','statistics', 'streetart', 'stencil', 'art'],
    classifiers=[
    # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
)
