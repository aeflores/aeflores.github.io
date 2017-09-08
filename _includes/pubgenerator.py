import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *


pubList=["AlbertFG12","FloresAG13","AlbertFGM13","FMH14","AlbertFMG15","FM16","AlbertFGM15","AlbertFGM17","AlbertCFGG11","AlbertFG12-FSE","AlbertAFGGMPR14"]

path="../_posts/publications/"

def prettyPrintEntry(entry):
    if "month" in entry:
	filename=path+entry["year"]+"-"+entry["month"]+"-01-"+entry["ID"]+".md"
    else:
    	filename=path+entry["year"]+"-01-01-"+entry["ID"]+".md"
    with open(filename, 'w') as f:
        f.write("---\n")
    	f.write("layout: post\n")
    	f.write("title: \""+ entry["title"]+"\"\n")
    	f.write("category: publication\n")
    	f.write("---\n")

    	authors=entry["author"]
    	authorsStr = ", ".join(authors )
    	f.write("#### "+authorsStr)
	if "booktitle" in entry:
    		f.write("\n*In "+entry["booktitle"]+"*")
	if "journal" in entry:
    		f.write("\n*In "+entry["journal"]+"*")
    	if "link" in entry:
        	f.write("  [link]("+entry["link"]+")")
    	if "abstract" in entry:
        	f.write("\n\n"+entry["abstract"])


def customizations(record):
    """Use some functions delivered by the library

    :param record: a record
    :returns: -- customized record
    """
    record = convert_to_unicode(record)
    for key in record:
	record[key]=record[key].replace('{','').replace('}','').encode('utf-8')
    record["author"]=record["author"].replace('\n', ' ').split(" and ")
    return record

def generateFromBib(bibfile):
    with open(bibfile) as bibtex_file:
    	bibtex_str = bibtex_file.read()
    	parser = BibTexParser()
    	parser.customization = customizations
    	bib_database = bibtexparser.loads(bibtex_str,parser=parser)
    	for entry in bib_database.entries:
    	    if entry["ID"] in pubList :
	   	prettyPrintEntry(entry)


generateFromBib("biblio.bib")
generateFromBib("biblio_journals.bib")      
generateFromBib("biblio_other.bib")
