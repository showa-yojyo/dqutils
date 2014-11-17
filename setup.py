# -*- coding: utf-8 -*-
"""Setup script for dqutils (Dragon Quest Utilities) package."""

from setuptools import setup, find_packages
import sys

# Write the version information.
sys.path.insert(0, 'dqutils')
import release
version = release.write_versionfile()
sys.path.pop(0)

setup(
    name='dqutils',

    # Versions should comply with PEP440.
    version=version,

    description='dqutils (Dragon Quest Utilities)',
    #long_description=description,

    # The project's main homepage.
    url='https://github.com/showa-yojyo/dqutils',

    # Author details.
    author='プレハブ小屋',
    author_email='yojyo@hotmail.com',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for.
        'Intended Audience :: Other Audience',
        'Topic :: Utilities',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.4',],

    # What does your project relate to?
    keywords='DRAGON QUEST SNES',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # Use MANIFEST.in during install where we specify additional files.
    include_package_data=True,

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'dqutils': ['*.xml', 'sample/*.xml'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages.
    # see http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('sample', ['sample/+.*.xml'])],
    )
