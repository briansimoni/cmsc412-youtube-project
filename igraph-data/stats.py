# This file will read in a graph and generate statistics for it.
from __future__ import division
from igraph import *

g = read('youtube.pickle')
# x = g.indegree()
# print x

x = {
    'Science&Technology':0,
    'Howto&Style': 0,
    'Travel&Events' : 0,
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


def initialize(x):
    for category in x:
        x[category] = 0


def in_degree_average(g):
    # takes a graph as input
    # returns a list denoting average in_degree_centrality
    initialize(x)
    i = 0

    for v in g.vs:
        i += v.degree()
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
        print(category + " " + str((x[category] / i)))

average_view_count(g)


