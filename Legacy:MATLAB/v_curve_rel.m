function v_curve_rel (m, u, Cl, A) 
%% V_CURVE_REL *Relative Performance über Kurvenradius* 
%% *Relative Performance (as in Thesis)*
% 
% 
% *Formell*
% 
% *v = sqrt( (m*g) / ( (m/ (u*R) ) - 0.5*p*Cl*A ) )*
% 
% *Warmup*
% 
% *m = %Insert Mass of car in [kg]*
% 
% *g= %Insert Gravitational (Constant) Acceleration on Earth in [m/s^2]*
% 
% *u = %Insert Coefficient of Friction in []*
% 
% *R = %Insert Radius of Curvature at Corners in [m]*
% 
% *p = %insert Density of Air in [kg/m^3]*
% 
% *Cl = %Insert Lift Coefficient  in []*
% 
% *A = %Refernce Frontal Area in [m^2]*
% 
% 
% 
% *Assumption: Coefficient of Friction is constant*
% 
% 
% 
% *Function outputs a plot of Relative Performance against Cornering Radius*
    %
    
    g = 9.806675; %Avg. Gravitational Acceleration above Sealevel
    p = 1.2754; %IUPAC Standard for Dry Air at 274K and 100kPa 
    % in [kg/m^3]
    R = 4:30; %Thesis Range for Corner Radius 
   %m= mass of car in [kg]
   %u = coefficient of friction according to tyre specifications 
   %A = Reference Frontal Area in [m^2]
    
    v_0Cl_ms2 = sqrt( (m.*g) ./ ( ( m./ (u.*R) ) - (0.5.*p.*0.*A) ) );
    v_0Cl = v_0Cl_ms2 * 3.6;
    v_0Cl_rel = v_0Cl ./ v_0Cl ;
    %Control with No Downforce. !! Frage an Louis, ist Cl= 0 gleich wie No
    %Downforce die richtige Annahme? 
    
    v = sqrt( (m.*g) ./ ( ( m ./ (u.*R) ) - (0.5.*p.*Cl.*A) ) );
    v_curve_abs = v*3.6;
    v_curve_rel = v_curve_abs ./  v_0Cl;
    
    
    plot(R, v_curve_rel, 'b')
    hold on 
    plot(R, v_0Cl_rel, '--r')
    
    xlabel('Corner Radius, R [m]')
    ylabel('Relative Performance')
    title('Relative Performance in Relation to Curve Radius')
    legend('Input Cl', 'Cl=0') %Does Cl=0 really mean no downforce?
    axis tight
    hold off
    
    %Is there a way to make two separate graph ie another graph for
    %relative performance in the same function?
end
%% 
% 
% 
% 
% 
%