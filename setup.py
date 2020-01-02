##############################################################################
#
# Working on copyrights

#
# # Version 0.2 (JKP).  A copy of the JKP should accompany this distribution.
# THIS Library IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################


from setuptools import find_packages
from setuptools import setup

version = '0.1.7'
Readme = 'A library file for Robot framework, It is a common library which can be ' \
'supported by robot framework. Please be cautious that this library is been only used to verify the date' \
' formats and also this library is still in development for worldwide usage but this has been distributed to' \
    'use across my current project --- stay tuned for more updates '\
' Connect with me via LInkedin: https://www.linkedin.com/in/pk296/'


setup(
    name='DateTimeFormatJKP',
    version=version,
    license='apache 2.0 Software License',
    description='Library for robot framework',
    author='Praveen Kumar Kanagaraj',
    author_email='pk292695@gmail.com',
    url='https://github.com/praveenjkp/DateFormat',
    long_description=Readme,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        "Environment :: Web Environment",
        'Framework :: Robot Framework :: Library',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    packages=['DateTimeFormatJKP'],
    download_url='https://github.com/praveenjkp/DateFormat',
    python_requires='>= 2.7.10',
    install_requires=[
        'robotframework >= 2.8.7',
        'robotframework-selenium2library >= 1.7.4'
    ],
    include_package_data=False,
    zip_safe=False
)
