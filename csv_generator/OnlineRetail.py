import numpy as np
from datetime import datetime
import pandas as pd
import random
import os
import sys

list_size = 1000

if (len(sys.argv) > 1):
    list_size = int(sys.argv[1])

countries = ["United Kingdom",
            "France",
            "Australia",
            "Netherlands",
            "Germany",
            "Norway",
            "EIRE",
            "Switzerland",
            "Spain",
            "Poland",
            "Portugal",
            "Italy",
            "Belgium",
            "Lithuania",
            "Japan",
            "Iceland",
            "Channel Islands",
            "Denmark",
            "Cyprus",
            "Sweden",
            "Austria",
            "Israel",
            "Finland",
            "Bahrain",
            "Greece",
            "Hong Kong",
            "Singapore",
            "Lebanon",
            "United Arab Emirates",
            "Saudi Arabia",
            "Czech Republic",
            "Canada",
            "Unspecified",
            "Brazil",
            "USA",
            "European Community",
            "Malta",
            "RSA"]

items = ["Bass Guitar", 
         "Maracas", 
         "Zither", 
         "Accordion", 
         "Symbols", 
         "Acoustic Guitar", 
         "Piccolo", 
         "Xylophone", 
         "Kazoo", 
         "Snare Drum"]

years = np.char.mod('%d',np.random.randint(20120213, high=20120223, size=list_size, dtype=int))
hours = np.char.mod('%d',np.random.randint(00, high=23, size=list_size, dtype=int))
minutes = np.char.mod('%d',np.random.randint(00, high=59, size=list_size, dtype=int))
seconds = np.char.mod('%d',np.random.randint(00, high=59, size=list_size, dtype=int))
datetime_np = np.stack((years, hours, minutes, seconds), axis=1).tolist()
datetime_int = [x[0]+x[1].zfill(2)+x[2].zfill(2)+x[3].zfill(2) for x in datetime_np]

invoice_no = np.random.randint(5000, size=list_size).tolist()
stock_code = np.random.randint(4000, size = list_size).tolist()
description = random.choices(items, k = list_size)
quantity = np.random.randint(5, size = list_size).tolist()
invoice_date = [datetime.strptime(str(x), '%Y%m%d%H%M%S').strftime("%Y-%m-%d %H:%M:%S") for x in datetime_int]
unit_price = [float("{:.2f}".format(random.random()*10)) for x in range(list_size)]
customer_id = np.random.randint(500, size=list_size).tolist()
country= random.choices(countries, k = list_size)

cols = ["invoice_no", "stock_code", "description", "quantity", "invoice_date", "unit_price", "customer_id", "country"]


df = pd.DataFrame(list(zip(invoice_no, stock_code, description, quantity, invoice_date, unit_price, customer_id, country)), columns=cols)

df.to_csv(os.path.join(os.getcwd(), 'sales.log'), index=False, header=False)