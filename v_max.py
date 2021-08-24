import numpy as np

def v_max(P, C_d, A):
    ''' This function outputs the __Theoretical Top Speed__ of a car in km/h
     The passed inputs are:
     - P, Engine Power in kW
     - C_d, Drag Coefficient
     - A, Reference Frontal Area in m^2

     The Basis Formula is; P = (C_d*A*v_max^3)/1.633
     Rearranging this provides us with the skeleton for our function
     name => v_max = ((P*1.633)/(Cd*A))^(1/3), where the v_max is in m/s

     Given the v_max, we can also output it in km/h by multiplying by 3.6 
     
     WARNING! You need to import numpy as np 
     '''


    #v_max_ms = nthroot(((P*1000*1.633)/(Cd*A)), 3); => why is there a 1000 here? Ah! From the kW 
    v_max_ms = np.cbrt((P*1000*1.633) / (C_d*A)) 

    v_max_kmh = v_max_ms*3.6

    return v_max_ms, v_max_kmh

P = float(input('Enter Engine Power in kW:\n'))
cd = float(input('Enter Drag Coefficient:\n'))
A = float(input('Enter Frontal Area in sq. m:\n'))

v_ms, v_kmh = v_max(P, cd, A)

print(f'The theoretical top speed for a Engine Power of {P} kW, {cd} Drag Coefficeient and {A} sq. m. Frontal Area is:\n {v_ms:.3f} m/s which is {v_kmh:.3f} km/h')
   
