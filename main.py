import sys
import pandas as pd

inspeciton_id_global = "(E263FDBD-F454-4B2D-9757-64CF2DD6277F}"

### loop through the export

# column for the comparison from export
RDM_anomaly_ID_column = 2
RDM_anomaly_vendorID_column = 5
RDM_anomaly_OD_column = 9

# Anomaly decativation template
TEMPLATE_anomaly_ID_column = 6
TEMPLATE_inspec_chainage_column = 7


RDM_anomaly_file = pd.read_csv('DM_anomaly_file.csv')
print(RDM_anomaly_file.head())


RDM_template_file = pd.read_excel('test.xlsx')
print(RDM_template_file.head())
#if inspeciton id global =- inspection id:

df = RDM_template_file.reset_index()  # make sure indexes pair with number of rows
for index, row in df.iterrows():
    print(row['c1'])

# need to manipulate excel files
# need to export a file with the proper headers
