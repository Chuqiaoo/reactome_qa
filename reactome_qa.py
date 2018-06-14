__author__ = 'chuqiao'

import pandas as pd
import re
import glob
import os.path, glob
import functools


file_path = "/your path to /reactome_qa/files/*.csv"

root = "/your path to /reactome_qa"

files = glob.glob(file_path)


def get_code_and_version(csv):

    version = csv.replace('_', '.').split('.')[-2]
    data = pd.read_csv(csv)
    df =data[['Priority','Code', 'Entries']]
    df.columns = ['Priority','Code', version]

    return df


def get_additional_values(csv):

    data = pd.read_csv(csv)
    df =data[['Priority', 'Code', 'Name','Description']]

    return df

def get_version_numbers(csv):
    # empty list to store version numbers
    numbers = []
    numbers = csv.replace('_', '.').split('.')[-2]
    return numbers

code_and_version = []
for file in files:

    df = get_code_and_version(file)

    # df.drop_duplicates(inplace=True)
    code_and_version.append(df)


# merge multiple dfs into one df on Priority and Code
code_and_version = functools.reduce(lambda left, right: pd.merge(left, right, on=['Priority', 'Code'], how='outer'), code_and_version )

# *****replace empty cell to 0 2018-06-14
code_and_version.fillna(0, inplace=True)
# *******


# a file list dic with version bunber as key, and the file as value
file_lists = []
for file in files:
    keys = []
    key = get_version_numbers(file)
    keys.append(key)
    for item in keys:
        keys = re.findall(r'\d+', item)
    values = []
    value = file
    values.append(value)
    dictionary = dict(zip(keys, values))

    sorted_dictionary = {int(k) : v for k, v in dictionary.items()}

    file_lists.append(sorted_dictionary.copy())


df_additional_values = []
if len(file_lists) > 0:
    for x in reversed(file_lists):
        dic_values = str(x.values())
        # get rid of symbol in dice value
        dic_values = dic_values.replace("(", '').replace(")", '').replace("[", '').replace("]", '').replace("'", '').replace("dict_values", '')
        df_others = get_additional_values(dic_values)
        # df_others.drop_duplicates(inplace=True)
        df_additional_values.append(df_others)



# concat multiple dfs to one df and ignore index
additional_values = pd.concat(df_additional_values, ignore_index = True)

additional_values.drop_duplicates(['Priority', 'Code'], inplace=True)


# merage two big dfs on priority and code
final_df = pd.merge(code_and_version, additional_values, on=['Priority', 'Code'])

final_df['PriorityNumber'] = [int(i.split('_')[0]) for i in final_df['Priority']]

final_df['CodeNumber'] = final_df['Code'].str[2:].astype(int)

final_df_sort = final_df.sort_values(['PriorityNumber', 'CodeNumber'], ascending=[True, True])

final_data = final_df_sort.drop(['PriorityNumber', 'CodeNumber'], axis=1)

# ***** combine two columns in one datagrame 2018-06-14
final_data["Priority_name"] = final_data["Priority"].map(str) + "_" +final_data["Name"]

# write results to a subdir
results = 'results'

subdir = os.path.join(root, results)

final_path = os.path.join(subdir, 'qqa_report.csv')

final_data.to_csv(final_path, encoding='utf-8', index=False)

