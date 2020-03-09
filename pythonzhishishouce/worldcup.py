#!/usr/local/bin/python3.7
# %%
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
df = pd.read_csv('results.csv')
df.head()

# %%
# 26.1.1 获取所有世界杯比赛数据（不包含预选赛）
df_FIFA_all = df[df['tournament'].str.contains('FIFA', regex=True)]
df_FIFA = df_FIFA_all[df_FIFA_all['tournament'] == 'FIFA World Cup']

df_FIFA.loc[:, 'date'] = pd.to_datetime((df_FIFA.loc[:, 'date']))
df_FIFA['year'] = df_FIFA['date'].dt.year
df_FIFA['diff_score'] = df_FIFA['home_score'] - df_FIFA['away_score']
df_FIFA['win_team'] = ''
df_FIFA['diff_score'] = pd.to_numeric(df_FIFA['diff_score'])
# note: The first method to get the winners
#df_FIFA.loc[df_FIFA['diff_score']>0, 'win_team'] = df_FIFA.loc[df_FIFA['diff_score']>0, 'home_team']
#df_FIFA.loc[df_FIFA['diff_score']<0, 'win_team'] = df_FIFA.loc[df_FIFA['diff_score']<0, 'away_team']
#df_FIFA.loc[df_FIFA['diff_score']==0, 'win_team'] = 'Draw'
# df_FIFA.head()
# The second method to get the winners


def find_win_team(df):
    winners = []
    for i, row in df.iterrows():
        if row['home_score'] > row['away_score']:
            winners.append(row['home_team'])
        elif row['home_score'] < row['away_score']:
            winners.append(row['away_team'])
        else:
            winners.append('Draw')
    return winners


df_FIFA['win_team'] = find_win_team(df_FIFA)
df_FIFA.head()
# %%
# 26.1.2 获取世界杯所有比赛的前20强数据
s = df_FIFA.groupby('win_team')['win_team'].count()
s.sort_values(ascending=True, inplace=True)
s.drop(labels=['Draw'], inplace=True)
# 柱状图
#s.head(20).plot(kind='bar', figsize=(10,6), title='Top 20 winners of World cup')
# 水平柱状图
# s.sort_values(ascending=True, inplace=True) # ascending=True 按升序排
# s.tail(20).plot(kind='barh', figsize=(10,6), title='Top 20 Winners of World Cup') # .tail（20） 取最后的20行
# 饼图
s_percentage = s/s.sum()
s_percentage.tail(20).plot(kind='pie', figsize=(10, 10), autopct='%.1f%%',
                           startangle=173, title='Top 20 Winners of World Cup', label='')
# %%
# 分析结论1
s.get('China', default='NA')
s.get('Japan', default='NA')
# %%
# 26.1.2.2 各个国家对进球总数量情况
df_score_home = df_FIFA[['home_team', 'home_score']]
column_update = ['team', 'score']
df_score_home.columns = column_update
df_score_away = df_FIFA[['away_team', 'away_score']]
df_score_away.columns = column_update
df_score = pd.concat([df_score_home, df_score_away], ignore_index=True)
s_score = df_score.groupby('team')['score'].sum()
s_score.sort_values(ascending=False, inplace=True)
s_score.sort_values(ascending=True, inplace=True)
s_score.tail(20).plot(kind='barh', figsize=(10, 6),
                      title='Top 20 in Total Score of World Cup')
s_score.tail()
# %%
# 26.1.3 2018年世界杯32强分析
team_list = ['Russia', 'Germany', 'Brazil', 'Portugal', 'Argentina', 'Belgium', 'Poland', 'France', 'Spain', 'Peru', 'Switzerland', 'England', 'Colombia', 'Mexico', ' Uruguay', 'Croatia',
             'Denmark', 'Iceland', 'Costa Rica', 'Sweden', 'Tunisia', 'Egypt', ' Senegal', 'Iran', 'Serbia', 'Nigeria', 'Australia', 'Japan', 'Morocco', 'Panama', ' Korea Republic', 'Saudi Arabia']
for item in team_list:
    if item not in s_score.index:
        print(item)

# %%
### 26.1.3.1 自1872年以来，32强数据情况
df_top32 = df_FIFA[(df_FIFA['home_team'].isin(team_list))&(df_FIFA['away_team'].isin(team_list))]
s_32 = df_top32.groupby('win_team')['win_team'].count()
s_32.sort_values(ascending=False, inplace=True)
s_32.drop(labels=['Draw'],inplace=True)
s_32.sort_values(ascending=True, inplace=True)
#s_32.plot(kind='barh', figsize=(8,12), title='Top 32 of World Cup since year 1872')
s_32.head()
# %%
### 进球数据情况
df_score_home_32 = df_top32[['home_team','home_score']]
column_update = ['team', 'score']
df_score_home_32.columns = column_update
df_score_away_32 = df_top32[['away_team','home_score']]
df_score_away_32.columns = column_update
df_score_32 = pd.concat([df_score_home_32, df_score_away_32], ignore_index=True)
df_score_32.head()
s_score_32 = df_score_32.groupby('team')['score'].sum()
s_score_32.sort_values(ascending=True, inplace=True)
s_score_32.plot(kind='barh',figsize=(8,12), title='Top 23 in Total Score of World Cup since year 1872')

# %%
df_top32.head()

# %%


# %%
