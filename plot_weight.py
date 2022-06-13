#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:01:46 2022

@author: julianhamre
"""
from matplotlib import pyplot as plt
from timeit import default_timer as tmi
import numpy as np
import sys 
import os
sys.path.append(os.path.abspath("../Polynomial"))
import poly_tools as pt


def date_to_day_number(date):
    year_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    year_number = int(date[4:6])
    year_value = 0
    for i in range(0, year_number):
        if i % 4 == 0:
            year_value += 366
        else:
            year_value += 365
        
    month_number = int(date[2:4])
    month_value = 0
    month_counter = 0
    if year_number % 4 == 0:
        for i in range(0, month_number - 1):
            month_value += leap_year_list[month_counter]
            month_counter +=1
    else:
        for i in range(0, month_number - 1):
            month_value += year_list[month_counter]
            month_counter += 1
        
    day_value = int(date[0:2])
    
    return year_value + month_value + day_value 

def all_days_from_first(dates):
    numbs = []
    first_date = date_to_day_number(dates[0])
    for date in dates:
        numbs.append(date_to_day_number(date) - first_date)
    return numbs


def remove_space(strings):
    split_strings = []
    for string in strings:
        split_strings.append(string.split())
    space_removed = []
    for i in split_strings:
        for element in i:
            if element != "":
                space_removed.append(element)
    return space_removed

            
def is_equal():
    with open("/Users/julianhamre/icloud/delt_med_julian/weight_data.txt") as f1, open("weight_control.txt") as f2:   #First path is spesificly for my computer, change when needed 
        f1 = remove_space(f1)
        f2 = remove_space(f2)
        if len(f1) != len(f2):
            print("number of elements changed in weight_data.txt")
            return False
        lncounter = 0
        for i in f1:
            if i != f2[lncounter]:
                print("changes made in weight_data.txt")
                return False
            lncounter += 1
    print("no changes detected in weight_data.txt")
    return True    
    
def plot_weight_graph():
    with open("/Users/julianhamre/icloud/delt_med_julian/weight_data.txt") as f:      #Path spesific
        lines = f.readlines()
        x = []
        y = []
        for line in lines:
            data = line.split()
            if len(data) == 2:
                x.append(data[0])
                y.append(float(data[1]))
        first_date = x[0]
    #print(f"dates: {x}")
    #print(f"weights: {y}")
    x = all_days_from_first(x)

    plt.grid(color="grey", linestyle="--")
    plt.xlabel(f"days after {first_date}")
    plt.ylabel("weight in kg")
    plt.title("Børge's weight graph")
    plt.ylim(75, 78)
    
    degree = 2
    trend = pt.polynomial(np.polyfit(x, y, degree))
    print(type(np.polyfit(x, y, degree)))
    x_trend = np.linspace(x[0], x[-1], 1000)
    plt.plot(x, y, linewidth=3, label="Weight graph")
    plt.plot(x_trend, trend.evaluate(x_trend), label=f"Trend polynomial, deg. {degree}")
    plt.legend(loc="upper left")
    
    d_trend = trend.differentiate()
    if d_trend.evaluate(x_trend[-1]) > 0:
        expected_hit = int(trend.evaluate(x[-1])) + 1
    else:
        expected_hit = int(trend.evaluate(x[-1]))
        
    trend = pt.polynomial(trend.get_coef())         #rewriting polynomial with coefficients as list (not np.narray)
    trend.add_constant(-expected_hit)
    days_to_hit = pt.pol_solve(trend, x[-1]) - x[-1]
    t = plt.text(0, 75.23, f"Børge is expected to\nweigh {expected_hit} kg in {round(days_to_hit)} days")
    t.set_bbox(dict(facecolor=[1, 0.6, 0], alpha=0.7))
    
    fig = plt.gcf()
    plt.show()
    return fig
    

def rewrite_and_upload(fig, message):
    fig.savefig("Boerge_weight_graph.pdf", format="pdf")
    os.system("cp /Users/julianhamre/icloud/delt_med_julian/weight_data.txt weight_control.txt")
    os.system(f"git commit -am '{message}'; git push")
    
def savefig_test(fig):
    fig.savefig("Graph_test_save.pdf", format="pdf")


start = tmi()


#plot_weight_graph()
#savefig_test(plot_weight_graph())

"""
if not is_equal():
    fig = plot_weight_graph()
    upload_confirmation = input("Do you want to rewrite the current graph file, weight_control.txt and upload \nthe new graph file to github?\n\nAnswer yes or no: ")
    if upload_confirmation == "yes":
        commit_message = input("Write new commit message: ")
        rewrite_and_upload(fig, commit_message)
    else:
        print("rewrite and upload cancelled")

"""
end = tmi()


#print(f"run in {round(end - start, 4)} seconds")








