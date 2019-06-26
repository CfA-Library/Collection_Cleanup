import pandas as pd


col_master = pd.read_csv("Wolbach_Collection_Mastersheet_v1.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
list(col_master.columns.values)

col_master['MATERIAL'] = col_master['MATERIAL'].astype('|S')


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
col_master = col_master[~col_master.MATERIAL.str.contains("VIS")]


col_master.to_csv("Wolbach_Collection_Mastersheet_v6.csv")

print('CSV saved')