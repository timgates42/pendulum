# -*- coding: utf-8 -*-

from .. import AbstractTestCase
from pendulum.parsing.parser import Parser, ParserError


class ParserTest(AbstractTestCase):

    def test_y(self):
        text = '2016'

        parsed = Parser().parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(1, parsed['month'])
        self.assertEqual(1, parsed['day'])
        self.assertEqual(0, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

    def test_ym(self):
        text = '2016-10'

        parsed = Parser().parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(10, parsed['month'])
        self.assertEqual(1, parsed['day'])
        self.assertEqual(0, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

    def test_ymd(self):
        text = '2016-10-06'

        parsed = Parser().parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(10, parsed['month'])
        self.assertEqual(6, parsed['day'])
        self.assertEqual(0, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

    def test_ymd_one_character(self):
        text = '2016-2-6'

        parsed = Parser().parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(2, parsed['month'])
        self.assertEqual(6, parsed['day'])
        self.assertEqual(0, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

    def test_ymd_day_first(self):
        text = '2016-02-06'

        parsed = Parser(day_first=True).parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(6, parsed['month'])
        self.assertEqual(2, parsed['day'])
        self.assertEqual(0, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

    def test_ymd_hms(self):
        text = '2016-10-06 12:34:56'

        parsed = Parser().parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(10, parsed['month'])
        self.assertEqual(6, parsed['day'])
        self.assertEqual(12, parsed['hour'])
        self.assertEqual(34, parsed['minute'])
        self.assertEqual(56, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

        text = '2016-10-06 12:34:56.123456'

        parsed = Parser().parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(10, parsed['month'])
        self.assertEqual(6, parsed['day'])
        self.assertEqual(12, parsed['hour'])
        self.assertEqual(34, parsed['minute'])
        self.assertEqual(56, parsed['second'])
        self.assertEqual(123456000, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

    def test_rfc_3339(self):
        text = '2016-10-06T12:34:56+05:30'

        parsed = Parser().parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(10, parsed['month'])
        self.assertEqual(6, parsed['day'])
        self.assertEqual(12, parsed['hour'])
        self.assertEqual(34, parsed['minute'])
        self.assertEqual(56, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(19800, parsed['offset'])

    def test_rfc_3339_extended(self):
        text = '2016-10-06T12:34:56.123456+05:30'

        parsed = Parser().parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(10, parsed['month'])
        self.assertEqual(6, parsed['day'])
        self.assertEqual(12, parsed['hour'])
        self.assertEqual(34, parsed['minute'])
        self.assertEqual(56, parsed['second'])
        self.assertEqual(123456000, parsed['subsecond'])
        self.assertEqual(19800, parsed['offset'])

        text = '2016-10-06T12:34:56.000123+05:30'

        parsed = Parser().parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(10, parsed['month'])
        self.assertEqual(6, parsed['day'])
        self.assertEqual(12, parsed['hour'])
        self.assertEqual(34, parsed['minute'])
        self.assertEqual(56, parsed['second'])
        self.assertEqual(123000, parsed['subsecond'])
        self.assertEqual(19800, parsed['offset'])

    def test_rfc_3339_extended_nanoseconds(self):
        text = '2016-10-06T12:34:56.123456789+05:30'

        parsed = Parser().parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(10, parsed['month'])
        self.assertEqual(6, parsed['day'])
        self.assertEqual(12, parsed['hour'])
        self.assertEqual(34, parsed['minute'])
        self.assertEqual(56, parsed['second'])
        self.assertEqual(123456789, parsed['subsecond'])
        self.assertEqual(19800, parsed['offset'])

    def test_iso_8601_date(self):
        text = '2012'

        parsed = Parser().parse(text)
        self.assertEqual(2012, parsed['year'])
        self.assertEqual(1, parsed['month'])
        self.assertEqual(1, parsed['day'])
        self.assertEqual(0, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

        text = '2012-05-03'

        parsed = Parser().parse(text)
        self.assertEqual(2012, parsed['year'])
        self.assertEqual(5, parsed['month'])
        self.assertEqual(3, parsed['day'])
        self.assertEqual(0, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

        text = '20120503'

        parsed = Parser().parse(text)
        self.assertEqual(2012, parsed['year'])
        self.assertEqual(5, parsed['month'])
        self.assertEqual(3, parsed['day'])
        self.assertEqual(0, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

        text = '2012-05'

        parsed = Parser().parse(text)
        self.assertEqual(2012, parsed['year'])
        self.assertEqual(5, parsed['month'])
        self.assertEqual(1, parsed['day'])
        self.assertEqual(0, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

        text = '201205'

        parsed = Parser().parse(text)
        self.assertEqual(2012, parsed['year'])
        self.assertEqual(5, parsed['month'])
        self.assertEqual(1, parsed['day'])
        self.assertEqual(0, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

    def test_iso8601_datetime(self):
        text = '2016-10-01T14'

        parsed = Parser().parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(10, parsed['month'])
        self.assertEqual(1, parsed['day'])
        self.assertEqual(14, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

        text = '2016-10-01T14:30'

        parsed = Parser().parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(10, parsed['month'])
        self.assertEqual(1, parsed['day'])
        self.assertEqual(14, parsed['hour'])
        self.assertEqual(30, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

        text = '20161001T14'

        parsed = Parser().parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(10, parsed['month'])
        self.assertEqual(1, parsed['day'])
        self.assertEqual(14, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

        text = '20161001T1430'

        parsed = Parser().parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(10, parsed['month'])
        self.assertEqual(1, parsed['day'])
        self.assertEqual(14, parsed['hour'])
        self.assertEqual(30, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

        text = '20161001T1430+0530'

        parsed = Parser().parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(10, parsed['month'])
        self.assertEqual(1, parsed['day'])
        self.assertEqual(14, parsed['hour'])
        self.assertEqual(30, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(19800, parsed['offset'])

        text = '20161001T1430,4+0530'

        parsed = Parser().parse(text)
        self.assertEqual(2016, parsed['year'])
        self.assertEqual(10, parsed['month'])
        self.assertEqual(1, parsed['day'])
        self.assertEqual(14, parsed['hour'])
        self.assertEqual(30, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(400000000, parsed['subsecond'])
        self.assertEqual(19800, parsed['offset'])

        text = '2008-09-03T20:56:35.450686+01'

        parsed = Parser().parse(text)
        self.assertEqual(2008, parsed['year'])
        self.assertEqual(9, parsed['month'])
        self.assertEqual(3, parsed['day'])
        self.assertEqual(20, parsed['hour'])
        self.assertEqual(56, parsed['minute'])
        self.assertEqual(35, parsed['second'])
        self.assertEqual(450686000, parsed['subsecond'])
        self.assertEqual(3600, parsed['offset'])

    def test_iso8601_week_number(self):
        text = '2012-W05'

        parsed = Parser().parse(text)
        self.assertEqual(2012, parsed['year'])
        self.assertEqual(1, parsed['month'])
        self.assertEqual(30, parsed['day'])
        self.assertEqual(0, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

        text = '2012W05'

        parsed = Parser().parse(text)
        self.assertEqual(2012, parsed['year'])
        self.assertEqual(1, parsed['month'])
        self.assertEqual(30, parsed['day'])
        self.assertEqual(0, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

        text = '2012-W05-5'

        parsed = Parser().parse(text)
        self.assertEqual(2012, parsed['year'])
        self.assertEqual(2, parsed['month'])
        self.assertEqual(3, parsed['day'])
        self.assertEqual(0, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

        text = '2012W055'

        parsed = Parser().parse(text)
        self.assertEqual(2012, parsed['year'])
        self.assertEqual(2, parsed['month'])
        self.assertEqual(3, parsed['day'])
        self.assertEqual(0, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

    def test_iso8601_ordinal(self):
        text = '2012-007'

        parsed = Parser().parse(text)
        self.assertEqual(2012, parsed['year'])
        self.assertEqual(1, parsed['month'])
        self.assertEqual(7, parsed['day'])
        self.assertEqual(0, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

        text = '2012007'

        parsed = Parser().parse(text)
        self.assertEqual(2012, parsed['year'])
        self.assertEqual(1, parsed['month'])
        self.assertEqual(7, parsed['day'])
        self.assertEqual(0, parsed['hour'])
        self.assertEqual(0, parsed['minute'])
        self.assertEqual(0, parsed['second'])
        self.assertEqual(0, parsed['subsecond'])
        self.assertEqual(None, parsed['offset'])

    def test_iso8601_ordinal_invalid(self):
        text = '2012-007-05'

        self.assertRaises(ParserError, Parser().parse, text)


    def test_invalid(self):
        text = '201610T'

        self.assertRaises(ParserError, Parser().parse, text)
