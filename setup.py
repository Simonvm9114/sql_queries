import setuptools
from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sql_query",
    version="0.0.8",
    author="Simon van Meegdenburg",
    author_email="simonvm@live.nl",
    description="Build simple SQL queries fast",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Simonvm9114",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: SQL",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Topic :: Database"
    ],
    python_requires='>=3.6',
    setup_requires=['wheel']
)