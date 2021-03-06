#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 10:47:18 2022

@author: julianhamre
"""

class date():
    year_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def check_if_string(self):
        tp = type(self.date)
        if not (tp is str):
            raise TypeError(f"in {self.date}, date must be a string, got {tp}")
        
    def check_length(self):
        length = len(self.date)
        if not length == 6:
            raise IndexError(f"in {self.date}, date must have 6 characters in the ddmmyy format, got {length} characters")
            
    def correct_year_list(self):
        if self.year_numb % 4 == 0:
            return self.leap_year_list
        else:
            return self.year_list
    
    def check_day_and_month(self):
        mn = self.month_numb 
        dn = self.day_numb
        if not (mn >= 1 and mn <= 12):
            raise ValueError(f"in {self.date}, month {mn} is invalid")
        if not (dn >= 1 and dn <= self.correct_year_list()[mn - 1]):
            raise ValueError(f"in {self.date}, day {dn} in month {mn} is invalid")
    
    def __init__(self, date):
        self.date = date
        
        self.check_if_string()
        self.check_length()
        
        self.day_numb = int(date[0:2])
        self.month_numb = int(date[2:4])
        self.year_numb = int(date[4:6])
        
        self.check_day_and_month()
        
        
    def date_to_day_number(self):
        year_value = 0
        for i in range(0, self.year_numb):
            if i % 4 == 0:
                year_value += 366
            else:
                year_value += 365
            
        month_value = 0
        month_counter = 0
        for i in range(0, self.month_numb - 1):
            month_value += self.correct_year_list()[month_counter]
            month_counter += 1
        
        day_value = self.day_numb
        
        return year_value + month_value + day_value 


def dates_to_days_from_first_date(dates):
    days = []
    first_date = dates[0].date_to_day_number()
    for date in dates:
        days.append(date.date_to_day_number() - first_date)
    return days
