# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:24:05 2017

@author: Carl
"""

from math import sqrt
critics={'Lisa Rose':{'Lady in the Water':2.5,'Snake on  a Plane':3.5,'Just My Luck':3.0,'Superman Returns':5.0,'You,Me, and Dupree':2.5,'The Night listener':3.0},
         'Gene Seymour':{'Lady in the Water':3.0,'Snake on  a Plane':3.5,'Just My Luck':1.5,'Superman Returns':5.0,'You,Me, and Dupree':3.5,'The Night listener':3.0},
         'Michael Phillips':{'Lady in the Water':2.5,'Snake on  a Plane':3.0,'Superman Returns':3.5,'The Night listener':4.0},
         'Claudia Puig':{'Snake on  a Plane':3.5,'Just My Luck':3.0,'Superman Returns':4.0,'You,Me, and Dupree':2.5,'The Night listener':4.5},
         'Mick Lasalle':{'Lady in the Water':3.0,'Snake on  a Plane':4.0,'Just My Luck':2.0,'Superman Returns':3.0,'You,Me, and Dupree':2.0,'The Night listener':3.0},
         'Jack Mattews':{'Lady in the Water':3.0,'Snake on  a Plane':4.0,'Superman Returns':5.0,'You,Me, and Dupree':3.5,'The Night listener':3.0},
         'Toby':{'Snake on  a Plane':4.5,'Superman Returns':4.0,'You,Me, and Dupree':1.0}
         }

def sim_distance(prefs,person1,person2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    if len(si)==0:return 0
    sum_of_squares=sum([(prefs[person1][item]-prefs[person2][item])**2 for item in prefs[person1] if item in  prefs[person2] ])
    return 1/(1+sqrt(sum_of_squares))

def  sim_pearson(prefs,p1,p2):
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:
               si[item]=1
    n=len(si)
    if n==0:return 1

    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])

    sum1_sq=sum(prefs[p1][it]**2 for it in si)
    sum2_sq=sum(prefs[p2][it]**2 for it in si)

    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1_sq-sum1**2/n)*(sum2_sq-sum2**2/n))

    if den==0:return 0

    r=num/den

    return r


def topMatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,other),other) for other in prefs if other !=person ]
    scores.sort(reverse=True)
    return scores[0:n]

def getRecommendations(prefs,person,similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
        if other==person:continue
        sim=similarity(prefs,person,other)

        if sim<=0:continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item]==0:
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
                simSums.setdefault(item,0)
                simSums[item]+=sim
    rankings=[(totals/simSums[item],item)for item ,totals in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings
print (topMatches(critics,'Toby',3))
getRecommendations(critics,'Lisa Rose')


import pydelicious
