#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:38:23 2021

@author: simranchathanat
"""
import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_excel('/Users/Simran/Desktop/temptest-5/SAMPLE 1Trace 0.xlsx')
time = file ['Time (s)']
voltage = file['Channel 1 (Vdc)']

voltage.loc[voltage==voltage.max()]
#voltage.plot()

cmds.align(x='mid')
# align the selected objects to the mid-point in x of the first select object
cmds.align(x='mid', alignToLead=True)
# 	