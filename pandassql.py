import MySQLdb
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from matplotlib import pyplot as plt
import numpy as np


con = MySQLdb.connect(host='essenjio.iptime.org',
                      port=3306,
                      user='root',
                      passwd='pass110829',
                      db='india_project')
targetsite = input("Please enter target site name: ")
band = input("Please enter target band: ")
carrier = input("Please enter target carrier: ")
sector =  input("Please enter target cellid: ")

cursor = con.cursor()
cursor.execute("""SELECT date, cellid_dec, pci, etilt, mtilt, azimuth FROM cellref WHERE site_name=%s AND band=%s AND carrier=%s AND cellid_dec=%s""", (targetsite, band, carrier, sector))
rows = cursor.fetchall()

df = pd.DataFrame([[ij for ij in i] for i in rows])
df.rename(columns={0: 'date', 1: 'cellid', 2: 'pci', 3: 'etilt', 4: 'mtilt', 5: 'azimuth'}, inplace=True)

df2 = pd.DataFrame(df.etilt, columns=['a'])
df2.plot.area()


