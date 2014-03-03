#!/usr/bin/env python

import urllib
import sys
import xml.etree.ElementTree as ET
def extract_name(pdb_id):
    url_template = "http://www.rcsb.org/pdb/rest/describeMol?structureId=%s"
    infile = urllib.urlopen(url_template % pdb_id)
    tree = ET.parse(infile)
    for x in tree.iter("polymerDescription"):
        return x.attrib["description"]
    

pdb_id_list = sys.argv[1]

pdb_ids = []

with open(pdb_id_list) as infile:
    for line in infile:
        pdb_ids.append(line.strip())

for pdb_id in pdb_ids:
    print pdb_id,"&",extract_name(pdb_id).lower(),"\\\\"
    print "\\hline"