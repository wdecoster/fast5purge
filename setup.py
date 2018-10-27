# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
exec(open('fast5purge/version.py').read())

setup(
    name='fast5purge',
    version=__version__,
    description='Remove sensible content from a fast5 file or directory',
    long_description=open(path.join(here, "README.md")).read(),
    long_description_content_type="text/markdown",
    url='https://github.com/wdecoster/fast5purge',
    author='Wouter De Coster',
    author_email='decosterwouter@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='nanopore',
    packages=find_packages(),
    python_requires='>=3',
    install_requires=['ont_fast5_api', ],
    package_data={'fast5purge': []},
    package_dir={'fast5purge': 'fast5purge'},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'fast5purge=fast5purge.fast5purge:main',
        ],
    },
)
