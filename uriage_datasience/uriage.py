# #%%
# import pandas as pd 
# uriage_data = pd.read_csv("uriage.csv")
# uriage_data.head()

list = [
[1, 100, 0.33, 'AAA', 'AAA100'], 
[2, 200, 0.67, 'BBB', 'BBB200'], 
[3, 300, 1, 'CCC', 'CCC300'], 
[4, 400, 1.33, 'DDD', 'DDD400'], 
[5, 500, 1.67, 'EEE', 'EEE500'], 
[6, 600, 2, 'FFF', 'FFF600']]

import pandas as pd 
df = pd.DataFrame(list)
print(df.head())
print(df.hist())