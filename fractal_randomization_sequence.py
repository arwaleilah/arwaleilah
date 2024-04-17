import random
import csv

# Define the inputs
mylist = ["2.1", "2.2", "2.3", "2.5", "2.7"]

# Number of lists to generate
num_lists = 60

# use a for loop to generate 60 random lists and export into csv
csv_file = "randomization_sequence.csv"

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ID"] + [f"Scene {i+1}" for i in range(len(mylist))])
    
    for i in range(num_lists):
    	# Create ID column
    	id_value = 100 + i + 1
    	randomized_list = random.sample(mylist, len(mylist))
    	print(f"ID: {id_value}, Randomized List { i +1}: {randomized_list}")
    	writer.writerow([id_value] + randomized_list)

print(f"CSV file '{csv_file}' has been created.")
