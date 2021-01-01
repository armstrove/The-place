# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 21:30:09 2018

@author: A
"""


import sys
import re
from pprint import pprint

def rename_pins_in_line_by_model(line):
    pass

def get_flat(name,pins_from_above=[],parent_name=""):
    
    body=subckt_dict[name]['body']
    
    if len(pins_from_above) != 0:
        
    
    print(body)
    output_body=""
    for line in body.split("\n"):
        print(line)
        if re.search(r'^X\w+.*(\w+)$',line):
            print("get_flat ")
            output_body="get_flat\n"
            pass
        rename_pins_in_line_by_model(line)
        

    pass
    
models={}
models["rmres"]={}
models["rmres"]["number_of_pins"]=2
models["rmres"]["seacrh_pattern"]='r\w+'

models["lvtpfet"]={}
models["lvtpfet"]["number_of_pins"]=4
models["lvtpfet"]["seacrh_pattern"]='M\w+'

models["lvtnfet"]={}
models["lvtnfet"]["number_of_pins"]=4
models["lvtnfet"]["seacrh_pattern"]='M\w+'

pprint(models)
for i in models:
    print(i)
   
top_name="tx_vdriver_pair_full"
top_name="tx_1"    
    
    
input_file = 'netlist.txt'
with open(input_file,"r") as f:
    data = f.read()




data = re.sub(r'^\*.*\n', "", data, flags=re.MULTILINE)
#print(data)
subckt_dict={}
subckts=re.finditer(r"""\.subckt\s+\w+(.*?)\n(.*?)\.ends\s+(\w+)""",data, re.DOTALL | re.VERBOSE)
for subckt in subckts: 
   subckt_name=subckt.group(3)   
   subckt_body=subckt.group(2)
   subckt_pins=subckt.group(1)
   print(subckt_name)
   subckt_dict[subckt_name]={}
   subckt_dict[subckt_name]['body']=subckt_body
   subckt_dict[subckt_name]['pins']=subckt_pins
   print(subckt.group(0))

pprint(subckt_dict)
flat_netlist=get_flat(top_name)    
print(flat_netlist)    

        