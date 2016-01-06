＃chapter5
#fetch data
def fetch_posts():
	for line in open("data.tsv","r"):
		post_id,text = line.split("\t")
		yield int(post_id),test_strip()

all_answers = [q for q,v in meta.iteritems() if v['ParentID']!=-1]
Y = np.asarray([meta[aid]['Score']>0 for aid in all_answers])

#kNN 
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier(n_beighbors=2)
print(knn)

knn.fit([[1],[2],[3],[4],[5],[6]],[0,0,0,1,1,1])
knn.predict(1.5)
knn.predict(37)
knn.predict(3)

#to get the class probability, use predict_proba()
knn.predict_proba(1.5)
#prints array([[1.,0.]])

#Feature engineering 
#Count links in text not in code

import re 
code_match = re.compile('<pre>(.*?)</pre>',re.MULTILINE|re.DOTALL)
link_match =re.compile('<a href="http://.*?".*?>(.*?)</a>',re.MULTILINE|re.DOTALL)

def extract_features_from_body(s):
	link_count_in_code = 0
	#count links in code to later subtract them
	for match_str in code match.findall(s):
		link_count_in_code +=
		len(len_match.findall(match_str))
	return len(link_match.findall(s)) - link_count_in_code
# it turns out that most posts don't have links in it


#training the classifier
X = np.asarray([extract_features_from_body(text) for post_id, text in fetch_posts() if post_id in all_answers])
knn.neighbors.KNeighborsClassifier()
knn.fit(X,Y)


#measuring classifier's performance
from sklearn.cross_validation import KFold
scores = []
cv = KFold(n=len(X), k=10,indices=True)
for train, test in cv:
	X_train, y_train = X[train],Y[train]
	X_test, Y_test = X[test],Y[test]
	clf = neighbors.KNeighborsClassifier()
	clf.fit(X,Y)
	scores.append(clf.score(X_test,Y_test))
#poor accuracy

#Designing new features
def extract_features_from_body(s):
	num_code_lines = 0
	link_count_in_code = 0
	code_free_s = s 
	#remove source code and count how many lines
	for match_str in code_match.findall(s):
		num_code_lines += match_str.count("\n")
		code_free_s = code_match.sub("",code_free_s)

'''
#
#Adding new features gives better accuracy
#
'''

#logistic regression
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(X,y)

#find threshold
threshold = np.hstack([0],thresholds[medium])
idx80 = precision>=0.8



