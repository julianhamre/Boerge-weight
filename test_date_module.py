#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 11:59:45 2022

@author: julianhamre
"""

import unittest
import date_module as dm

class TestDate(unittest.TestCase):
    def test_total_days(self):
        date_strings = ["010100", "290220", "311299"]
        correct_day_numbs = [1, 7365, 36525]

        for i in range(0, len(date_strings)):
            day_numb = dm.date(date_strings[i]).total_days()
            self.assertEqual(day_numb, correct_day_numbs[i])
    
    def test_check_if_string(self):
        with self.assertRaises(TypeError):
            dm.date(6)

    def test_check_length(self):
        with self.assertRaises(IndexError):
            dm.date("3010206")
        try: 
            dm.date("301020")
        except IndexError:
            self.fail("IndexError raised when date string had correct length")

    def test_check_day_and_month(self):
        correct_date_strings = ["101078", "310120", "290220", "310320"]
        for s in correct_date_strings:
            try:
                dm.date(s)
            except ValueError:
                self.fail("ValueError raised when date string had correct day and month")
        
        incorrect_date_strings = ["101320", "320120", "311120", "290221"]
        for s in incorrect_date_strings:
            with self.assertRaises(ValueError):
                dm.date(s)

    def test_days_from_first_date(self):
        date_strings = ["010120", "050120", "070327"]
        days = []
        for s in date_strings:
            days.append(dm.date(s))
        days_appart = dm.days_from_first_date(days)
        self.assertEqual(days_appart, [0, 4, 2622])

if __name__ == "__main__":
    unittest.main()
