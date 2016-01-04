#chapter3
import numpy as np
import scipy as sp
import os

#bag of word
from sklearn.feature_extraction.text import CountVectorizer

#minimum count is 1, separate stop words
vectorizer = CountVectorizer(min_df=1, stop_words='english')

#find the most relavant post to "imaging databases"
DIR = r"/Users/ClarkSong/Desktop/pythonML/chapter3/posts"
posts = [open(os.path.join(DIR,f)).read() for f in os.listdir(DIR)]
X_train = vectorizer.fit_transform(posts)

num_samples, num_features = X_train.shape
print("#sample: %d, #features: %d" % (num_samples, num_features))

#new post
new_post  = "imaging databases"
new_post_vec = vectorizer.transform([new_post])

#distance function
def dist_raw(v1,v2):
	delta = v1-v2
	return sp.linalg.norm(delta.toarray())

#normalized distance
def dist_norm(v1,v2):
	v1_normalized = v1/sp.linalg.norm(v1.toarray())
	v2_normalized = v2/sp.linalg.norm(v2.toarray())
	delta = v1_normalized - v2.normalized 
	return sp.linalg.norm(delta.toarray())


#iterate all post and find the nearest
best_doc = None
best_dist = sys.maxint
best_i = None
for i in range(0, num_samples):
	post= posts[i]
	#skip the post itself
	if post == new_post:
		continue
	post_vec = X_train.getrow(i)
	cur_dist = dist_raw(new_post_vec,post_vec)
	if cur_dist < best_dist:
		best_dist = cur_dist
		best_i = i
		best_doc = posts[i]


#Clustering K-Means
vectorizer2 = StemmedTfidVectorizer(min_df=10,max_df=0.5,stop_words='english',charset_error='ignore')
vectorized = vectorizer2.fit_transform(dataset.data)
num_cluster = 50
from sklearn.cluster import KMeans
km = KMeans(n_cluster=num_cluster, init='random', n_init=1,verbose=1)
km.fit(vectorized)

