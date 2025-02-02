import pandas as pd
from collections import defaultdict


def process_data(df):
    df['owner_postcode'] = df['owner_postcode'].astype(str)
    df['owner_address_1'] = df['owner_address_1'].astype(str)
    df['owner_name'] = df['owner_name'].astype(str)
    aa = list(df['owner_address_1'].unique())
    abc = list(map(lambda x: x.lower(), aa))
    return abc


def save_results_to_excel(data, place):
    data1 = defaultdict(list, Organization_Name=data['name1'], Organization_business=data['business1'],
                   Organization_address=data['address1'])
    df = pd.DataFrame(data=data1)
    filename = f'cleaned_1_may_r1_{place}.xlsx'
    df.to_excel(filename, index=False)
