sample_item ="""
\cvitem{2012}{Briney BS, \textbf{Willis JR}, Crowe JE. Location and length distribution of somatic hypermutation-associated DNA insertions and deletions reveals regions of antibody structural plasticity. \textit{Genes and Immunity} \textbf{13(7)}: 523-529} """

#!/usr/bin/env python
# numpy and biopython are required -- pip install numpy biopython

from Bio import Entrez
from Bio import Medline
from collections import OrderedDict

def parse_record_to_latex(authors, year, title, volume, issue, pmid, journal, pages):
    authors = authors[0]
    new_authors = []
    for auth in authors:
        if 'Willis' in auth:
            auth = "\\textbf{{{0}}}".format(auth)
        new_authors.append(auth)
    return "\cvitem{{{0}}}{{{1}, {2} \\textit{{{3}}} \\textbf{{{4}}}: {5}}}".format( year.split(" ")[0],
            ", ".join(new_authors),
            title, 
            journal,
            volume,
            pages)

class PubMed():

    def __init__(self, search_term, publishing_last_name):

        MAX_COUNT = 300
        self.TERM = search_term
        self.last_name = publishing_last_name
        self.publications = []
        #print('Getting {0} publications containing {1}...'.format(MAX_COUNT, self.TERM))
        h = Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=self.TERM)
        result = Entrez.read(h)
        #print('Total number of publications containing {0}: {1}'.format(self.TERM, result['Count']))
        ids = result['IdList']
        h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
        records = Medline.parse(h)

        if records:
            for record in records:
                authors = record.get('AU'),
                year = record.get('DP')
                title = record.get('TI')
                journal = record.get('TA')
                volume = record.get('VI')
                issue = record.get('IP')
                pages = record.get('PG')
                pmid = record.get('PMID')
                self.publications.append(
                    [authors,
                     year,
                     title,
                     journal,
                     volume,
                     issue,
                     pages,
                     pmid
                     ])
                print(parse_record_to_latex(authors, year, title, volume, issue, pmid , journal, pages))
                print
    

   # def return_html(self):
   #     all_formatted = []
   #     print "here"
   #     print self.publications
   #     if self.publications:
   #         print "here two"
   #         for publicaitons in self.publications:
   #             formatted = ""
   #             # authors
   #             authors = publicaitons[0][0]
   #             if not authors:
   #                 continue
   #             print publicaitons
   #             for author in authors:
   #                 # print author,
   #                 if self.last_name in author:
   #                     authors = [w.replace(author, "<b>" + author + "</b>") for w in authors]

   #             format_author = ", ".join(authors)

   #             # year
   #             format_year = " ({}). ".format(publicaitons[1].split()[0])

   #             # title
   #             format_title = " {} ".format(publicaitons[2])

   #             # journal
   #             format_journal_volume = "<i> {} {} </i>".format(publicaitons[3], publicaitons[4])

   #             formatted = format_author + format_year + format_title + format_journal_volume
   #             if publicaitons[6] is not None:
   #                 formatted += " {}.".format(publicaitons[6])

   #             all_formatted.append({'id': publicaitons[7], 'html': formatted})
   #         return all_formatted
   #     return all_formatted.append({'_id': "", 'html': ''})

if __name__ == '__main__':
    pb = PubMed("Jordan Willis", "Willis")

