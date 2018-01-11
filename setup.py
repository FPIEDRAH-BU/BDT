from distutils.core import setup

setup(
    name='BDT',
    version='0.1.0',
    author='Franciscp J. Piedrahita',
    author_email='fpiedrah93@gmail.com',

    packages=['bdt', 'tests'],
    url='https://github.com/fpiedrah/BDT',

    license='LICENSE',
    description='Simple library to write decision trees',
    long_description=open('README.md').read(),

    install_requires=[
        "pytest == 3.3.2",
        "boolexp == 0.1"
    ],
)
