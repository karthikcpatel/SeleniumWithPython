# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:12:25 2020

@author: rakesh_reddy
"""

import pandas as pd
import numpy as np
import pyodbc
from openpyxl import load_workbook

instnissuerdf = pd.read_excel(
    r'C:\Users\kartikp\OneDrive - S&P Global\Desktop\IssuerInstn_Sample_Dev_Feb_22.xlsx')
newsissuerdf = pd.read_excel(
    r'C:\Users\kartikp\OneDrive - S&P Global\Desktop\NewsIssuer_Sample_Dev_Feb_22.xlsx')
articleIndex = pd.read_excel(
    r'C:\Users\kartikp\OneDrive - S&P Global\Desktop\ArticleIndex_Dev_Feb_22.xlsx')
articleIndexPrimary = articleIndex[articleIndex['PrimarySubject'] == 1]
articleIndexPrimary.reset_index(inplace=True, drop=True)
articleIndexPrimary = articleIndexPrimary.reindex(
    columns=np.append(articleIndexPrimary.columns.values, ['Issuer', 'KeyInstn', 'KeyInDocs']))
newdf = pd.DataFrame([], columns=['AISArticleIndex', 'LcdKeyDoc', 'KeyDoc', 'Subject', 'PrimarySubject', 'ISSUER_ID'])
newdf2 = pd.DataFrame([], columns=['AISArticleIndex', 'LcdKeyDoc', 'KeyDoc', 'Subject', 'PrimarySubject', 'ISSUER_ID',
                                   'KeyInstn', 'KeyInDocs'])
print(instnissuerdf)
print(newsissuerdf)
for x in range(len(articleIndexPrimary)):
    a = int(articleIndexPrimary.loc[x, 'LcdKeyDoc'])
    b = int(articleIndexPrimary.loc[x, 'MIKeyDoc'])
    c = int(articleIndexPrimary.loc[x, 'Subject'])
    d = int(articleIndexPrimary.loc[x, 'PrimarySubject'])
    for y in range(len(newsissuerdf)):
        e = int(newsissuerdf.loc[y, 'NEWS_ID'])
        f = int(newsissuerdf.loc[y, 'ISSUER_ID'])
        if e == a:
            newdf = newdf.append({'LcdKeyDoc': a, 'KeyDoc': b, 'Subject': c, 'PrimarySubject': d, 'ISSUER_ID': f},
                                 ignore_index=True)
for i in range(len(instnissuerdf)):
    g = int(instnissuerdf.loc[i, 'Issuer'])
    # print (b)
    h = int(instnissuerdf.loc[i, 'KeyInstn'])
    k = int(instnissuerdf.loc[i, 'KeyInDocs'])
    # print (a)
    for j in range(len(newdf)):
        l = (newdf.loc[j, 'LcdKeyDoc'])
        m = (newdf.loc[j, 'KeyDoc'])
        n = (newdf.loc[j, 'Subject'])
        o = (newdf.loc[j, 'PrimarySubject'])
        p = (newdf.loc[j, 'ISSUER_ID'])
        #    print (c)
        #   e = int (newdf.loc[j,'NEWS_ID'])
        #   print (d)
        if g == p:
            #      print (a)
            newdf2 = newdf2.append(
                {'LcdKeyDoc': l, 'KeyDoc': m, 'Subject': n, 'PrimarySubject': o, 'ISSUER_ID': p, 'KeyInstn': h,
                 'KeyInDocs': k}, ignore_index=True)

# newdf2 = newdf2.merge(newdf.drop_duplicates(), on =['LcdKeyDoc'],how = 'right',indicator = True)
for ab in range(len(newdf)):
    ac = (newdf.loc[ab, 'LcdKeyDoc'])
    ad = (newdf.loc[ab, 'KeyDoc'])
    ae = (newdf.loc[ab, 'Subject'])
    af = (newdf.loc[ab, 'PrimarySubject'])
    ag = (newdf.loc[ab, 'ISSUER_ID'])
    if ag not in instnissuerdf.values:
        newdf2 = newdf2.append({'LcdKeyDoc': ac, 'KeyDoc': ad, 'Subject': ae, 'PrimarySubject': af, 'ISSUER_ID': ag},
                               ignore_index=True)
for ba in range(len(articleIndexPrimary)):
    bc = (articleIndexPrimary.loc[ba, 'LcdKeyDoc'])
    bd = (articleIndexPrimary.loc[ba, 'MIKeyDoc'])
    be = (articleIndexPrimary.loc[ba, 'Subject'])
    bf = (articleIndexPrimary.loc[ba, 'PrimarySubject'])
    bg = (articleIndexPrimary.loc[ba, 'Issuer'])
    if bc not in newdf.values:
        newdf2 = newdf2.append({'LcdKeyDoc': bc, 'KeyDoc': bd, 'Subject': be, 'PrimarySubject': bf, 'ISSUER_ID': bg},
                               ignore_index=True)
for q in range(len(articleIndex)):
    r = (articleIndex.loc[q, 'LcdKeyDoc'])
    s = (articleIndex.loc[q, 'MIKeyDoc'])
    t = (articleIndex.loc[q, 'Subject'])
    u = (articleIndex.loc[q, 'PrimarySubject'])
    if u == 0:
        newdf2 = newdf2.append({'LcdKeyDoc': r, 'KeyDoc': s, 'Subject': t, 'PrimarySubject': u}, ignore_index=True)

newdf2.to_excel("Issuer_Article_Instn.xlsx", engine='xlsxwriter')

# newsissuerdf = newsissuerdf.assign(Present=newsissuerdf.ISSUER_ID.isin(instnissuerdf.Issuer_ID).astype(int))
# newsissuerdf = newsissuerdf.assign(Instn=newsissuerdf.ISSUER_ID.isin(instnissuerdf.Issuer_ID))
# newsissuerdf = (newsissuerdf.ISSUER_ID.isin(instnissuerdf.Issuer_ID))