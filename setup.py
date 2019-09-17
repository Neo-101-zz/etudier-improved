from sys import exit
from setuptools import setup
from distutils.spawn import find_executable

if not (find_executable('chromedriver') or find_executable('chromedriver.exe')):
    exit('You need to install chromedriver https://sites.google.com/a/chromium.org/chromedriver/')

with open("README.md") as f:
    long_description = f.read()

setup(
    name = 'etudier',
    version = '0.0.7',
    url = 'https://github.com/edsu/etudier',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    py_modules = ['etudier',],
    description = 'Collect a citation graph from Google Scholar',
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={'console_scripts': ['etudier = etudier:main']},
    python_requires=">=3",
    install_requires = [
        'selenium', 
        'requests-html', 
        'networkx'
    ]
)
