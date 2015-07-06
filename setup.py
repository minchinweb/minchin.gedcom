import os
import re
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

base_dir = os.path.dirname(os.path.abspath(__file__))

def get_version(filename="minchin/gedcom/__init__.py"):
    with open(os.path.join(base_dir, filename), encoding="utf-8") as initfile:
        for line in initfile.readlines():
            m = re.match("__version__ *= *['\"](.*)['\"]", line)
            if m:
                return m.group(1)

setup(
    name = 'minchin.gedcom',
    version = get_version(),
    description = 'A simple Python GEDCOM parser',
    long_description = "\n\n".join([open(os.path.join(base_dir, "README.rst")).read(), open(os.path.join(base_dir,"CHANGELOG.rst")).read()]),
    keywords='gedcom, genealogy',
    author='W. Minchin',
    author_email='w_minchin@hotmail.com',
    url='https://github.com/dijxtra/simplepyged/',
    packages=find_packages(),
    namespace_packages = ['minchin'],
    include_package_data = True,
    license='GPL 2+',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Sociology :: Genealogy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
)

