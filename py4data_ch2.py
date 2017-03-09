import pandas as pd
import json
import os
import matplotlib
import numpy as np
# default dictionary, counter
from collections import defaultdict
from collections import Counter

# alternative method to open
# open(path).readline()
path = "usagov_bitly_data2012-03-16-1331923249.txt"

# list comprehension
records=[json.loads(line) for line in open(path)]
# print records[0]['tz']

# counting time zones
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
#print time_zones

def get_counts(seq):
	counts ={}
	for x in seq:
		if x in counts:
			counts[x]+=1
		else:
			counts[x]=1
	return counts

# with a default dictionary
def get_counts2(seq):
	counts = defaultdict(int)
	for x in seq:
		if x in counts:	
			counts[x]+=1
	return counts

# top 10 frequent time zones
def top_counts(count_dict,n=10):
	value_key_pairs = [(count,tz) for tz,count in count_dict.items()]
	value_key_pairs.sort()
	return value_key_pairs[-n:]

counts= get_counts(time_zones)
print top_counts(counts)

# standard library
counts2 = Counter(time_zones)
counts2.most_common(10)

# pandas
frame = pd.DataFrame(records)
tz_counts = frame['tz'].value_counts()

clean_tz = frame['tz'].fillna("Missing")
clean_tz[clean_tz==''] = 'Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:10]

#user behavior
results = Series([x.split()[0] for x in frame.a.dropna()])
results[:5]

cframe=frame[frame.a.notnull()]
# numpy array
operating_system= np.where(cframe['a'].str.contains('Windows'),'Windows', "Not Windows")
by_tz_os = cframe.groupby(['tz',operating_system])
agg_counts=by_tz_os.size().unstack().fillna(0)


'''
Movie Lens 1M Data Set Example
'''

import pandas as pd
unames = ['user_id', 'gender', 'age', 'occupation', 'zip'] users = pd.read_table('ml-1m/users.dat', sep='::', header=None, names=unames)
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ml-1m/ratings.dat', sep='::', header=None, names=rnames)
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('ml-1m/movies.dat', sep='::', header=None, names=mnames)

# merge all three dataframe into one
data = pd.merge(pd.merge(users,ratings),movies)

# get mean rating for each movie by gender 
# correct one error in the book
# mean_ratings = data.pivot_table('rating',rows='title',cols='gender',aggfunc='mean')
# "rows" should be "index", "cols" is replaced with "columns" 
mean_ratings = data.pivot_table('rating',index='title',columns='gender',aggfunc='mean')

# select movies that have at least 250 ratings
ratings_by_title = data.groupby('title').size()
active_titles = ratings_by_title.index[ratings_by_title>=250]

top_female_ratings = mean_ratings.sort_index(by='F',ascending=False)
top_female_ratings[:10]


# measure disagreement e.g. standard deviation
mean_ratings['diff'] = mean_ratings['M']-mean_ratings['F']
sorted_by_diff=mean_ratings.sort_values(by='diff')
sorted_by_diff[:10]

rating_std_by_title=data.groupby('title')['rating'].std()
