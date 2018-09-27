import pandas as pd

vrPostcodesDf = pd.read_csv('./waPostcodesDf_7 digit postcodes.csv', sep=',', header=0, usecols=['no', 'easting', 'northing', 'date' ], dtype={'no': 'object', 'easting': 'float64', 'northing': 'float64', 'date': 'object' })

# vrPostcodesDf = vrPostcodesDf.query('date == "2010"')
#
# del vrPostcodesDf['date']

vrPostcodesDf = vrPostcodesDf.rename(columns = {'no':'Z', 'easting':'X', 'northing':'Y'})

vrPostcodesDf = vrPostcodesDf.dropna()

print(vrPostcodesDf.shape[0])
# vrPostcodesDf.to_csv('carto_local_postcodes.csv', index=False)
