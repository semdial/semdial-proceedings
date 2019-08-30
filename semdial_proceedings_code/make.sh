# use toc.tex from easychair
python extract_meta.py toc.tex > index.txt
# order.txt is order file from easychair
# will save in SemDial_proceedings.tex
# requires the papers/ directory from easychair
python generate.py order.txt index.txt semdial_proceedings_template.tex
pdflatex SemDial_proceedings.tex
pdflatex SemDial_proceedings.tex