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
    install_requires=['pandas==0.20.1',
                      'numpy==1.15.2',
                      'opencv-python==3.4.7.28',
                      'python-dateutil==2.7.3',
                      'pytz==2018.5',
                      'six==1.11.0'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='From pics to stencil',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)
