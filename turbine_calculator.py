import numpy as np
from tabulate import tabulate


##########Input Data#################
##########Full-Scale
D = 178.3
U_inf = 11.4
c_70 = 4.392
#Chose one of these variables
#TSR = 7.0
omega = 0.959
#U_tip = 90.0
rho = 1.225
mu = 1.789E-5
calculate_full_turbine = True

##########Geometric Scaling
calculate_geometrical_scaling = True
scale_factor = 1/60

##########Froude Scaling
calculate_froude_scaling = True
scale_factor = 1/60










#Calculation of properties of full scale
if calculate_geometrical_scaling:
    R = D/2
    R_70 = R*0.7
    
    if 'TSR' in vars():
        U_tip = TSR*U_inf
        omega = U_tip/R
    elif 'omega' in vars():
        U_tip = omega*R
        TSR = U_tip/U_inf
    elif 'U_tip' in vars():
        TSR = U_tip/U_inf
        omega = U_tip/R

    U_70 = np.sqrt(U_inf**2 + (0.7*U_tip)**2)
    
    omega_RPM = omega/(2*np.pi)*60

    Re_70 = (rho*c_70*U_70)/mu

    data_full_turbine = [['Diameter'       , D        ,     'm'],
                         ['Radius'         , R        ,     'm'],
                         ['Radius @ 70%'   , R_70     ,     'm'],
                         ['Chord  @ 70%'   , c_70     ,     'm'],
                         ['-'              , 0.0      ,     '-'],
                         ['Wind Speed'     , U_inf    ,   'm/s'],
                         ['Tip Speed'      , U_tip    ,   'm/s'],
                         ['Tip Speed @ 70%', U_70     ,   'm/s'],
                         ['Angular Speed'  , omega    , 'rad/s'],
                         ['Angular Speed'  , omega_RPM,   'RPM'],
                         ['TSR'            , TSR      ,     '-'],
                         ['-'              , 0.0      ,     '-'],
                         ['Re @ 70%'       , Re_70    ,     '-']]

    print(tabulate(data_full_turbine, headers=['FULL-SCALE PROPERTY', 'VALUE', 'UNIT'], tablefmt="fancy_grid", floatfmt=(".3f")))





#Calculation of properties for pure geometrical scaling
if calculate_froude_scaling:
    D_geo = D*scale_factor    
    R_geo = R*scale_factor
    R_70_geo = R_70*scale_factor
    c_70_geo = c_70*scale_factor

    U_inf_froude = U_inf*np.sqrt(scale_factor)
        
        
    if 'U_tip' in vars():
      U_tip_froude = U_tip*np.sqrt(scale_factor)      
    elif 'TSR' in vars():
      U_tip_froude = TSR*U_inf_froude

    omega_froude = U_tip_froude/R_geo


    U_70_froude = np.sqrt(U_inf_froude**2 + (0.7*U_tip_froude)**2)
    
    omega_RPM_froude = omega_froude/(2*np.pi)*60

    Re_70_froude = (rho*c_70_geo*U_70_froude)/mu

    data_model_turbine_fro = [['Diameter'       , D_geo           ,     'm'],
                              ['Radius'         , R_geo           ,     'm'],
                              ['Radius @ 70%'   , R_70_geo        ,     'm'],
                              ['Chord  @ 70%'   , c_70_geo        ,     'm'],
                              ['-'              , 0.0             ,     '-'],
                              ['Wind Speed'     , U_inf_froude    ,   'm/s'],
                              ['Tip Speed'      , U_tip_froude    ,   'm/s'],
                              ['Tip Speed @ 70%', U_70_froude     ,   'm/s'],
                              ['Angular Speed'  , omega_froude    , 'rad/s'],
                              ['Angular Speed'  , omega_RPM_froude    ,   'RPM'],
                              ['TSR'            , TSR             ,     '-'],
                              ['-'              , 0.0             ,     '-'],
                              ['Re @ 70%'       , Re_70_froude    ,     '-']]

    print(tabulate(data_model_turbine_fro, headers=['MODEL-SCALE PROPERTY (FROUDE)', 'VALUE', 'UNIT'], tablefmt="fancy_grid", floatfmt=(".3f")))

