# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:41:51 2022

@author: Administrator
"""
import argparse
parser = argparse.ArgumentParser(description='fasta index——ray')
parser.add_argument('--input', help='Path to input file.', default=r"C:\Users\Administrator\Desktop\curated.FINAL.fasta")
parser.add_argument('--output', help='Path to output file.', default=r"C:\Users\Administrator\Desktop\result.txt")
parser.add_argument('--start', help='start position', default="0")
parser.add_argument('--end', help='end position', default="-1")
args = parser.parse_args()

with open(args.input,"r") as f:
    f=f.read()
    f=f.split(">")
    f=list(map(lambda x:">"+x,f))
with open(args.output,"w") as t:
    t.writelines(f[eval(args.start):eval(args.end)+1])

