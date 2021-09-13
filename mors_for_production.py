import numpy as np
import pandas as pd
import csv

jump_level = 0.5

nomenclature_HS1992 = pd.read_csv('./nomenclatures/HS1992_4digits.csv', delimiter=',', header=1).to_numpy()
correspondance_HS2017_NACE2 = pd.read_csv('./correspondence_tables/correspondance_NACE_2_HS_2017_4digits_weighted.csv', delimiter=',', header=1).to_numpy()
nomenclature_NACE2 = pd.read_csv('./nomenclatures/NACE_2.csv', delimiter=',', header=None).to_numpy()
productive_jumps = pd.read_csv('./productive_jumps/hs92_proximities.csv', delimiter=',', header=None).to_numpy()


establishments_test = pd.read_csv('./companies/etablishments-france-department43.csv', delimiter=',', header=1).to_numpy()

# loading computed ranking
# 1. ranking_competitive_advantage
ranking_competitive_advantage = pd.read_csv('./computed_ranking/ranking_competitive_advantage.csv', delimiter=',', header=1).to_numpy()

# 2. ranking_economic_growth
ranking_economic_growth = pd.read_csv('./computed_ranking/ranking_economic_growth.csv', delimiter=',', header=1).to_numpy()

# 3. ranking_green_production
ranking_green_production = pd.read_csv('./computed_ranking/ranking_green_production.csv', delimiter=',', header=1).to_numpy()

# 4. ranking_productive_resilience
ranking_productive_resilience = pd.read_csv('./computed_ranking/ranking_productive_resilience.csv', delimiter=',', header=1).to_numpy()

# 5. ranking_securing_basic_necessities
ranking_securing_basic_necessities = pd.read_csv('./computed_ranking/ranking_securing_basic_necessities.csv', delimiter=',', header=1).to_numpy()



print('---------------Production Units on a territory-------------')
establishment =  [print(establishments_test[j,0]) for j in range (0, len(establishments_test))]

siret = input("Enter a valid SIRET number: (default : 47916269500056) ") or "47916269500056"
print('---------------------Production Unit-----------------------')


print('Siret:', siret)

idx_siret =  np.where(establishments_test[:,0]==int(siret))

# looking for the selected company
activity = establishments_test[idx_siret[0],1][0]
print('Name:', establishments_test[idx_siret[0],5][0])
print('Activity code:', activity)

print('-----------------------Productions-------------------------')


# looking for production
idx_activities =  np.where(correspondance_HS2017_NACE2[:,0]==float(activity))
#print (idx_activities)
for i in range(0, len(idx_activities[0])):

	idx_hs_nomenclature =  np.where(nomenclature_HS1992==float(correspondance_HS2017_NACE2[idx_activities[0][i]][1]))
	#print (idx_ahs_nomenclature)
	hs_code = nomenclature_HS1992[idx_hs_nomenclature[0],0][0]
	print('product #',i+1,' HS code:',hs_code)
	print('product #',i+1,' Description:',nomenclature_HS1992[idx_hs_nomenclature[0],1][0])

	# measuring productive jumps
	print('--------------------Productive jumps-----------------------')
	idx_jumps =  np.where(productive_jumps[:,0]==int(hs_code))
	for j in range(0, len(idx_jumps[0])):
		proximity_jump = productive_jumps[idx_jumps[0][j]][2]
		hs_code_jump = productive_jumps[idx_jumps[0][j]][1]
		if ((proximity_jump >= jump_level) and (int(hs_code_jump) != int(hs_code))):
			print('product jump HS code:',hs_code_jump)
			idx_hs_nomenclature2 =  np.where(nomenclature_HS1992==float(hs_code_jump))
			jump_description = nomenclature_HS1992[idx_hs_nomenclature2[0],1][0]
			print('product jump description:',jump_description)
			print('product jump proximity:',proximity_jump)

			idx_ranking_economic_growth =  np.where(ranking_economic_growth[:,0]==int(hs_code_jump))
			economic_growth_value = ranking_economic_growth[idx_ranking_economic_growth[0],1][0]
			print('product jump economic_growth', economic_growth_value)

			idx_ranking_productive_resilience =  np.where(ranking_productive_resilience[:,0]==int(hs_code_jump))
			productive_resilience_value = ranking_productive_resilience[idx_ranking_productive_resilience[0],1][0]
			print('product jump productive_resilience', productive_resilience_value)

			idx_ranking_securing_basic_necessities =  np.where(ranking_securing_basic_necessities[:,0]==int(hs_code_jump))
			securing_basic_necessities_value = ranking_securing_basic_necessities[idx_ranking_securing_basic_necessities[0],2][0]
			print('product jump securing_basic_necessities', securing_basic_necessities_value)

			



