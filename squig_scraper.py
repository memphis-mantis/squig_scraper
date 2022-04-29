# include start_color and end_color -- grab fields from features (as opposed to traits)
# scrape the animation_url and append to end of table

import requests
import json
import pandas as pd
import csv
import time

squig_count = 9305 # currently 9305 squigs minted, as of 2022-04-05
columns = ['token_id', 'type', 'height', 'segments', 'spectrum', 'color_spread', 'steps_between', 'color_direction']
values_list = []

for squig in range(0, squig_count):
	url = "https://token.artblocks.io/" + str(squig)
	r = requests.get(url) # returns a requests.Response object
	squig_dict = r.json() # Returns a dictionary of the result
	values = []
	for i in squig_dict.items(): #squig_dict.items() is an iterable of tuples
		if i[0] == 'tokenID':
			values.append(i[1])
		if i[0] == 'traits':
			for trait in i[1]: # each trait is a dictionary: {'trait_type': 'Chromie Squiggle', 'value': 'All Chromie Squiggles'}
				if trait['value'] != 'All Chromie Squiggles':
					extract_value = trait['value'].split(': ') # split the field_name and values
					values.append(extract_value[1])
			values_list.append(values)
	print('squig #' + str(squig) + ' completed at: ' + str(time.ctime(time.time())))

df = pd.DataFrame(data=values_list, columns=columns)
df.to_csv('squig_scraper_output.csv')