#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 20:45:42 2023

@author: rwang
"""
import numpy as np
import pandas as pd
import argparse
import os
        

parser = argparse.ArgumentParser(description=''''transform stero to h5ad，author——ray''')

##########输入处理
parser.add_argument('--dict_file', help='a file can tell us key and value.key in col1;value in col2', default=r"./dict_file.txt")
parser.add_argument('--dict_sep', help='the sep of dict file', default=r"\t")
parser.add_argument('--key', help='the col of key,start at 0', default=r"0")
parser.add_argument('--value', help='the col of value,start at 0', default=r"1")
parser.add_argument('--i', help='a file can tell us input file', default=r"./input.txt")
parser.add_argument('--i_sep', help='the sep of input file', default="\t")
parser.add_argument('--col', help='which col will replace,start at 0', default=r"0")
parser.add_argument('--sep', help='the sep of replaced col', default="/")
parser.add_argument('--o', help='a file can tell us input file', default=r"./output.txt")
args = parser.parse_args()


key = int(args.key)
value = int(args.value)
dict_file = pd.read_csv(args.dict_file, sep = args.dict_sep,engine='python')
#dict_file = pd.read_csv("/Users/rwang/Desktop/example/pattern_gene/IDH_wt_pattern/Gene_ID.txt", sep = "\t")

print("key is {}".format(dict_file.columns[key]))
print("value is {}".format(dict_file.columns[value]))

dict_ = dict()

for i,j in  zip(dict_file[dict_file.columns[key]],dict_file[dict_file.columns[value]]):
    dict_[str(i)] =j
    
input_file = pd.read_csv(args.i, sep = args.i_sep,engine='python')
#input_file = pd.read_csv("/Users/rwang/Desktop/example/pattern_gene/IDH_wt_pattern/GO.csv", sep = "\t")


temp = []
for i in input_file.iloc[:,int(args.col)]:
    
    #print(i.split(args.sep))
    str_=""
    for j in i.split(args.sep):
        str_ += dict_[j]
        str_ += args.sep
    temp.append(str_.strip(args.sep))
    #print(str_.strip(args.sep))   
    #print("*"*20)
input_file.iloc[:,int(args.col)] = temp
input_file.to_csv(args.o,sep=args.i_sep, index=False)

        
    