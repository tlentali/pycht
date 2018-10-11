from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='cheshire',
    url='https://github.com/tlentali/cheshire',
    author='Thomas Lentali',
    author_email='thomas.lentali@gmail.com',
    # Needed to actually package something
    packages=['cheshire'],
    # Needed for dependencies
    install_requires=['pandas',
                      'numpy',
                      'opencv-python',
                      'python-dateutil',
                      'pytz'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='From pics to stencil',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)
