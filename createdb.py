# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:23:18 2018

@author: gy17mjk
"""

import sqlite3

conn = sqlite3.connect('resultsdb.sqlite')
c = conn.cursor()
c.execute("CREATE TABLE Results (address text, burglaries integer)")
c.execute("INSERT INTO Results VALUES ('Queen Vic',2)")
conn.commit()
conn.close()