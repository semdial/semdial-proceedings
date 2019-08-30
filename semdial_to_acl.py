from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import os, shutil


def make_xml(counter, title, names, year):
    top = Element('paper')
    top.set('id', str(counter))
    title_xml = SubElement(top, 'title')
    title_xml.text = title
    for name in names:
        name = name.split()
        lname = name[-1]
        fname = ' '.join(name[:-1])
        author_xml = SubElement(top, 'author')
        first_xml = SubElement(author_xml, 'first')
        first_xml.text = fname
        last_xml = SubElement(author_xml, 'last')
        last_xml.text = lname
    url_xml = SubElement(top, 'url')
    url = 'Z{}-{}_semdial_{}.pdf'.format(year, names[0].split()[-1], f'{counter:04}')
    url_xml.text = url
    xml  = str(tostring(top).decode("utf-8"))
    xml = xml.replace('\\\\', '') # some of the stuff is a bit too escapeds
    return xml, url


year = '14'
proceedings = open('semdial_proceedings.tex')

counter = 1
for line in proceedings:
    if 'goodpaper' in line[1:15]: #only if it's towards the beginning
        line = line.strip()
        line = line.replace('\\\\',' ')
        line = line[11:-1]
        line = line.split('}{')
        #print(line)
        paper = line[0]
        title = line[1]
        names = line[2]
        names = names.replace(' and', ',')
        names = names.split(', ')
        xml, url = make_xml(counter, title, names, year)
        counter += 1
        if '.pdf' not in paper:
                paper = '{}.pdf'.format(paper)
        target = paper.split('/')[1]
        shutil.copy(paper, target)
        os.rename(target, url)
        print(xml)
        print()
