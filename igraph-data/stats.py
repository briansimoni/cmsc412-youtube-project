# This file will read in a graph and generate statistics for it.
from __future__ import division
from igraph import *

g = read('youtube.pickle')
p = g.pagerank()

x = {
    'Science&Technology': 0,
    'Howto&Style': 0,
    'Travel&Events': 0,
    'Nonprofits&Activism': 0,
    'Music': 0,
    'News&Politics': 0,
    'Comedy': 0,
    'Film&Animation': 0,
    'Education': 0,
    'Autos&Vehicles': 0,
    'UNA': 0,
    'Entertainment': 0,
    'People&Blogs': 0,
    'Sports': 0,
    'Pets&Animals': 0,
    'Gadgets&Games': 0,
    'Howto&DIY': 0,
    'Travel&Places': 0
}


videos = {
    'Science&Technology':0,
    'Howto&Style': 0,
    'Travel&Events': 0,
    'Nonprofits&Activism': 0,
    'Music': 0,
    'News&Politics': 0,
    'Comedy': 0,
    'Film&Animation': 0,
    'Education': 0,
    'Autos&Vehicles': 0,
    'UNA': 0,
    'Entertainment': 0,
    'People&Blogs': 0,
    'Sports': 0,
    'Pets&Animals': 0,
    'Gadgets&Games': 0,
    'Howto&DIY': 0,
    'Travel&Places': 0
}

def total_videos(g):
    i = 0
    for v in g.vs:
        i += 1
        videos[v['category']] += 1


total_videos(g)


def initialize(x):
    for category in x:
        x[category] = 0


def in_degree_average(g):
    # takes a graph as input
    # returns a list denoting average in_degree_centrality
    initialize(x)
    i = 0

    for v in g.vs:
        i += 1
        x[v['category']] += v.degree()

    for category in x:
        print(category + " " + str((x[category] / i) * 100))


def average_view_count(g):
    initialize(x)
    i = 0
    for v in g.vs:
        print v['views']
        i += 1
        x[v['category']] += int(v['views'])

    for category in x:
        if videos[category] != 0:
            print(category + " " + str((x[category] / videos[category])))



def average_pagerank(g):
    i = 0
    initialize(x)
    for v in g.vs:
        i += 1
        if i < len(p):
            v['pagerank'] = p[i]
    i = 0

    for v in g.vs:
        i += 1
        if v['pagerank'] != None:
            x[v['category']] += v['pagerank']

    for category in x:
        print(category + " " + str(x[category] * 100))


def average_rate(g):
    i = 0
    initialize(x)
    for v in g.vs:
        if float(v['rate']) == 0:
            videos[v['category']] -= 1
            continue
        else :
            x[v['category']] += float(v['ratings'])
            # print x[v['category']]
            i += 1

    for category in x:
        if videos[category] != 0:
            print category + " " + str(x[category] / videos[category])


#
# for v in g.vs:
#     print v['views']

def mode_videos(g):
    initialize(x)
    id = {}
    for v in g.vs:
        category = v['category']
        if int(v['views']) > x[v['category']] :
            x[v['category']] = int(v['views'])
            id[v['category']] = v['name']

    for category in x:
        if x[category] != 0:
            print category + " " + str(x[category]) + " " + id[category]

# def mode_videos(g):
#     most = 0
#     for v in g.vs :
#         if (v['category'] == 'Music') and (v['views'] > most):
#             print v['views']
#             most = v['views']
#
#     print most



mode_videos(g)



