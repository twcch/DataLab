import pandas as pd

data_path = '/Users/twcch/Documents/Drive/20. 學術/00. 學術研究/10. (碩士論文)企業的財務風險和避稅行為/Data/data/Compustat/志謙(原始資料)/'

df1 = pd.read_excel(data_path + '1998.xlsx', sheet_name='WRDS')
df1['year'] = 1998
df2 = pd.read_excel(data_path + '1999.xlsx', sheet_name='WRDS')
df2['year'] = 1999
df3 = pd.read_excel(data_path + '2000.xlsx', sheet_name='WRDS')
df3['year'] = 2000
df4 = pd.read_excel(data_path + '2001.xlsx', sheet_name='WRDS')
df4['year'] = 2001
df5 = pd.read_excel(data_path + '2002.xlsx', sheet_name='WRDS')
df5['year'] = 2002
df6 = pd.read_excel(data_path + '2003.xlsx', sheet_name='WRDS')
df6['year'] = 2003
df7 = pd.read_excel(data_path + '2004.xlsx', sheet_name='WRDS')
df7['year'] = 2004
df8 = pd.read_excel(data_path + '2005.xlsx', sheet_name='WRDS')
df8['year'] = 2005
df9 = pd.read_excel(data_path + '2006.xlsx', sheet_name='WRDS')
df9['year'] = 2006
df10 = pd.read_excel(data_path + '2007.xlsx', sheet_name='WRDS')
df10['year'] = 2007
df11 = pd.read_excel(data_path + '2008.xlsx', sheet_name='WRDS')
df11['year'] = 2008
df12 = pd.read_excel(data_path + '2009.xlsx', sheet_name='WRDS')
df12['year'] = 2009
df13 = pd.read_excel(data_path + '2010.xlsx', sheet_name='WRDS')
df13['year'] = 2010
df14 = pd.read_excel(data_path + '2011.xlsx', sheet_name='WRDS')
df14['year'] = 2011
df15 = pd.read_excel(data_path + '2012.xlsx', sheet_name='WRDS')
df15['year'] = 2012
df16 = pd.read_excel(data_path + '2013.xlsx', sheet_name='WRDS')
df16['year'] = 2013
df17 = pd.read_excel(data_path + '2014.xlsx', sheet_name='WRDS')
df17['year'] = 2014
df18 = pd.read_excel(data_path + '2015.xlsx', sheet_name='WRDS')
df18['year'] = 2015
df19 = pd.read_excel(data_path + '2016.xlsx', sheet_name='WRDS')
df19['year'] = 2016

result = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19], axis=0)
result.to_csv('/Users/twcch/Downloads/' + 'Compustat.csv', index=False)
