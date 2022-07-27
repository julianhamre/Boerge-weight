#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:01:46 2022

@author: julianhamre
"""
from matplotlib import pyplot as plt
import matplotlib.offsetbox as offsetbox

import numpy as np
import copy
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
        for i in f1:   # set range loop later
            if i != f2[lncounter]:
                print("changes made in weight_data.txt")
                return False
            lncounter += 1
    print("no changes detected in weight_data.txt")
    return True    


class trend:
    
    def __init__(self, x_values, y_values):
        self.__line_x = np.linspace(x_values[0], x_values[-1], 1000)
        self.__degree = 2
        self.__poly = pt.polynomial(np.polyfit(x_values, y_values, self.__degree).tolist())
    
    def get_poly_degree(self):
        return self.__degree
    
    def get_line_points(self):
        y = self.__poly.evaluate(self.__line_x)
        return [self.__line_x, y]
    
    def current_weight(self):
        return self.__poly.evaluate(self.__line_x[-1])
    
    def __next_expected_whole_kg(self):
        diff_poly = self.__poly.differentiate()
        next_kg = int(self.current_weight())
        if diff_poly.evaluate(self.__line_x[-1]) > 0:
            next_kg += 1
        
        return next_kg

    def __estimated_days_until_whole_kg(self):
        poly = copy.copy(self.__poly)
        poly.add_constant(- self.__next_expected_whole_kg())
        days_until_weight = pt.pol_solve(poly, self.__line_x[-1]) - self.__line_x[-1]
        
        return days_until_weight
    
    def expected_weight_information(self):
        days_remaining = round(self.__estimated_days_until_whole_kg())
        upcomming_weight = self.__next_expected_whole_kg()
        return f"Børge is expected to\nweigh {upcomming_weight} kg in {days_remaining} days"
    

class plot:
    __weight_data = "/Users/julianhamre/icloud/delt_med_julian/weight_data.txt"
    
    def get_weight_data_path(self):
        return self.__weight_data
    
    def __init__(self):
        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot()
        
        self.__set_point_values()
        self.__set_layout()
        self.__plot_data_graph()
        self.__plot_trend_elements()
        self.__ax.legend(loc="upper left")
    
    def __is_sorted(self, numbs):
        return all(numbs[i] <= numbs[i+1] for i in range(len(numbs) - 1))
    
    def __set_point_values(self):
        with open(self.__weight_data) as f:      
            lines = f.readlines()
            x = []
            y = []
            for line in lines:
                data = line.split()
                if len(data) == 2:
                    x.append(dm.date(data[0]))
                    y.append(float(data[1]))
    
            self.__first_date = x[0]
            self.__current_date = x[-1]
            
        x = dm.days_from_first_date(x)
        if not self.__is_sorted(x):
            raise ValueError("dates are not in chronological order")

        self.__x = x
        self.__y = y
        
    def __set_layout(self):
        self.__ax.grid(color="grey", linestyle="--")
        self.__ax.set_xlabel(f"days after {self.__first_date.get_full_format()}")
        self.__ax.set_ylabel("weight in kg")
        self.__ax.title.set_text("Børge's weight graph")
        self.__ax.set_ylim(74.8, 78)
    
    def __plot_data_graph(self):
        self.__ax.plot(self.__x, self.__y, linewidth=2, label="Weight graph")
    
    def __plot_trend_elements(self):
        tr = trend(self.__x, self.__y)
        line_points = tr.get_line_points()
        self.__ax.plot(line_points[0], line_points[1], label=f"Trend polynomial, deg. {tr.get_poly_degree()}")
        
        current_weight = f"Current weight is {round(tr.current_weight(), 1)}\nkg on {self.__current_date.get_full_format()}"
        box1 = offsetbox.AnchoredText(current_weight, loc=1)
        box1.patch.set(color=[1, 0.6, 0], alpha=0.8)
        
        expected_weight = tr.expected_weight_information()
        box2 = offsetbox.AnchoredText(expected_weight, loc=3)
        box2.patch.set(color=[1, 0.6, 0], alpha=0.8)
        
        self.__ax.add_artist(box2)
        self.__ax.add_artist(box1)
        
    def get_fig(self):
        return self.__fig
    

def savefig_test(plot):
    fig = plot.get_fig()
    fig.savefig("Graph_test_save.pdf", format="pdf")

def rewrite_plot(plot):
    fig = plot.get_fig()
    fig.savefig("weight_graph.pdf", format="pdf")

def rewrite_and_upload(plot, message):
    rewrite_plot(plot)
    os.system(f"cp {plot.get_weight_data_path()} weight_control.txt")               
    os.system(f"git add weight_graph.pdf; git add weight_control.txt; git commit -m '{message}'; git push")

def check_and_commit_new_measurement():
    pl = plot()
    if not is_equal(pl.get_weight_data_path(), "weight_control.txt"):
        plt.show()
        upload_confirmation = input("Do you want to rewrite the current graph file and weight_control.txt, commit and upload the files to github?\n\nAnswer yes to continue: ")
        if upload_confirmation == "yes":
            commit_message = "new measurement"
            rewrite_and_upload(pl, commit_message)
        else:
            print("rewrite and upload cancelled")

if __name__ == "__main__":
    check_and_commit_new_measurement()

