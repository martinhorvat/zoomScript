# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#!/usr/bin/python3
import pandas as pd
import datetime as dt
import numpy as np
import sys
# %%
urnik = pd.read_csv('~/urnik.txt', delimiter='\t', names=['Mon', 'Tue', 'Wed', 'Thu'])
urnik.insert(0, 'Ura', np.arange(8, 16, 1))
urnik.set_index('Ura', inplace=True)
#urnik.replace('None', np.NaN, inplace=True)

meeting = pd.read_csv('~/meeting.txt', delimiter='\t', names=['Predmet', 'ID', 'pwd'])
meeting.set_index('Predmet', inplace=True)

meeting['pwd'] = '&pwd=' + meeting['pwd'].astype(str)
meeting.replace('&pwd=None', '', inplace=True)
# %%
currentDT = dt.datetime.now()

dan = currentDT.strftime("%a")
ura = currentDT.hour

if len(sys.argv) > 1:
    dan = str(sys.argv[1])
    ura = int(sys.argv[2])

print("Dan: %s, Ura: %d" % (dan, ura))
# %%
predmet = urnik[dan][ura]

ID = meeting['ID'][predmet]
pwd = meeting['pwd'][predmet]

print("Predmet: %s, ID: %d, pwd: %s" % (predmet, ID, pwd))
# %%
url = '"zoommtg://zoom.us/join?action=join&confno=%s%s"' % (ID, pwd)
# %%
bashCommand = 'xdg-open ' + url

import os

os.system(bashCommand)