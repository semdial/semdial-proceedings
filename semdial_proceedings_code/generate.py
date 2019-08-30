#!/bin/env python

"""Using order as defined by easychair, or manually, 
and a template with title/preface/sponsors, 
 
generate Semdial proceedings: invited talk abstracts, oral papers, posters, in the right order

easychair order file has following format: 
- % defines comments, 
- # for latex commands to insert as separate pages (USE IT TO SIGNAL POSTERS: put a line containing "posters" when posters starts)
- positive number gives paper numbers, corresponding to file paper_nn.pdf
- negative number gives invited talks, corresponding to file invited_paper_(-nn).pdf

ex:
# \part*{Invited talks}
-4 % Branigan. Say as I say: Alignment as a multi-componential phenomenon
-1 % Oberlander. Talking to animals and talking to things
-3 % Purver. Ask Not What Semantics Can Do For Dialogue - Ask What Dialogue Can Do For Semantics
-2 % Schober. Dialogue, response quality and mode choice in iPhone surveys
# \part*{Oral presentations}
21 % Alacam, Acarturk, Habel. Referring Expressions in Discourse about Haptic Li

Before that, an index must be generated from the toc provided by easychair (with extract_meta.py)

WARNING: we assume the order is invited talks, full papers the posters

usage: order.txt is from easychair, index.txt is from extract_meta in frontmatter
python  order.py order.txt index.txt template
"""
import sys
import subprocess
import string 
import codecs

paper = "papers/paper_%d.pdf"
invited = "papers/invited_paper_%d.pdf"


order_raw = codecs.open(sys.argv[1],encoding="utf8").readlines()
order = [x.strip() for x in order_raw if not(x.startswith("%"))]
titles =  [x.split("%") for x in order if not(x.startswith("#"))]
titles = dict([(int(x),".".join(y.split(".")[1:]).strip())  for (x,y) in titles])
order = [x.split("%")[0] for x in order]


# index of title --> authors
index = codecs.open(sys.argv[2],encoding="utf8").readlines()
index = [x.strip().split("-->") for x in index]
index = dict([(x.strip(),y.strip()) for (x,y) in index])


#template_file = "semdial_proceedings_template.tex"
template_file = sys.argv[3]

template = string.Template(open(template_file).read())
l_inv_talk = []
l_full = []
l_posters = []
# file, title, authors
elt_tplte  = "\\goodpaper{%s}{%s}%%\n{%s}"
poster = False

for line in order:
    if line.startswith("#"):
        if "poster" in line.lower():
            poster = True
    else:
        id = int(line.split()[0])
        a_title = titles[id]
        authors = index[titles[id]]
        if id>0:
            a_file = paper%id
            if not(poster): 
                l_full.append(elt_tplte%(a_file,a_title,authors))
            else:
                l_posters.append(elt_tplte%(a_file,a_title,authors))
        else:
            a_file = invited%(-id)
            l_inv_talk.append(elt_tplte%(a_file,a_title,authors))



# 
final = template.safe_substitute(invited = "\n".join(l_inv_talk), full="\n".join(l_full), posters = "\n".join(l_posters))
final_tex = codecs.open("SemDial_proceedings.tex","w",encoding="utf8")
print >> final_tex, final
final_tex.close()
