# setup.py is a module used to build and distribute Python packages

from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

SRC_REPO = 'src'
AUTHOR = 'gdharanidharan'
REPO_NAME = 'industry_template'
AUTHOR_EMAIL = 'gdharanidharan07@gmail.com'
VERSION = '0.0.1'
DESCRIPTION = 'This is our first release'
LIST_OF_REQUIREMENTS = []

setup(
    name = SRC_REPO,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION ,
    long_description=long_description,
    url = f"https://github.com/{AUTHOR}/{REPO_NAME}",
    author_email = AUTHOR_EMAIL,
    packages=SRC_REPO,
    python_requires='>=3.6',
    install_requires = LIST_OF_REQUIREMENTS
)

