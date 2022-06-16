#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 11:59:45 2022

@author: julianhamre
"""

import unittest
import date_module as dm

class TestDate(unittest.TestCase):
    def test_date_to_day_number(self):
        date_strings = ["010100", "290220", "311299"]
        correct_day_numbs = [1, 7365, 36525]

        for i in range(0, len(date_strings)):
            day_numb = dm.date(date_strings[i]).date_to_day_number()
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
            
            
if __name__ == "__main__":
    unittest.main()
