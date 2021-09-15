import numpy as np
import pandas as pd
import csv

from sklearn.preprocessing import normalize

def minmax_norm(df_input):
    df_input -= np.mean(df_input, axis=0)
    df_input /= np.std(df_input, axis=0)
    df_input = (df_input - df_input.min()) / ( df_input.max() - df_input.min())
    
    return df_input

jump_level = 0.70

territory = "43" #french department

# setting weights
W_a_0 = .3 # Objective #1: Diversify production
W_a_1 = .3 # Objective #2: Increase the competitive advantage
W_a_2 = .15 # Objective #3: Improve economic performance
W_a_3 = .1 # Objective #4: Improve the resilience of the production system
W_a_4 = .1 # Objective #5: Secure the production of essential goods
W_a_5 = .05 # Objective #6: Promote the production of environmental products

nomenclature_HS2017 = pd.read_csv('./nomenclatures/HS2017_4digits.csv', delimiter=',', header=1).to_numpy()
correspondance_HS2017_HS1992 = pd.read_csv('./correspondence_tables/correspondance_HS2017_HS1992_4digits.csv', delimiter=',', header=1).to_numpy()
correspondance_HS2017_NACE2 = pd.read_csv('./correspondence_tables/correspondance_NACE_2_HS_2017_4digits_weighted.csv', delimiter=',', header=1).to_numpy()
nomenclature_NACE2 = pd.read_csv('./nomenclatures/NACE_2.csv', delimiter=',', header=None).to_numpy()
productive_jumps = pd.read_csv('./productive_jumps/hs92_proximities.csv', delimiter=',', header=1, dtype={'proximity': float}).to_numpy()


establishments_test = pd.read_csv('./companies/etablishments-france-department43.csv', delimiter=',', header=1).to_numpy()

# loading computed ranking
# 1. ranking_competitive_advantage
ranking_competitive_advantage = pd.read_csv('./computed_ranking/ranking_competitive_advantage.csv', delimiter=',', header=1, dtype={'hs4': int, 'local_rca': float}).to_numpy()

# 2. ranking_economic_growth
ranking_economic_growth = pd.read_csv('./computed_ranking/ranking_economic_growth.csv', delimiter=',', header=1, dtype={'PCI_2019': float}).to_numpy()

# 3. ranking_green_production
ranking_green_production = pd.read_csv('./computed_ranking/ranking_green_production.csv', delimiter=',', header=1).to_numpy()

# 4. ranking_productive_resilience
ranking_productive_resilience = pd.read_csv('./computed_ranking/ranking_productive_resilience.csv', delimiter=',', header=1, dtype={'resilience_nomalized': float}).to_numpy()

# 5. ranking_securing_basic_necessities
ranking_securing_basic_necessities = pd.read_csv('./computed_ranking/ranking_securing_basic_necessities.csv', delimiter=',', header=1, dtype={'maslow_normalized': float}).to_numpy()

# normalize data
ranking_competitive_advantage[1:,6] = minmax_norm(ranking_competitive_advantage[1:,6])
ranking_economic_growth[1:,1] = minmax_norm(ranking_economic_growth[1:,1])
ranking_productive_resilience[1:,5] = minmax_norm(ranking_productive_resilience[1:,5])
ranking_securing_basic_necessities[1:,2] = minmax_norm(ranking_securing_basic_necessities[1:,2])
productive_jumps[1:,2] = minmax_norm(productive_jumps[1:,2])


print('---------------Production Units on a territory-------------')
for i in range(0, len(establishments_test)):
	idx_check_activity =  np.where(correspondance_HS2017_NACE2[:,0]==float(establishments_test[i,1]))
	if (len(idx_check_activity[0]) > 0):
		print(establishments_test[i,5], ', activity=', establishments_test[i,1],'(siret =', establishments_test[i,0], ')')


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
weights = ['hs_code', 'description', 'weight', 'proximity_jump', 'competitive_advantage_value', 'economic_growth_value', 'productive_resilience_value', 'securing_basic_necessities_value', 'green_production_value']

for i in range(0, len(idx_activities[0])):

	idx_hs_nomenclature =  np.where(nomenclature_HS2017==float(correspondance_HS2017_NACE2[idx_activities[0][i]][1]))
	#print (idx_ahs_nomenclature)
	hs_code = nomenclature_HS2017[idx_hs_nomenclature[0],0][0]
	print('product #',i+1,' HS code:',hs_code)
	print('product #',i+1,' Description:',nomenclature_HS2017[idx_hs_nomenclature[0],1][0])
	# measuring productive jumps
	idx_jumps =  np.where(productive_jumps[:,0]==int(hs_code))
	if (len(idx_jumps[0]) > 0):
		for j in range(0, len(idx_jumps[0])):
			proximity_jump = productive_jumps[idx_jumps[0][j]][2]
			hs_code_jump = productive_jumps[idx_jumps[0][j]][1]
			hs_code_jump_92 = hs_code_jump
			jump_description = ""
			hs_meta_category = int(str(int(hs_code)).zfill(4)[0:1])
			jump_meta_category = int(str(int(hs_code_jump)).zfill(4)[0:1])
			if ((proximity_jump >= jump_level) and (int(hs_code_jump) != int(hs_code)) and ((hs_meta_category == jump_meta_category) or (hs_meta_category == (jump_meta_category-1)) or (hs_meta_category == (jump_meta_category+1)))):
				#print('product jump HS1992 code:',hs_code_jump)
				# jumps are in HS1992, we should convert in HS2017
				idx_correspondence=  np.where(correspondance_HS2017_HS1992[:,1]==float(hs_code_jump))
				if (len(idx_correspondence[0]) > 0):
					hs_code_jump = correspondance_HS2017_HS1992[idx_correspondence[0],0][0]
					#print('product jump HS2017 code:',hs_code_jump)
				
				idx_hs_nomenclature2 =  np.where(nomenclature_HS2017[:,0]==float(hs_code_jump))
				if (len(idx_hs_nomenclature2[0]) > 0):
					jump_description = nomenclature_HS2017[idx_hs_nomenclature2[0],1][0]
					#print('product jump description:',jump_description)
				#print('product jump proximity:',proximity_jump)

				economic_growth_value = 0
				idx_ranking_economic_growth =  np.where(ranking_economic_growth[:,0]==int(hs_code_jump))
				if (len(idx_ranking_economic_growth[0]) > 0):
					economic_growth_value = ranking_economic_growth[idx_ranking_economic_growth[0],1][0]
				#print('product jump economic_growth:', economic_growth_value)

				productive_resilience_value = 0
				idx_ranking_productive_resilience =  np.where(ranking_productive_resilience[:,0]==int(hs_code_jump))
				if (len(idx_ranking_productive_resilience[0]) > 0):
					productive_resilience_value = ranking_productive_resilience[idx_ranking_productive_resilience[0],1][0]
				#print('product jump productive_resilience:', productive_resilience_value)

				securing_basic_necessities_value = 0
				idx_ranking_securing_basic_necessities =  np.where(ranking_securing_basic_necessities[:,0]==int(hs_code_jump))
				if (len(idx_ranking_securing_basic_necessities[0]) > 0):
					securing_basic_necessities_value = ranking_securing_basic_necessities[idx_ranking_securing_basic_necessities[0],2][0]
				#print('product jump securing_basic_necessities:', securing_basic_necessities_value)

				idx_ranking_green_production =  np.where(ranking_green_production[:,0]==int(hs_code_jump))
				
				green_production_value = 0
				if (len(idx_ranking_green_production[0]) > 0):
					green_production_value = ranking_green_production[idx_ranking_green_production[0],1][0]
				#print('product jump green_production:', green_production_value)

				idx_ranking_competitive_advantage =  np.where((ranking_competitive_advantage[:,0]==int(territory)) & (ranking_competitive_advantage[:,1]==int(hs_code_jump))) #& (ranking_competitive_advantage[:,1]==int(hs_code_jump))	
				competitive_advantage_value = 0
				if (len(idx_ranking_competitive_advantage[0]) > 0):
					competitive_advantage_value = ranking_competitive_advantage[idx_ranking_competitive_advantage[0],6][0]
				#print('product jump competitive_advantage:', competitive_advantage_value)

				total_weight = W_a_0 * proximity_jump + W_a_1 * competitive_advantage_value + W_a_2 * economic_growth_value + W_a_3 * productive_resilience_value + W_a_4 * (1.0-securing_basic_necessities_value) + W_a_5 * green_production_value
				weights = np.vstack([weights, [hs_code_jump, jump_description, total_weight, proximity_jump, competitive_advantage_value, economic_growth_value, productive_resilience_value, (1-securing_basic_necessities_value), green_production_value]])

weights = np.unique(weights, axis=0)
weights_values = weights[:,2]
weights_values_indexes = weights_values.argsort()
weights_values_indexes = weights_values_indexes[::-1]
weights = weights[weights_values_indexes][:7]
print('--------------------Productive jumps-----------------------')
print(weights)


			



