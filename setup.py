"""Setup script for dqutils (Dragon Quest Utilities) package."""

from setuptools import setup, find_packages
import sys

# Write the version information.
# pylint: disable=import-error,invalid-name
sys.path.insert(0, 'dqutils')
import release
version = release.write_versionfile()
sys.path.pop(0)

setup(
    name=release.NAME,
    version=version,
    #maintainer=,
    #maintainer_email=,
    author=release.AUTHOR,
    author_email=release.AUTHOR_EMAIL,
    description=release.DESCRIPTION,
    keywords=release.KEYWORDS,
    #long_description=,
    license=release.LICENSE,
    platforms=release.PLATFORMS,
    url=release.URL,
    download_url=release.DOWNLOAD_URL,
    classifiers=release.CLASSIFIERS,

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
    # see http://docs.python.org/3.4/distutils/setupscript.html
    # #installing-additional-files
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('sample', ['sample/+.*.xml'])],
    )
