from __future__ import division
from igraph import *

g = Graph()

# if not g["name"]["fart"]:
#     print "lol"
# g.add_vertices(3)
# g.add_edges([(0, 1), (1, 2)])
# g.add_vertex()
#
# g.vs[0]["name"] = "Alice"
# g.vs[1]["name"] = "Bob"
# g.vs[2]["name"] = "Eve"
# g.vs[3]["name"] = "farts"
#
# g.vs["label"] = g.vs["name"]
#
# layout = g.layout_kamada_kawai()
# layout = g.layout("kamada_kawai")
# plot(g, layout=layout)

print 'adding vertices'
i = 0
quarter = False
half = False
three_quarters = False

f = open('../youtube-data/big.txt', 'r')
for line in f:
    node_values = line.split()

    # throwing out incomplete pieces of data
    if len(node_values) < 7:
        continue

    video_id = node_values[0]
    author = node_values[1]
    age = node_values[2]
    category = node_values[3]
    length = node_values[4]
    views = node_values[5]
    rate = node_values[6]
    ratings = node_values[7]
    comments = node_values[8]

    # everything past 8  is related videos
    related = node_values[9:]

    g.add_vertex(video_id, author=author, age=age, category=category, length=length, views=views, rate=rate, ratings=ratings, comments=comments)
    i += 1
    if i / 300000 > 0.25 and not quarter :
        print '25%'
        quarter = True
    elif i / 300000 > .5 and not half:
        print '50%'
        half = True
    elif i / 300000 > .75 and not three_quarters:
        print '75%'
        three_quarters = True

f.close()

print 'adding edges'


i = 0
p = 500
f = open('../youtube-data/big.txt', 'r')
for line in f:
    node_values = line.split()

    if len(node_values) < 10:
        i += 1
        continue

    video_id = node_values[0]

    related = node_values[9:]
    try:
        for related_id in related:
            g.add_edge(video_id, related_id)
    except:
        i += 1
        continue
    i += 1

    if i >= p:
        print str((i / 300000) * 100) + "%"
        p += 500


f.close()

g.write('youtube.pickle', 'pickle')
g.write('youtube.gml', 'gml')
g.write('youtube.graphml', 'graphml')
g.write('youtube.edgelist', 'edgelist')
g.write('youtube.lgl', 'lgl')
g.write('youtube.adjacency', 'adjacency')
g.write('youtube.svg', 'svg')
