#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 23:07:30 2022

@author: julianhamre
"""

import unittest
import os
import plot_weight as pw

class TestTxtCompare(unittest.TestCase):
    n1 = "equal_test_1.txt"
    n2 = "equal_test_2.txt"
    
    def create_files(self, mode1, mode2):
        f1 = open(self.n1, mode1)
        f2 = open(self.n2, mode2)
        return [f1, f2]
    
    def edit_file_2(self, text):
        f = open(self.n2, "a")
        f.write(text)
        f.close()
    
    def setUp(self):
        files = self.create_files("w", "w")
        text = "123456 70.3\n654321 72.5"
        for f in files:
            f.write(text)
            f.close()
        
    def test_is_equal(self):
           self.edit_file_2("   ")
           self.assertTrue(pw.is_equal(self.n1, self.n2))
           self.edit_file_2("\n   ")
           self.assertTrue(pw.is_equal(self.n1, self.n2))
           self.edit_file_2("123456 70.0")
           self.assertFalse(pw.is_equal(self.n1, self.n2))
       
    def tearDown(self):
        for n in [self.n1, self.n2]:
            os.remove(n)

if __name__ == "__main__":
    unittest.main()
    
