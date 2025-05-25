import os 
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
from cs1033_evaluator import evaluate_lab9
import matplotlib.pyplot as plt

input_file_name = input()

# Your code should be included here. 
# Avoid using the print function in the code, as it may cause errors

output_file_name='output.txt'


def read_input_file(input_file_name):
    '''
    Read the input file and extract data
    '''
    try:
        #opens input file to read
        with open(input_file_name,'r') as input_file:
            #list out each line in the file
            lines=input_file.readlines()
            
            try:
                #assign float and integer values in lines to variables
                v_in,v_out,tolerance=map(lambda x: int(x) if x.isdigit()==True else float(x),lines[0].strip().split(', '))
                resistor_list=list(map(lambda x: int(x) if x.isdigit()==True else float(x),lines[1].strip().split(', ')))
                return v_in,v_out,tolerance,resistor_list
            
            except ValueError:
                return  None,None,None,None

    except FileNotFoundError:
        return  None,None,None,None


def find_v_out(v_in,r1,r2):
    '''
    Calcualtes output voltage of a given resistor combination
    '''
    return v_in*(r2/(r1+r2)) #calculating output voltage


def find_power_dissipation(v_in,r1,r2):
    '''
    Calcualtes output power dissipation of a given resistor combination
    '''
    return v_in**2/(r1+r2) #calculating power dissipation


def find_resistor_combination(v_in,desired_v_out,tolerance,resistor_list):
    '''
    Find the suitable resistor combination with minimum power 
    '''
    #holds the values at minimum power dissipation
    min_power_dissipation=-1
    final_r1=0
    final_r2=0

    for i,r1 in enumerate(resistor_list): #choosing r1
        
        for j,r2 in enumerate(resistor_list): #choosing r2
            
            if i==j: #filter out repetition of resistors
                continue

            v_out=find_v_out(v_in,r1,r2) #output voltage
            
            if abs(v_out-desired_v_out)<=tolerance: #executes if v_out is within the tolerance
                power_dissipation=find_power_dissipation(v_in,r1,r2)

                #tracking the case of minimum poewr dissipation and the resistors at that instance
                if min_power_dissipation==-1 or power_dissipation<min_power_dissipation:
                    min_power_dissipation=power_dissipation
                    final_r1=r1
                    final_r2=r2
                    
    return final_r1,final_r2


def write_to_output_file(output_file_name,final_r1,final_r2):
    '''
    Print the resistor combination to output file
    '''
    #opening output file to write the rasistor combination
    with open(output_file_name,'w') as output_file:
        output_file.write(f'{final_r1}, {final_r2}')


def find_v_new(v_in,r1,r2,r_load):
    '''
    Calculate new output voltage when load is connected
    '''
    r_parallel=r_load*r2/(r2+r_load) #equivelent resistance of load and r2 
    return v_in*r_parallel/(r1+r_parallel) #new output voltage


def plot_graph(final_r1,final_r2):
    '''
    Print the resistor combination to output file
    '''
    load_list = list(range(10, 1001, 10))
    v_new_list=[find_v_new(v_in,final_r1,final_r2,r_load) for r_load in load_list]

    #plot graph
    plt.plot(load_list,v_new_list)
    plt.title('Voltage vs Resistance')
    plt.xlabel('Resistance (ohms)')
    plt.ylabel('Voltage (V)')
    plt.grid(True)
    plt.show()


############################################################################################
# Main

#Calling the functions  
v_in,desired_v_out,tolerance,resistor_list=read_input_file(input_file_name)

if None not in (v_in, desired_v_out, tolerance, resistor_list):
    final_r1,final_r2=find_resistor_combination(v_in,desired_v_out,tolerance,resistor_list)
    write_to_output_file(output_file_name,final_r1,final_r2)
    plot_graph(final_r1,final_r2)


################################################################################
# Please do not edit anything below this line.
evaluate_lab9()

##################### End of the programme #####################################
