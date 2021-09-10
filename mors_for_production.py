import numpy as np
import pandas as pd
import csv


nomenclature_HS2017 = pd.read_csv('./nomenclatures/HS_2017.csv', delimiter=',', header=None).to_numpy()
correspondance_HS2017_NACE2 = pd.read_csv('./correspondence_tables/correspondance_NACE_2_HS_2017_weighted.csv', delimiter=',', header=1).to_numpy()
nomenclature_NACE2 = pd.read_csv('./nomenclatures/NACE_2.csv', delimiter=',', header=None).to_numpy()

establishments_test = pd.read_csv('./companies/etablishments-france-department43.csv', delimiter=',', header=1).to_numpy()

establishment =  [print(establishments_test[j,0]) for j in range (0, len(establishments_test))]

siret = input("Enter a valid SIRET number: (default : 47916269500056) ") or "47916269500056"
print(siret)

idx_siret =  np.where(establishments_test==int(siret))

# looking for the selected company
activity = establishments_test[idx_siret[0],1][0]
print('Name:', establishments_test[idx_siret[0],5])
print('Activity code:', activity)

# looking for production
idx_activities =  np.where(correspondance_HS2017_NACE2==float(activity))
print (idx_activities)
for i in range(0, len(idx_activities[0])):
	print('product #',i+1,' HS code:',nomenclature_HS2017[idx_activities[0][i]][0])
	print('product #',i+1,' Description:',nomenclature_HS2017[idx_activities[0][i]][1])

# convert HS2017 to HS1992

# measuring productive jumps

# defining territory
dep = 43

# loading computed ranking
# 1. ranking_competitive_advantage
ranking_competitive_advantage = pd.read_csv('./computed_ranking/ranking_competitive_advantage.csv', delimiter=',', header=None).to_numpy()

# 2. ranking_economic_growth
ranking_economic_growth = pd.read_csv('./computed_ranking/ranking_economic_growth.csv', delimiter=',', header=None).to_numpy()

# 3. ranking_green_production
ranking_green_production = pd.read_csv('./computed_ranking/ranking_green_production.csv', delimiter=',', header=None).to_numpy()

# 4. ranking_productive_resilience
ranking_productive_resilience = pd.read_csv('./computed_ranking/ranking_productive_resilience.csv', delimiter=',', header=None).to_numpy()

# 5. ranking_securing_basic_necessities
ranking_securing_basic_necessities = pd.read_csv('./computed_ranking/ranking_securing_basic_necessities.csv', delimiter=',', header=None).to_numpy()
