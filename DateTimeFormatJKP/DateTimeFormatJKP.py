"""A test library for handling date and time formats.,

''DateTimeFormat is written to robot framework to extend the support on verifying the date formats initially,
It will be extended further according the impediments which will be faced.

This Library file is mainly used to verify the Date format in run time in robot tests,

As I came accross the scenario where there were no libraries which is made to verufy the format of Date in Robot framework
so, decided to write my very own library which will be utlized currently under my project after the succesion over there
I am uploading this to github to make every Robot framework users life in easy way.

 = Table Of Contents =

- ' Date Formats '

In the context of the library, ''date'' generally have the following meanings;

- ''date'': An entity which can be only to verify the Date format which can be in any format, and it is test oriented
library which is mainly used and focussed on comparing the base format wth the format which needs to be verifies
as part of our tests.

 Examples:
    | ${date} =       | Date Format | ${format}   | ${date_format} |

This library will do get update at Monthly basis to give an enlarge support over all the formats which can be verified.,
For now there, it is very straight forward library file but going forward, this will be updated to have a extended
support.

#   Created by @PraveenKumarK alias @JKP

#   Capgemini India - @PK18

#   e-Mail - pk292695@gmail.com


"""

from datetime import datetime

from robot.version import get_version

__version__ = get_version()
_all_ = ['date_format']





def _verify_date_format_(input_date, input_format):
    format1 = 'dd/MM/yyyy'
    format2 = 'dd MMM yyyy'
    format3 = 'MMM dd, yyyy'
    format4 = 'MMMM dd, yyyy'
    if input_format == format1:
        bool(datetime.strptime(input_date, "%d/%m/%Y"))
    elif input_format == format2:
        bool(datetime.strptime(input_date, "%d %b %Y"))
    elif input_format == format3:
        bool(datetime.strptime(input_date, "%b %d, %Y"))
    elif input_format == format4:
        bool(datetime.strptime(input_date, "%B %d, %Y"))
    else:
        return _fail(input_format, 'Not matching with any of the format available in library')


def _fail(formatdate, fail_template):
    raise AssertionError(formatdate + '  ' + fail_template)


class DateTimeFormatJKP(object):

    def date_format(self, input_date, format_date):
        """
        :param format_date:  Date which needs to be tested against
                        the given format from the argument date
        :param input_date:    Date or the format with any supported formats
                        which is basically taken as baseline here to verify
                        the date structure

        Examples:
        | ${date} =       | Date Format | ${input_date}   | ${format_date} |

        """
        return _verify_date_format_(input_date, format_date)
