import numpy as np
import matplotlib.pyplot as plt

def v_curve(m, mu, C_l, A, g='Earth', rho='Standard'):

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
     Rearranging this provides us with the skeleton for our function

     The function outputs a plot of Relative Performance against a Cornering Radius

     Assumptions made are:
     - mu is a constant value
     
     WARNING! You need to import numpy as np  and matplotlib.pyplot as plt
     '''


    g_set = {'Earth': 9.806675, #Average Gravitational Acceleration above Sealevel
    }

    #it'd be cool to see a graph of comparison of cornering speeds for different planets and environments

    rho_set = {'Standard':1.2754, #IUPAC Standard for Dry Air at 274K and 100kPa in kg/m^3
    }

    R = np.arange(100) #Defined a Range of Values for R the Cornering Radius

    if 'earth' in g.lower():
        g = g_set['Earth']
    
    if 'standard' in rho.lower():
        rho = rho_set['Standard']

    #The Velocity at Cornering Radius with C_l = 0 i.e. no Downforce as control
    v_0Cl_ms = np.sqrt((m*g) / (m/(mu*R)-(0.5*rho*0*A)))
    v_0Cl_kmh = v_0Cl_ms * 3.6
    v_0Cl_rel = v_0Cl_kmh / v_0Cl_kmh
    
    v_wCl_ms = np.sqrt((m*g)/((m/(mu*R))-(0.5*rho*C_l*A)))
    v_wCl_kmh = v_wCl_ms * 3.6
    v_curve_abs = v_wCl_kmh.copy()
    
    
    v_wCl_rel = v_wCl_kmh /  v_0Cl_kmh
    v_curve_rel = v_wCl_rel.copy()


    plot(R, v_curve_rel, 'b')
    hold on 
    plot(R, v_0Cl_rel, '--r')
    
    xlabel('Corner Radius, R [m]')
    ylabel('Relative Performance')
    title('Relative Performance in Relation to Curve Radius')
    legend('Input Cl', 'Cl=0') %Does Cl=0 really mean no downforce?
    axis tight
    hold off

plot(R, v_curve_abs, 'b')
    hold on 
    plot(R, v_0Cl, '--r')
    
    xlabel('Corner Radius, R [m]')
    ylabel('Maximum Absolute Velocity, v [km/h]')
    title('Maximum Cornering Velocity in Relation to Curve Radius')
    legend('Input Cl', 'Cl=0') %Does Cl=0 really mean no downforce?
    axis tight
    return v_curve_abs, v_curve_rel


  

P = float(input('Enter Engine Power in kW:\n'))
cd = float(input('Enter Drag Coefficient:\n'))
A = float(input('Enter Frontal Area in sq. m:\n'))

v_ms, v_kmh = v_max(P, cd, A)

print(f'The theoretical top speed for a Engine Power of {P} kW, {cd} Drag Coefficeient and {A} sq. m. Frontal Area is:\n {v_ms:.3f} m/s which is {v_kmh:.3f} km/h')