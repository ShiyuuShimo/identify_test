import ast
import math
import csv
import sys
import os

dir_name = input('enter directory name: ')

if not os.path.isdir(dir_name):
	print('there is no ' + dir_name)
	sys.exit()

list_path = dir_name + '/list.txt'
table_path = dir_name + '/result.csv'

dr = {}

# input list.txt from subdirectory, for example, buncho, const
with open(list_path, newline='') as t:
	lines = '{'
	for line in t:
		lines = lines + t.readline() + ', '
	lines = lines.rstrip(', ') + '}'
	d = ast.literal_eval(lines)

# calculate suppressed ratio, "ratio"
x = math.floor(math.sqrt(len(d))) + 1

for n in range(1, x):

	n_num = str(n)

	for m in range(1, x):

		lz1 = d['z' + n_num + '.zip']
		lz2 = d['z' + str(m) + '.zip']
		lz_sup = d['z' + n_num + str(m) + '.zip']

		ratio = lz_sup / (lz1 + lz2)

		temp = {'r' + n_num + str(m): ratio}
		dr = {**dr, **temp}
		temp = {}

# sort and output the rank of "ratio"
dr_sorted = sorted(dr.items(), key=lambda x:x[1], reverse=True)

print(dr_sorted)

# create table of "ratio"
with open(table_path, 'w') as c:
	writer = csv.writer(c)
	for row in dr_sorted:
		writer.writerow(row)

# choice the most doubtful pairs
#if x >= 10:
#	top = dr_sorted[:x]
#else:
#	top = dr_sorted[:5]
