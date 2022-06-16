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
        d1 = dm.date("010100").date_to_day_number()
        d2 = dm.date("310310").date_to_day_number()
        d3 = dm.date("311299").date_to_day_number()
        
        self.assertEqual(d1, 1)
        self.assertEqual(d2, 3743)
        self.assertEqual(d3, 36525)
        
if __name__ == "__main__":
    unittest.main()