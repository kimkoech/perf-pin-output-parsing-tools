###############################################################################
"""
Program description

Created by:	skeleton by Billy Koech
Date:		Jan 4th 2018

mru(most recent update):

"""
###############################################################################
# import modules
import re    			# for parsing lines to numbers
import numpy as np 		# for computing std and mean
import os				# for navigativn gth eos

# program variables



# user variables
pin_output_dir = "outputs/"
combined_output_file = "combined.out"

pin_specific_search_terms = ["Total number of instructions executed",\
								"Number of load instructions", \
								"Number of store instructions", \
								"Number of branch instructions"] 

# troubleshooting
debugMode = False
###############################################################################
# program functions
###############################################################################

# function to combine files into one


## source: https://www.mkyong.com/python/
# python-how-to-list-all-files-in-a-directory/

def combine_files(dir_with_files, name_for_output_file):


	# clear file first
	open(name_for_output_file, 'w+').close()
	# open in append mode
	out_f = open(name_for_output_file, "a+")

	files = []
	# r=root, d=directories, f = files
	for r, d, f in os.walk(dir_with_files):
	    for file in f:
	        # open each file
	        in_f = open(dir_with_files + file, "r")
	        
	        # troubleshooting
	        if debugMode:
	        	print(in_f)

	        # begin appending:
	        for line in in_f:
	        	out_f.write(line)


	        in_f.close()

	out_f.close()




# Main entry point for the script.
def compute_std_and_mean(stat_file, search_terms):

	runtimes = {} 		# dict to hold instruction and runtimes

	##################### EXTRACTION AND PARSING #########################
	# open file and read line by line
	f = open(stat_file, "r")

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

	header = "Type of instruction: \t std, \t mean \n"

	print(header + output_str)

	return(header + output_str)


# Main entry point for the script.
def main():
	# combine files
	combine_files(pin_output_dir, combined_output_file)

	# parse and return std
	return_str = compute_std_and_mean(combined_output_file, pin_specific_search_terms)



	# write to file
	report = open("pin_report.txt", "w+")

	report.write(return_str)
	report.close()


if __name__ == '__main__':
    main()

