#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 
import pandas as pd 

import datetime
import matplotlib.dates as mdates

import matplotlib.pyplot as plt


class fancyplot():
    def plot_timeseries(x_values, y_values, x_formatting = 'months', xlim = None, ylim = None, title = None, y_label = None):
        fig, ax = plt.subplots(figsize = (15,4))  
        if x_formatting == 'months':

            # Set the locator
            locator = mdates.MonthLocator()  # every month
            # Specify the format - %b gives us Jan, Feb...
            fmt = mdates.DateFormatter('%b')

            X = fig.gca().xaxis
            X.set_major_locator(locator)
            # Specify formatter
            X.set_major_formatter(fmt)

            ax.plot(x_values, y_values)
            plt.xlabel(x_formatting)


        if x_formatting == 'years':
            # Set the locator
            locator = mdates.YearLocator()  # every month
            # Specify the format - %b gives us Jan, Feb...
            fmt = mdates.DateFormatter('%Y')

            X = fig.gca().xaxis
            X.set_major_locator(locator)
            # Specify formatter
            X.set_major_formatter(fmt)

            ax.plot(x_values, y_values)
            plt.xlabel(x_formatting)


        if xlim is not None:
            plt.xlim(xlim)

        if ylim is not None:
            plt.ylim(ylim)
        if title is not None: 
            plt.title(title)
        if y_label is not None: 
            plt.ylabel(y_label)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.show()


    def plot_longtail(dataframe, x_values, y_values, title = None, limit = None):
        dataframe = dataframe.sort_values(by = y_values, ascending = False)
        fig, ax = plt.subplots()  
        if limit == None:
            ax.plot(dataframe[x_values].astype(str), dataframe[y_values])
        else: 
            ax.plot(dataframe[x_values][0:limit].astype(str), dataframe[y_values][0:limit])
        plt.tick_params(
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            labelbottom=False) # labels along the bottom edge are off
        plt.xlabel(x_values)
        plt.ylabel(y_values)
        if title == None:
            plt.title("Long tail for " + y_values)
        else: 
            plt.title(title)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.show()

    def fancy_barplot(dataframe, x_values, y_values, ascending = True, limit = None, figsize = None, title = None, shiftparams = None, fancylabels = True, sort_x = False):

        if sort_x == False:
            dataframe = dataframe.sort_values(y_values, ascending = ascending)
        else: 
            dataframe = dataframe.sort_values(x_values, ascending = ascending)

        if figsize == None:
            fig, ax = plt.subplots(figsize = (8,4)) 
        else: 
            fig, ax = plt.subplots(figsize = figsize) 

        if limit == None: 
            x_val = dataframe[x_values].astype(str)
            y_val = dataframe[y_values]
        else: 
            x_val = dataframe[x_values][0:limit].astype(str)
            y_val = dataframe[y_values][0:limit]

        ax.bar(x_val, y_val)
        if fancylabels == True:

            plt.yticks([])
            if shiftparams == None:
                for i, v in enumerate(y_val):
                    ax.text(i, v , v, color = "black")
            else: 
                for i, v in enumerate(y_val):
                    ax.text(i + shiftparams[0], v + shiftparams[1] , v, color = "black")

        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        if title == None:
            plt.title("Barplot for " + x_values + " and " + y_values)
        else: 
            plt.title(title) 

        plt.xlabel(x_values)
        plt.ylabel(y_values)
        plt.show()
    
    
    