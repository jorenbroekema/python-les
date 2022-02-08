# Files (csv, txt, excel)
# Scraping
# APIs
import pandas

csv = pandas.read_csv('./something.csv')

for key,value in csv.iterrows():
  print(value['occupation'])
