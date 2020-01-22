import os
import subprocess

mol2directory = "/Users/guowei/Code/benchmarksets/input_files/cd-set1/mol2/"
sdfdirectory= "/Users/guowei/Code/benchmarksets/input_files/cd-set1/newsdf/"

for filename in os.listdir(mol2directory):
	# print(filename)
	command = "convert.py " + mol2directory + filename + " " + sdfdirectory + filename.split(".")[0] + ".sdf"
	subprocess.call(command)