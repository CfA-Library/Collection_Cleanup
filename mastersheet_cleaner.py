import pandas as pd


col_master = pd.read_csv("Wolbach_Collection_Mastersheet_v1.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
list(col_master.columns.values)

col_master['MATERIAL'] = col_master['MATERIAL'].astype('|S')
col_master['COLLECTION'] = col_master['COLLECTION'].astype('|S')

col_master = col_master[~col_master.MATERIAL.str.contains("CDROM")]
col_master = col_master[~col_master.MATERIAL.str.contains("DATA")]
col_master = col_master[~col_master.MATERIAL.str.contains("DVDRO")]
col_master = col_master[~col_master.MATERIAL.str.contains("EQUIP")]
col_master = col_master[~col_master.MATERIAL.str.contains("ISSBD")]
col_master = col_master[~col_master.MATERIAL.str.contains("ISSLL")]
col_master = col_master[~col_master.MATERIAL.str.contains("ISSUE")]
col_master = col_master[~col_master.MATERIAL.str.contains("MAP")]
col_master = col_master[~col_master.MATERIAL.str.contains("MEDIA")]
col_master = col_master[~col_master.MATERIAL.str.contains("MFICH")]
col_master = col_master[~col_master.MATERIAL.str.contains("MFILM")]
col_master = col_master[~col_master.MATERIAL.str.contains("MIXED")]
col_master = col_master[~col_master.MATERIAL.str.contains("RCASS")]
col_master = col_master[~col_master.MATERIAL.str.contains("VCASS")]
col_master = col_master[~col_master.MATERIAL.str.contains("VDVD")]
col_master = col_master[~col_master.MATERIAL.str.contains("VIS")]

col_master = col_master[~col_master.COLLECTION.str.contains("HASTH")]
col_master = col_master[~col_master.COLLECTION.str.contains("HDH")]
col_master = col_master[~col_master.COLLECTION.str.contains("HDS")]
col_master = col_master[~col_master.COLLECTION.str.contains("JRNLH")]
col_master = col_master[~col_master.COLLECTION.str.contains("JRNLS")]
col_master = col_master[~col_master.COLLECTION.str.contains("MFRMH")]
col_master = col_master[~col_master.COLLECTION.str.contains("MFRMH")]
col_master = col_master[~col_master.COLLECTION.str.contains("MFRMS")]
col_master = col_master[~col_master.COLLECTION.str.contains("PCHTH")]
col_master = col_master[~col_master.COLLECTION.str.contains("PCHTS")]
col_master = col_master[~col_master.COLLECTION.str.contains("PORTH")]
col_master = col_master[~col_master.COLLECTION.str.contains("PORTS")]
col_master = col_master[~col_master.COLLECTION.str.contains("REFS")]
col_master = col_master[~col_master.COLLECTION.str.contains("RESH")]
col_master = col_master[~col_master.COLLECTION.str.contains("RESS")]
col_master = col_master[~col_master.COLLECTION.str.contains("RREFS")]
col_master = col_master[~col_master.COLLECTION.str.contains("SMAS")]
col_master = col_master[~col_master.COLLECTION.str.contains("STORH")]
col_master = col_master[~col_master.COLLECTION.str.contains("STORS")]
col_master = col_master[~col_master.COLLECTION.str.contains("VIDH")]
col_master = col_master[~col_master.COLLECTION.str.contains("WIAH")]

col_master.to_csv("Wolbach_Collection_Mastersheet_v7.csv")

print('CSV saved')