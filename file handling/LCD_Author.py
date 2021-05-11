# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 18:33:59 2021

@author: rakesh_reddy
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 22:20:17 2020

@author: rakesh_reddy# -*- coding: utf-8 -*-
"""
import pandas as pd
import pyodbc
import re
from openpyxl import load_workbook

samplefiledf = pd.read_excel(r'C:\Users\kartikp\OneDrive - S&P Global\Desktop\ArticleTable_914.xlsx')
authordetailsdf = pd.read_excel(r'C:\Users\kartikp\OneDrive - S&P Global\Desktop\31st March_Files to be backfilled\ArticleAuthor\Sample_LCD_Author_List.xlsx')
newdf = pd.DataFrame([],columns = ['News_ID','Email','KeyPerson'])

#newdf2 = pd.DataFrame([],columns = ['News_ID','Author'])
#matchedKeyfile = pd.DataFrame([],columns = ['News_ID','Author'])

samplefiledf['scanKeyFile'] = samplefiledf['Article'].str.findall(r'href=((.*)).*')
samplefiledf['secondEmail'] = samplefiledf['Article'].str.findall(r'(href=(.*?)>)')

for i in range(len(samplefiledf)):
    #print (i)
    c = str( samplefiledf.loc[i,'AISArticle'])
    b = (samplefiledf.loc[i,'Article'])
    m = (samplefiledf.loc[i,'Headline'])
    n = 'Fridson'
  
    #scanKeyFile2 = re.findall(r'href=((.*)).* ',b)
    #scanKeyFile2 = re.findall(r'(href=(.*?)>)',b)
    scanKeyFile2 = re.findall(r'href=(.*?.{1,40})',b)
    scanKeyFile3 = re.findall(r'<em(.*?.)/em>',b,flags = re.IGNORECASE)
    
    #scanKeyFile2 = re.findall('[SNL IMAGE KeyFile=\d]{28}',b) 
    #print (scanKeyFile2)
    #print(type(scanKeyFile2))
    if n in m:
        newdf.loc[i,'News_ID'] = c
        newdf.loc[i,'Email'] = 'marty@fridson.com'
        newdf.loc[i,'KeyPerson'] = 433292
    for j in range (len(scanKeyFile2)):
      a= scanKeyFile2[j]
      newdf = newdf.append({'News_ID':c,'Email':a},ignore_index=True)
    for h in range (len(scanKeyFile3)):
        u = scanKeyFile3[h]
        newdf = newdf.append({'News_ID':c,'Email':u},ignore_index=True)

for y in range (len(newdf)):
    f = str(newdf.loc[y,'Email'])
    for z in range (len(authordetailsdf)):
        k = str(authordetailsdf.loc[z,'EMAIL'])
        l = (authordetailsdf.loc[z,'KEY_PERSON'])
        o = (authordetailsdf.loc[z,'NAME'])
       # print ('the values are :')
        #print (f)
        #print (l)
        if k in f:
          # newdf.loc[y,'KeyPerson'] = newdf.append({'KeyPerson':l},ignore_index=True)
           newdf.loc[y,'KeyPerson'] = l
        if o.casefold() in f.casefold():
           newdf.loc[y,'KeyPerson'] = l
             
newdf2 = newdf[newdf['KeyPerson'].notnull()]
newdf2.reset_index(inplace = True, drop= True)
newdf3 = newdf[newdf['KeyPerson'].isnull()]
newdf3.reset_index(inplace = True, drop= True)

for w in range (len(samplefiledf)):
    x = str(samplefiledf.loc[w,'AISArticle'])
    v = 1005823071
    p = 'No Author - Staff Reports'
    print (x)
    if x in newdf2.values:
        print("\nThis value exists in Dataframe") 
    else : 
       print("\nThis value does not exists in Dataframe")
       newdf2 = newdf2.append({'News_ID':x,'Email':p,'KeyPerson':v},ignore_index=True)

newdf2.to_excel(r"C:\Users\kartikp\OneDrive - S&P Global\Desktop\LCDArticleAuthor.xlsx", engine='xlsxwriter',index=False)

for w in range (len(newdf3)):
    x = newdf3.loc[w,'News_ID']
    v = 1005823071
    p = 'No Author - Staff Reports'
    print (x)
    if x in newdf2.values:
        print("\nThis value exists in Dataframe") 
    else : 
       print("\nThis value does not exists in Dataframe")
       newdf2 = newdf2.append({'News_ID':x,'Email':p,'KeyPerson':v},ignore_index=True)

#    for q in range (len(newdf2)):
#        s = int(newdf2.loc[q,'News_ID'])
#        if x :
#            newdf2 = newdf2.append({'News_ID':x,'Email':p,'KeyPerson':v},ignore_index=True)
            

#df = pd.DataFrame(KeyFileList,columns = ['KeyFile'])
#for i in range (len(df)):
 #   z = str( df.loc[i,'KeyFile'])
    #print(label)
  #  print (z)
   # y = str(z)   
   # finddf = newdf2[newdf2['KeyFile'].str.contains(y)] 
   # if len(finddf) > 0 :
    #    print(finddf)
     #   finddf = finddf.reset_index()
      #  print(finddf)
       # s = (finddf.loc[0,'KeyFile'])
        #print (s)
        #t = (finddf.loc[0,'KeyDoc'])
        #print (t)
        #matchedKeyfile = matchedKeyfile.append({'KeyDoc':t,'KeyFile':s},ignore_index=True)
        #print(matchedKeyfile)

