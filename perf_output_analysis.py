###############################################################################
"""
Program description

Created by:	skeleton by Billy Koech
Date:		Jan 4th 2018

mru(most recent update):
Sept 24th 2019
Std and mean calculator for perf and pin outputs

"""
###############################################################################
# import modules
import re    			# for parsing lines to numbers
import numpy as np 		# for computing std and mean

# program variables
runtimes = {} 		# dict to hold instruction and runtimes


# user variables
perf_output_file = "measure.out"

search_terms = ["mem_inst_retired.all_loads:u",\
				"instructions:u", \
				"mem_inst_retired.all_stores:u", \
				"br_inst_retired.all_branches:u"] 

# troubleshooting
debugMode = False
###############################################################################
# program functions
###############################################################################


# Main entry point for the script.
def main():


	##################### EXTRACTION AND PARSING #########################
	# open file and read line by line
	f = open(perf_output_file, "r")

	# initialize dict with search terms and empty list
	for term in search_terms:
		runtimes.update({term:[]})

	if debugMode:
		print(runtimes)

	# iterate over each line in ouput file
	for line in f:

		# search for the search_terms in each line
		for term in search_terms:
			if term in line:
				# extract number and update runtime dict
				numeric_value = int(re.findall("\d+", line)[0])
				if debugMode:
					print(numeric_value)

				runtimes[term].append(numeric_value)

				#print(term + " -->> " + str(numeric_value))

	print("Parsing complete!")
	f.close()

	################# STD and MEAN Computation ###########################

	output_str = ""

	# use numpy to find std and mean:
	for key in runtimes.keys():
		# compute std and append to list in output dict
		std = np.std(runtimes[key])
		mean = np.mean(runtimes[key])

		# write to string and print
		output_str += key + " :\t" + str(std) +  ",\t" + str(mean) + "\n"

	header = "Type of instruction: \t std, \t mean\n"
	print(header + output_str)

	# write to file
	report = open("perf_report.txt", "w+")
	report.write(header + output_str)
	report.close()



if __name__ == '__main__':
    main()