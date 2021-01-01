#!/depot/Python-2.7.9/bin/python
import re
input_file = 'netlist.txt'
with open(input_file,"r") as f:
    data = f.read()

data = re.sub(r'^\*.*', "", data)

#print(data)

subckt_list=[]
with open(input_file,"r") as f:
  for line in f:
   match = re.findall(r'^.subckt\s(\S+)\s.*$',line)
	#print(match)
   if len(match)==1:
     subckt_list.append(match[0])
		    		
print(subckt_list)


	 
first=subckt_list[-1]

print(first)




output_file ='flat_netslit.sp'
with open(output_file, "w") as f:
    f.write(data)



with open('netlist.txt') as infile, open('flat_netlist_all.sp', 'a') as outfile:
    copy = False
    for line in infile:
      if any(".subckt "+word in line for word in subckt_list):
            copy = True
      elif any(".ends "+word in line for word in subckt_list):
          copy = False
      elif copy:
          outfile.write(line)


	
		
		


"""
with open('cdl_netlist.sp') as infile, open('flat_netlist_all.sp', 'w') as outfile:
    copy = False
    for line in infile:
        if line.strip() == ".subckt tx_vdriver_mos_drv a drv_en drv_en_n gd n p vreg_tx_drv":
            copy = True
        elif line.strip() == ".ends tx_vdriver_mos_drv":
            copy = False
        elif copy:
            outfile.write(line)
"""
