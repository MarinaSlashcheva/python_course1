#!/usr/bin/python3.5
import argparse
from Bio import Entrez
Entrez.email = 'slashcheva@gmail.com'

parser = argparse.ArgumentParser(description="Searching datasets "
                                             "from GEO database")

parser.add_argument('query',
                    type=str,
                    help='enter your query')

parser.add_argument('species',
                    type=str,
                    nargs='?',
                    help='enter species you wanted to get')

args = parser.parse_args()
query = args.query
species = args.species

if species == None:
    full_term = query + ' AND GSE[Entry Type]'
else:
    full_term = query + ' AND GSE[Entry Type] AND ' + species + '[Organism]'

search = Entrez.esearch(db='gds', term=full_term)
result = Entrez.read(search)

num_results = result['Count']
print('Founded {0} results containing {1}'.format(num_results, query))

ids = result['IdList']
for id in ids:
    handle = Entrez.esummary(db='gds', id=id)
    summary = Entrez.read(handle)
    cooked_output = summary[0]['Accession'], summary[0]['taxon'], summary[0]['title']
    print('\t'.join(cooked_output))

# Example query ./GSE_search.py 'acinar cells' 'Homo Sapiens'
