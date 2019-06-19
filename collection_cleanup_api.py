import pandas as pd
from isbnlib import *
from isbnlib.registry import bibformatters

wol_col = pd.read_csv("Wolbach_Collection_Mastersheet_v3.csv")

SERVICE = 'goob'

isbn = '9780062420701'
json = bibformatters['json']

metadata = json(meta(isbn, SERVICE)).encode('utf-8')
wol_col['Metadata'] = metadata
print metadata

doi = doi(isbn).encode('utf-8')
wol_col['DOI'] = doi
print doi

info = info(isbn).encode('utf-8')
wol_col['Info'] = info
print info

editions = editions(isbn, service='merge')
wol_col['Editions'] = editions
print editions

wol_col.to_csv("Wolbach_Collection_Mastersheet_v4.csv")