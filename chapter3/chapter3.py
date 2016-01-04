#chapter3
import numpy as np
import scipy as sp
import os
#bag of word
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(min_df=1)

#find the most relavant post to "imaging databases"
DIR = os.path.join("/Users/ClarkSong/Desktop/pythonML/chapter3")
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


#iterate all post and find the nearest
best_doc = None
best_dist = sys.maxint
best_i = None
for i in range(0, num_samples):
	post= posts[i]
	#skip the post itself
	if post = new_post:
		continue
	post_vec = X_train.getrow(i)
	cur_dist = dist_raw(new_post_vec,post_vec)
	if cur_dist < best_dist:
		best_dist = cur_dist
		best_i = i
		best_doc = posts[i]
