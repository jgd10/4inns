import matplotlib.pyplot as plt
import FourInns as FI
import numpy as np

fig = plt.figure(figsize=(14,10))
axes = []
civ = plt.cm.cividis
ymax = [1.5,3.5,1,1.5,4,1.5,3.5,3.5,3,3.5,2.5]
for i in range(11):
    ax = fig.add_subplot(4,3,i+1)
    ax.set_xlim(6,24)
    ax.set_xticks([6,12,18,24])
    ax.set_xticklabels([6,12,18,24])
    ax.set_xlabel('Final Time')
    ax.set_ylabel('Interval Time')
    ax.set_title('{} to {}'.format(FI.checkpoints[i],FI.checkpoints[i+1]))
    ax.set_ylim(0,ymax[i])
    axes.append(ax)

years = [2005,2006,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
for y in years:
    print y
    data = np.genfromtxt('times_{}.csv'.format(y),delimiter=',',dtype=str)
    teams = []
    N,cols = np.shape(data)
    for i in range(N):
        t = FI.Team(data[i,0],data[i,1])
        t.add_times(data[i,2:14])
        teams.append(t)
    
    yr = FI.Year(y,teams)
    for i in range(11):
        ax = axes[i]
        ax.plot(yr.totals,yr.intvls[:,i],linestyle=' ',marker='.',
                mfc='None',color=civ(float(y-2005.)/13.),alpha=0.5)

fig.tight_layout()
fig.savefig('full_intvls.pdf')
