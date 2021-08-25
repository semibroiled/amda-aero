import numpy as np

def v_curve(m, mu, C_l, A, g='Earth', rho='Standard', R='Placeholder'):

    ''' This function outputs the __Relatice and Absolute Performance__ of a car against a Cornering Radius
     The passed inputs are:
     - m, Mass of the car in kg
     - mu, Friction Coefficient according to Tyre Specifications 
     - C_l, Lift Coefficient
     - A, Reference Frontal Area in sq. m / m^2

     Moreover;
     - rho, Density of Air in kg/m^3
     - R, Curvature Radius at Corners in m
     - g, Gravitational Acceleration in m/s^2

     The Basis Formula is; v = sqrt([m*g]/[(m/(mu*R))- 0.5*p*Cl*A]) !# is something missing here?!!!

     Assumptions made are:
     - mu is a constant value
     
     WARNING! You need to import numpy as np
     '''


    g_set = {'Earth': 9.806675, #Average Gravitational Acceleration above Sealevel
    }

    #it'd be cool to see a graph of comparison of cornering speeds for different planets and environments

    rho_set = {'Standard':1.2754, #IUPAC Standard for Dry Air at 274K and 100kPa in kg/m^3
    }

    if 'placeholder' in R.lower():
        R = np.arange(5, 100, 5, dtype = float) #Defined a Range of Values for R the Cornering Radius

    if 'earth' in g.lower():
        g = g_set['Earth']
    
    if 'standard' in rho.lower():
        rho = rho_set['Standard']

    #The Velocity at Cornering Radius with C_l = 0 i.e. no Downforce as control
    v_0Cl_ms = np.sqrt( (m*g) / ( ( ( m/(mu*R) ) -(0.5*rho*0*A) ) ) )
    v_0Cl_kmh = v_0Cl_ms * 3.6
    v_0Cl_rel = v_0Cl_kmh / v_0Cl_kmh
    
    #Now with C_l
    v_wCl_ms = np.sqrt( (m*g) / ( ( (m/(mu*R))-(0.5*rho*C_l*A) ) ) )
    #print(((m/(mu*R))-(0.5*rho*C_l*A))>0 ) Need to check formulas and at least see if the formulas right, and jot down typical ranges of values and include example in docstring
    v_wCl_kmh = v_wCl_ms * 3.6
    v_curve_abs = v_wCl_kmh.copy()
    
    
    v_wCl_rel = v_wCl_kmh /  v_0Cl_kmh
    v_curve_rel = v_wCl_rel.copy()

    return v_curve_abs, v_curve_rel, v_0Cl_rel, R


  
if __name__ == '__main__':

    try:
        # m = float(input('Enter Mass in kg:\n'))
        # cl = float(input('Enter Lift Coefficient:\n'))
        # A = float(input('Enter Frontal Area in sq. m:\n'))
        # mu = float(input('Enter Friction Coefficient:\n'))
        # v_abs, v_rel, v_cont, R = v_curve(m, mu, cl, A)
        
        #For testing
        v_rel, v_abs, v_cont, R = v_curve(250, 0.8, 1, 5)

       # print(f'The Turning Speeds for Mass {m} kg, {cl} Lift Coefficeient, {mu} Friction Coefficient and {A} sq. m. Frontal Area is:\n')
        print('Cornering Radius\n', R)
        print('Control', v_cont)
        print('Relative Performance \n', v_rel)
        print('Absolute Performance\n', v_abs)
    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(te)