from cs1033_evaluator import evaluate_lab9

INPUT_FILE_NAME = input()
################################################################################
# Do not change anything above this line
################################################################################

# Enter your code here
# Use INPUT_FILE_NAME variable to read the file instead of 'contamination_analysis.txt'

import re #import regax


def read_file_data(input_file_name):
    '''
    Read input file and return dictionary containing chemical data
    '''
    
    chemical_data_dictionary={}
    
    try:
        #opens the input file to read
        with open(input_file_name,'r') as input_file:
    
            for line in input_file: #executes for each line in file
                chemical_name,chemical_formula=line.strip().split()
                
                #match the format of the text line using regax
                element_composition=re.findall(r'([A-Z][a-z]*)(\d*)',chemical_formula)
                
                composition_dictionary={} #dictionary to contain element compositions
    
                for element in element_composition: #retrieving the count of elements
                    if element[0] in composition_dictionary:
                        composition_dictionary[element[0]]+=int(element[1])
                    elif element[1]=='':
                        composition_dictionary[element[0]]=1
                    else:
                        composition_dictionary[element[0]]=int(element[1])
    
                chemical_data_dictionary[chemical_name]=composition_dictionary
    
        #returns a dictionary containing all chemicals and their element compositions
        return(chemical_data_dictionary) 
        
    except FileNotFoundError:
        return None
          
            
def categorize_chemical(chemical_data_dictionary):
    '''
    Categorize chemicals into each Level
    '''
    #lists to hold compounds of each category
    level_0_list=[]
    level_1_list=[]
    level_2_list=[]
    level_3_list=[]
    level_4_list=[]
        
    for chemical_name,chemical_composition in chemical_data_dictionary.items():
        #booleans to identify the category of compound
        is_level_1=False
        is_level_2=False
        is_level_3=False
        is_categorized=False
        
        #for chemicals of level 1
        if chemical_composition.get('S',0)>=1 and chemical_composition.get('O',0)>=4 and chemical_composition.get('Na',0)>=1:
            is_level_1=True
            is_categorized=True
            chemical_composition['S']-=1
            chemical_composition['O']-=4
            chemical_composition['Na']-=1
            
        #for chemicals of level 2   
        if chemical_composition.get('S',0)>=1 and chemical_composition.get('O',0)>=3 and chemical_composition.get('Mg',0)>=1:
            if is_categorized==True:
                level_4_list.append(chemical_name)
                continue
            is_level_2=True
            is_categorized=True
            chemical_composition['S']-=1
            chemical_composition['O']-=3
            chemical_composition['Mg']-=1
            
        #for chemicals of level 3
        if chemical_composition.get('O',0)>=2 and chemical_composition.get('Cl',0)>=3:
            if is_categorized==True:
                level_4_list.append(chemical_name)
                continue
            is_level_3=True
            is_categorized=True

        #for chemicals of level 0
        if is_categorized==False:
            level_0_list.append(chemical_name)
            continue

        if is_level_1==True:level_1_list.append(chemical_name)
        elif is_level_2==True:level_2_list.append(chemical_name)
        elif is_level_3==True:level_3_list.append(chemical_name)
    
    #returns lists of chemicals of each category
    return level_0_list,level_1_list,level_2_list,level_3_list,level_4_list


################################################################################
# Main

chemical_data_dictionary=read_file_data(INPUT_FILE_NAME)

level_0_list,level_1_list,level_2_list,level_3_list,level_4_list=categorize_chemical(chemical_data_dictionary)

#iterates for every chemical category
for level,level_list in enumerate([level_0_list,level_1_list,level_2_list,level_3_list,level_4_list]):
    with open(f'Level_{level}.txt', 'w') as output_file:
        
        #iterates for evey compound in categorized list
        for chemical_name in level_list:
            #writing relevant chemical names to relevant file
            output_file.write(f'{chemical_name}\n')

################################################################################
# Do not change anything below this line.
evaluate_lab9()
