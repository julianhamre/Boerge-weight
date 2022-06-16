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
            self.assertEqual(dm.date(date_strings[i]).date_to_day_number(), correct_day_numbs[i])
        
if __name__ == "__main__":
    unittest.main()
    
