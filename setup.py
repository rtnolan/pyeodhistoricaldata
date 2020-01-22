from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from os import path
import io

here = path.abspath(path.dirname(__file__))

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    print("Can't import pypandoc - using README.md without converting to RST")
    long_description = open('README.md').read()

install_requires = []
with open("./requirements.txt") as f:
    install_requires = f.read().splitlines()


setup(
    name='pyeodhistorical',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/development.html#single-sourcing-the-version
    # version='0.0.2',
    version=0.0.1,

    description='End Of Day Historical Data using Python',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/tnolan8/pyeodhistorical',

    # Author details
    author='Tom Nolan',
    author_email='tomnolan95@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
     classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ]

    keywords='python trading data stock index',
    install_requires=install_requires,
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    zip_safe=False,
)