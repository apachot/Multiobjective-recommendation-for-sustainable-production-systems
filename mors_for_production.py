import numpy as np
import pandas as pd
import csv


nomenclature_HS2017 = pd.read_csv('./nomenclatures/HS_2017.csv', delimiter=',', header=None).to_numpy()
correspondance_HS2017_NACE2 = pd.read_csv('./correspondence_tables/correspondance_NACE_2_HS_2017_4digits_weighted.csv', delimiter=',', header=1).to_numpy()
nomenclature_NACE2 = pd.read_csv('./nomenclatures/NACE_2.csv', delimiter=',', header=None).to_numpy()

