function v_max(P,Cd,A)
%% V_MAX *Aero Top Speed Funktion*
%% Top Speed als Skalar 
% Für gegebenes Cd 
% 
% Formell
% 
% P = (Cd*A*v^3)/1.633
% 
% 
% 
% Warmup
% 
% P = %Insert Engine Power in [kW]
% 
% Cd = %Insert Drag Coefficient in []
% 
% A = %Insert Frontal Area in [m^2]
% 
% => v_max = ((P*1.633)/(Cd*A))^(1/3)
% 
% Assumption: Rolling Resistance has been ignored
% 
% Function outputs theoretical Topspeed in [km/h]
% 
% 
    % P - Engine Power in [kW]
    % Cd - Drag Coefficient 
    % A - Frontal Area in [m^2]
    % function outputs theoretical Topspeed in kmh
   
   %P = Engine Power in [kW];
   %A = Reference Frontal Area in [m^2]
   
   v_max_ms = nthroot(((P*1000*1.633)/(Cd*A)), 3);
   v_max = v_max_ms * 3.6
end
%% 
% Anmerkungen: Should topspeed and v_max be combined or dispayed separately 
% as is? Functions based on varying P and A, since I didn't know their values. 
% Was the demand to form function on known P and A? If yes, the function need 
% to be modified to include them as constants as opposed to variables.