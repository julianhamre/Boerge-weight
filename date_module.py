#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 10:47:18 2022

@author: julianhamre
"""

class date():
    __year_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    __leap_year_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def __check_if_string(self):
        tp = type(self.__ddmmyy)
        if not (tp is str):
            raise TypeError(f"in {self.__ddmmyy}, date must be a string, got {tp}")
        
    def __check_length(self):
        length = len(self.__ddmmyy)
        if not length == 6:
            raise IndexError(f"in {self.__ddmmyy}, date must have 6 characters in the ddmmyy format, got {length} characters")
            
    def __correct_year_list(self):
        if self.__year_numb % 4 == 0:
            return self.__leap_year_list
        else:
            return self.__year_list
    
    def __check_day_and_month(self):
        mn = self.__month_numb 
        dn = self.__day_numb
        if not (mn >= 1 and mn <= 12):
            raise ValueError(f"in {self.__ddmmyy}, month {mn} is invalid")
        if not (dn >= 1 and dn <= self.__correct_year_list()[mn - 1]):
            raise ValueError(f"in {self.__ddmmyy}, day {dn} in month {mn} is invalid")
    
    def __init__(self, ddmmyy):
        self.__ddmmyy = ddmmyy
        
        self.__check_if_string()
        self.__check_length()
        
        self.__day_numb = int(ddmmyy[0:2])
        self.__month_numb = int(ddmmyy[2:4])
        self.__year_numb = int(ddmmyy[4:6])
        
        self.__check_day_and_month()
        
    def get_ddmmyy(self):
        return self.__ddmmyy
    
    def get_full_format(self):
        month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        year = self.__year_numb
        if year < 10:
            year = f"0{year}"
        full_format = f"{month_names[self.__month_numb - 1]} {self.__day_numb}, 20{year}"
        return full_format
        
    def date_to_day_number(self):
        year_value = 0
        for i in range(0, self.__year_numb):
            if i % 4 == 0:
                year_value += 366
            else:
                year_value += 365
            
        month_value = 0
        month_counter = 0
        for i in range(0, self.__month_numb - 1):
            month_value += self.__correct_year_list()[month_counter]
            month_counter += 1
        
        day_value = self.__day_numb
        
        return year_value + month_value + day_value 


def dates_to_days_from_first_date(dates):
    days = []
    first_date = dates[0].date_to_day_number()
    for date in dates:
        days.append(date.date_to_day_number() - first_date)
    return days
