# first example in chapter 1
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#load data from .tsv file
data = sp.genfromtxt("web_traffic.tsv",delimiter="\t")
# tsv format: number of hours 	number of hits

x=data[:,0]
y=data[:,1]

# clean data, eliminate nan values
sp.sum(sp.isnan(y))

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

plt.scatter(x,y)
plt.title("web traffic over the last month")
plt.xlabel("time")
plt.ylabel("Hits/hours")
#xtick?
plt.xticks([w*7*24 for w in range(10)],['week %i' %w for w in range(10)])

plt.autoscale(tight=True)
plt.grid()


#error function RSS
def error(f, x, y):
	return sp.sum((f(x)-y)**2)

#model with straight line 
fp1, residuals, rank, sv, rcond = sp.polyfit(x,y,1,full=True)

#plotting
f1= sp.poly1d(fp1)
fx= sp.linspace(0,x[-1],1000)
plt.plot(fx,f1(fx),linewidth=4)
plt.legend(["d=%i" % f1.order], loc="upper left")
plt.show()

#a better model--segmented lines 
inflection = 3.5*7*24
#data before 
xa= x[:inflection]
ya= y[:inflection]
#data after
xb= x[inflection:]
yb= y[inflection:]

fa = sp.poly1d(sp.polyfit(xa,ya,1))
fb = sp.poly1d(sp.polyfit(xb,yb,1))

fa_error = error(fa,xa,ya)
fb_error = error(fb,xb,yb)

print("Error inflection =%f" % (fa_error+fb_error))
#plot new model
fa_x = sp.linspace(0,xa[-1],1000)
fb_x = sp.linspace(xb[0],xb[-1],1000)
plt.scatter(x,y)
plt.plot(fa_x,fa(fa_x),"r")
plt.plot(fb_x,fb(fb_x),"r")
plt.show()
