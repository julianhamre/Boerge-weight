#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:01:46 2022

@author: julianhamre
"""
from matplotlib import pyplot as plt
import numpy as np
import sys 
import os
sys.path.append(os.path.abspath("../Polynomial"))
import poly_tools as pt
import date_module as dm


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
        
def is_equal(path1, path2):
    with open(path1) as f1, open(path2) as f2:    
        f1 = remove_space(f1.readlines())
        f2 = remove_space(f2.readlines())
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

def is_sorted(d_numbs):
    return all(d_numbs[i] <= d_numbs[i+1] for i in range(len(d_numbs) - 1))
    
def plot_weight_graph():
    with open("/Users/julianhamre/icloud/delt_med_julian/weight_data.txt") as f:      #Path specific
        lines = f.readlines()
        x = []
        y = []
        for line in lines:
            data = line.split()
            if len(data) == 2:
                x.append(dm.date(data[0]))
                y.append(float(data[1]))
        first_date = x[0].date
    x = dm.dates_to_days_from_first_date(x)

    if not is_sorted(x):
        raise ValueError("dates are not in chronological order")

    plt.grid(color="grey", linestyle="--")
    plt.xlabel(f"days after {first_date}")
    plt.ylabel("weight in kg")
    plt.title("Børge's weight graph")
    plt.ylim(75, 78)
    
    degree = 2
    trend = pt.polynomial(np.polyfit(x, y, degree).tolist())
    x_trend = np.linspace(x[0], x[-1], 1000)
    plt.plot(x, y, linewidth=3, label="Weight graph")
    plt.plot(x_trend, trend.evaluate(x_trend), label=f"Trend polynomial, deg. {degree}")
    plt.legend(loc="upper left")
    
    d_trend = trend.differentiate()
    if d_trend.evaluate(x_trend[-1]) > 0:
        expected_hit = int(trend.evaluate(x[-1])) + 1
    else:
        expected_hit = int(trend.evaluate(x[-1]))
             
    trend.add_constant(-expected_hit)
    days_to_hit = pt.pol_solve(trend, x[-1]) - x[-1]
    t = plt.text(0, 75.23, f"Børge is expected to\nweigh {expected_hit} kg in {round(days_to_hit)} days")
    t.set_bbox(dict(facecolor=[1, 0.6, 0], alpha=0.7))
    
    fig = plt.gcf()
    plt.show()
    return fig
    

def rewrite_and_upload(fig, message):
    fig.savefig("weight_graph.pdf", format="pdf")
    os.system("cp /Users/julianhamre/icloud/delt_med_julian/weight_data.txt weight_control.txt")               #Path specific
    os.system(f"git add weight_graph.pdf; git add weight_control.txt; git commit -m '{message}'; git push")
    
def savefig_test(fig):
    fig.savefig("Graph_test_save.pdf", format="pdf")

def check_and_run():
    if not is_equal("/Users/julianhamre/icloud/delt_med_julian/weight_data.txt", "weight_control.txt"):             #Path specific
        fig = plot_weight_graph()
        upload_confirmation = input("Do you want to rewrite the current graph file, weight_control.txt and upload the new graph file to github?\n\nAnswer yes or no: ")
        if upload_confirmation == "yes":
            commit_message = "new measurement"
            rewrite_and_upload(fig, commit_message)
        else:
            print("rewrite and upload cancelled")

plot_weight_graph()
#savefig_test(plot_weight_graph())

if __name__ == "__main__":
    check_and_run()
