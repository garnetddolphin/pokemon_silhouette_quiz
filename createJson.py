import glob
import os
import json

os.chdir('/path/to/dir/pokequiz/gray/')

index = 0
file_list = sorted(glob.glob('*.png'))
data = {}
for i in range(len(file_list)):
	data[i+1] = {
		"image": file_list[i],
		"name": ""
	}

os.chdir('~/pokequiz/')
name_json = open('name.json', 'w')
json.dump(data, name_json, indent=2)
