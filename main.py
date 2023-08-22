import csv
import glob
import os
import re
import time

my_path = r"D:\Intern_problems\et3_Problem_1\dairies"
new_path = r"D:\Intern_problems\et3_Problem_1\Images"
my_data = []

# get all images
files = glob.glob(my_path + '/**/*.JPG', recursive=True)

# copy each image to the new path
for file in files:
    filename = os.path.basename(file)
    os.rename(file, new_path + '/' + filename)

# get the required data of each image
for pic_name in os.listdir(new_path):
    row = []
    c_time = os.path.getmtime(new_path + '/' + pic_name)
    local_time = time.ctime(c_time)
    row.append(re.findall('-(.*)', pic_name)[0])
    row.append(str(round(os.path.getsize(new_path + '/' + pic_name) / 1024.0, 1)) + ' Kb')
    row.append(local_time)
    my_data.append(row)

# create a csv and save the data in it
with open("D:\Intern_problems\et3_Problem_1\dairies.csv", "w", newline="") as file_writer:
    fields = ["Image name", "Image size", "Image last modification date"]
    writer = csv.writer(file_writer)
    writer.writerow(fields)
    writer.writerows(my_data)
