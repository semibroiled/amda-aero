%% *Aero Top Speed Plot*
%% Top Speed over Drag Coefficient, Cd 
% Formell
% 
% P = (Cd*A*v^3)/1.633
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
% Function plots Theoretical Topspeed over a predefined range of Drag Coefficient 


function topspeed_plot(P,A)
    % P - Engine Power in [kW]
    % Cd - Drag Coefficient 
    % A - Frontal Area in [m^2]
    % Function plots Theoretical Topspeed over a predefined range of Drag Coefficient 
   Cd = 0:0.001:4 ; %Range of Cd allocating for all (ir)relevancy 
   % P = Engine Power in [kW]
   % A = Frontal Area in [m^2]
   v_max_ms = nthroot(((P*1000*1.633)./(Cd.*A)), 3);
   
   topspeed_plot = v_max_ms * 3.6;
  
   %Plotting topspeed and Cd over the predefined range of Cd
   %TO BE CHECKED: Does the graph make mathematical sense for increasing
   %Cd?? Frage an Louis
   
   plot(Cd, topspeed_plot,'b')
   ylabel('Theoretical Topspeed, v [km/h]')
   xlabel('Drag Coefficient, C^d')
   title('Topspeed Function over C^d')
   ylim([0, 300])

end




%% 
% Anmerkungen: 
% 
% 1)Should topspeed and v_max be combined or dispayed separately as is? Functions 
% based on varying P and A, since I didn't know their values. Was the demand to 
% form function on known P and A? If yes, the function need to be modified to 
% include them as constants as opposed to variables.
% 
% 
% 
% 2) Does the plot make sense mathematically or is there an error there somewhere?
% 
%