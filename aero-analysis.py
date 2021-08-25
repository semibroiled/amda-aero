%% Aero Wertanalyse 
% 
%% Files Importieren 
% Import data files from the four iterative version

data1 = readmatrix('data1.xlsx'); %DATA_v1_gerade_SeiteParabel_GurneyFlap_AbstandGross.xlsx
data2 = readmatrix('data2.xlsx'); %DATA_v2_gerade_SeiteGanz_GurneyFlap_AbstandGross.xlsx
data3 = readmatrix('data3.xlsx'); %DATA_v3_gerade_SeiteSchraeg_GurneyFlap_AbstandGross.xlsx
data4 = readmatrix('data4.xlsx'); %DATA_v4_gerade_SeiteSchraegCutUnten_GurneyFlap_AbstandGross.xlsx

%Rename Files names to data1, data2, data3 and data4 for their Versions
%respectively for easier import handling
%Change name in Brackets to accommodate usage as seen fit
%% Arrays Sortieren
% Data 4
% Sort-Out individual Arrays from data4. Display Means for each relevant Array.



%Indiviudally Sorted Arrays from Column of Datalists
%Uncomment for usage when need arises
%Iteration_4 = data4(:,1);

%First Column of Iteration Values

%DownforceMonitor03_4 = data4(:,2);
%Downforce_DiffusorMonitor03_4 = data4(:,3);
%Downforce_FrontFluegelMonitor03_4 = data4(:,4);
%Downforce_HeckFluegelMonitor03_4 = data4(:,5);
%Downforce_HIMonitor03_4 = data4(:,6);
%Downforce_SeitenKastenMonitor03_4 = data4(:,7);
%Downforce_SeitenKasten_FlapMonitor03_4= data4(:,8);
%Downforce_SeitenKasten_MainMonitor03_4 = data4(:,9);
%Downforce_VOMonitor03_4 = data4(:,10);

%Columns Containing Downforce Values, from left to right in order of
% - Downforce Monitor, Diffusor Monitor, Front Fluege Monitor, Heck Fluege
% Monitor, HI Monitor, SeitenKasten Monitor, SeitenKasten Flap Monitor,
% Seiten Kasten Main Monitor, VO Monitor /- 

%CxMonitor04_4 = data4(:,11);
%CzMonitor04_4 = data4(:,12);

%Columns Containing C Monitors in order of - Cx, Cz /-

%LuftwiderstandMonitor04_4 = data4(:,13);
%Luftwiderstand_FrontfluegelMonitor04_4 = data4(:,14);
%Luftwiderstand_HeckfluegelMonitor04_4 = data4(:,15);
%Luftwiderstand_SeitenKastenMonitor04_4 = data4(:,16);
%Luftwiderstand_SeitenKasten_FlapMonitor04_4 = data4(:,17);
%Luftwiderstand_SeitenKasten_MainMonitor04_4 = data4(:,18);

%Columns Containing Luftwiderstand Values in order of - Luftwiderstand
%Monitor, Front Fluege Monitor, Heckfluege Monitor, Seiten Kasten Monitor,
%Seiten Kasten Flap Monitor, Seiten Kasten Main Monitor /-

%Massflow_KMMonitor05_4 = data4(:,19);

%Column Containing Massflow Values from KM Monitor

%EffizienzMonitor06_4 = data4(:,20);
%Effizienz_DiffusorMonitor06_4 = data4(:,21);
%Effizienz_FrontFluegeMonitor06_4 = data4(:,22);
%Effizienz_HeckFluegeMonitor06_4 = data4(:,23);
%Effizienz_SeitenKastenMonitor06_4 = data4(:,24);

%Columns Containing Effizienz Values in order of - Effizienz Monitor,
%Diffusor Monitor, Front Fluege Monitor, Heck Fluege Monitor, Seiten Kasten
%Monitor /-

%Iteration2_4 = data4(:,25);

%Column of Second Iteration Values, purpose and function unknown

%Bunched Multidimensional Matrices from data4

downforce_4 = data4(:, [2:10]);

%Columns Containing Downforce Values, from left to right in order of
% - Downforce Monitor, Diffusor Monitor, Front Fluege Monitor, Heck Fluege
% Monitor, HI Monitor, SeitenKasten Monitor, SeitenKasten Flap Monitor,
% Seiten Kasten Main Monitor, VO Monitor /- 

c_4 = data4(:, [11 12]); %Columns Containing C Monitors in order of - Cx, Cz /-

luftwiderstand_4 = data4(:, [13:18]);

%Columns Containing Luftwiderstand Values in order of - Luftwiderstand
%Monitor, Front Fluege Monitor, Heckfluege Monitor, Seiten Kasten Monitor,
%Seiten Kasten Flap Monitor, Seiten Kasten Main Monitor /-

massflow_4 = data4(:,19); %Column Containing Massflow Values from KM Monitor

effizienz_4 = data4(:, [20:24]);


%Columns Containing Effizienz Values in order of - Effizienz Monitor,
%Diffusor Monitor, Front Fluege Monitor, Heck Fluege Monitor, Seiten Kasten
%Monitor /-


%Means for Last 50 Iterations 


%Calculate Mean along Colums aka dim 1

m_downforce_4 = mean(downforce_4([end-50:end],:))
%Columns Containing Downforce Means, from left to right in order of
% - Downforce Monitor, Diffusor Monitor, Front Fluege Monitor, Heck Fluege
% Monitor, HI Monitor, SeitenKasten Monitor, SeitenKasten Flap Monitor,
% Seiten Kasten Main Monitor, VO Monitor /- 

m_c_4 = mean(c_4([end-50:end],:)) %Columns Containing C Monitors Means in order of - Cx, Cz /-

m_luftwiderstand_4 = mean(luftwiderstand_4([end-50:end],:))


%Columns Containing Luftwiderstand Means in order of - Luftwiderstand
%Monitor, Front Fluege Monitor, Heckfluege Monitor, Seiten Kasten Monitor,
%Seiten Kasten Flap Monitor, Seiten Kasten Main Monitor /-

m_massflow_4 = mean(massflow_4([end-50:end],:)) %Column Containing Massflow Means from KM Monitor

m_effizienz_4 = mean(effizienz_4([end-50:end],:))

%Columns Containing Effizienz Means in order of - Effizienz Monitor,
%Diffusor Monitor, Front Fluege Monitor, Heck Fluege Monitor, Seiten Kasten
%Monitor /-



% Data 3
% Sort-Out individual Arrays from data3. Display Means for each relevant Array.



%Indiviudally Sorted Arrays from Column of Datalists
%Uncomment for usage as needed
%Iteration_3 = data3(:,1);

%First Column of Iteration Values

%DownforceMonitor03_3 = data3(:,2);
%Downforce_DiffusorMonitor03_3 = data3(:,3);
%Downforce_FrontFluegelMonitor03_3 = data3(:,4);
%Downforce_HeckFluegelMonitor03_3 = data3(:,5);
%Downforce_HIMonitor03_3 = data3(:,6);
%Downforce_SeitenKastenMonitor03_3 = data3(:,7);
%Downforce_SeitenKasten_FlapMonitor03_3= data3(:,8);
%Downforce_SeitenKasten_MainMonitor03_3 = data3(:,9);
%Downforce_VOMonitor03_3 = data3(:,10);

%Columns Containing Downforce Values, from left to right in order of
% - Downforce Monitor, Diffusor Monitor, Front Fluege Monitor, Heck Fluege
% Monitor, HI Monitor, SeitenKasten Monitor, SeitenKasten Flap Monitor,
% Seiten Kasten Main Monitor, VO Monitor /- 

%CxMonitor04_3 = data3(:,11);
%CzMonitor04_3 = data3(:,12);

%Columns Containing C Monitors in order of - Cx, Cz /-

%LuftwiderstandMonitor04_3 = data3(:,13);
%Luftwiderstand_FrontfluegelMonitor04_3 = data3(:,14);
%Luftwiderstand_HeckfluegelMonitor04_3 = data3(:,15);
%Luftwiderstand_SeitenKastenMonitor04_3 = data3(:,16);
%Luftwiderstand_SeitenKasten_FlapMonitor04_3 = data3(:,17);
%Luftwiderstand_SeitenKasten_MainMonitor04_3 = data3(:,18);

%Columns Containing Luftwiderstand Values in order of - Luftwiderstand
%Monitor, Front Fluege Monitor, Heckfluege Monitor, Seiten Kasten Monitor,
%Seiten Kasten Flap Monitor, Seiten Kasten Main Monitor /-

%Massflow_KMMonitor05_3 = data3(:,19);

%Column Containing Massflow Values from KM Monitor

%EffizienzMonitor06_3 = data3(:,20);
%Effizienz_DiffusorMonitor06_3 = data3(:,21);
%Effizienz_FrontFluegeMonitor06_3 = data3(:,22);
%Effizienz_HeckFluegeMonitor06_3 = data3(:,23);
%Effizienz_SeitenKastenMonitor06_3 = data3(:,24);

%Columns Containing Effizienz Values in order of - Effizienz Monitor,
%Diffusor Monitor, Front Fluege Monitor, Heck Fluege Monitor, Seiten Kasten
%Monitor /-

%Iteration2_3 = data3(:,25);

%Column of Second Iteration Values, purpose and function unknown

%Bunched Multidimensional Matrices from data4

downforce_3 = data3(:, [2:10]);

%Columns Containing Downforce Values, from left to right in order of
% - Downforce Monitor, Diffusor Monitor, Front Fluege Monitor, Heck Fluege
% Monitor, HI Monitor, SeitenKasten Monitor, SeitenKasten Flap Monitor,
% Seiten Kasten Main Monitor, VO Monitor /- 

c_3 = data3(:, [11 12]); %Columns Containing C Monitors in order of - Cx, Cz /-

luftwiderstand_3 = data3(:, [13:18]);

%Columns Containing Luftwiderstand Values in order of - Luftwiderstand
%Monitor, Front Fluege Monitor, Heckfluege Monitor, Seiten Kasten Monitor,
%Seiten Kasten Flap Monitor, Seiten Kasten Main Monitor /-

massflow_3 = data3(:,19); %Column Containing Massflow Values from KM Monitor

effizienz_3 = data3(:, [20:24]);


%Columns Containing Effizienz Values in order of - Effizienz Monitor,
%Diffusor Monitor, Front Fluege Monitor, Heck Fluege Monitor, Seiten Kasten
%Monitor /-


%Means for Last 50 Iterations 


%Calculate Mean along Colums aka dim 1

m_downforce_3 = mean(downforce_3([end-50:end],:))
%Columns Containing Downforce Means, from left to right in order of
% - Downforce Monitor, Diffusor Monitor, Front Fluege Monitor, Heck Fluege
% Monitor, HI Monitor, SeitenKasten Monitor, SeitenKasten Flap Monitor,
% Seiten Kasten Main Monitor, VO Monitor /- 

m_c_3 = mean(c_3([end-50:end],:)) %Columns Containing C Monitors Means in order of - Cx, Cz /-

m_luftwiderstand_3 = mean(luftwiderstand_3([end-50:end],:))


%Columns Containing Luftwiderstand Means in order of - Luftwiderstand
%Monitor, Front Fluege Monitor, Heckfluege Monitor, Seiten Kasten Monitor,
%Seiten Kasten Flap Monitor, Seiten Kasten Main Monitor /-

m_massflow_3 = mean(massflow_3([end-50:end],:)) %Column Containing Massflow Means from KM Monitor

m_effizienz_3 = mean(effizienz_3([end-50:end],:))

%Columns Containing Effizienz Means in order of - Effizienz Monitor,
%Diffusor Monitor, Front Fluege Monitor, Heck Fluege Monitor, Seiten Kasten
%Monitor /-
% Data 2
% Sort-Out individual Arrays from data2. Display Means for each relevant Array.



%Indiviudally Sorted Arrays from Column of Datalists
%Uncomment for usage as needed
%Iteration_2 = data2(:,1);

%First Column of Iteration Values

%DownforceMonitor03_2 = data2(:,2);
%Downforce_DiffusorMonitor03_2 = data2(:,3);
%Downforce_FrontFluegelMonitor03_2 = data2(:,4);
%Downforce_HeckFluegelMonitor03_2= data2(:,5);
%Downforce_HIMonitor03_2 = data2(:,6);
%Downforce_SeitenKastenMonitor03_2 = data2(:,7);
%Downforce_SeitenKasten_FlapMonitor03_2= data2(:,8);
%Downforce_SeitenKasten_MainMonitor03_2 = data2(:,9);
%Downforce_VOMonitor03_2 = data2(:,10);

%Columns Containing Downforce Values, from left to right in order of
% - Downforce Monitor, Diffusor Monitor, Front Fluege Monitor, Heck Fluege
% Monitor, HI Monitor, SeitenKasten Monitor, SeitenKasten Flap Monitor,
% Seiten Kasten Main Monitor, VO Monitor /- 

%CxMonitor04_2 = data2(:,11);
%CzMonitor04_2 = data2(:,12);

%Columns Containing C Monitors in order of - Cx, Cz /-

%LuftwiderstandMonitor04_2 = data2(:,13);
%Luftwiderstand_FrontfluegelMonitor04_2 = data2(:,14);
%Luftwiderstand_HeckfluegelMonitor04_2 = data2(:,15);
%Luftwiderstand_SeitenKastenMonitor04_2 = data2(:,16);
%Luftwiderstand_SeitenKasten_FlapMonitor04_2 = data2(:,17);
%Luftwiderstand_SeitenKasten_MainMonitor04_2 = data2(:,18);

%Columns Containing Luftwiderstand Values in order of - Luftwiderstand
%Monitor, Front Fluege Monitor, Heckfluege Monitor, Seiten Kasten Monitor,
%Seiten Kasten Flap Monitor, Seiten Kasten Main Monitor /-

%Massflow_KMMonitor05_2 = data2(:,19);

%Column Containing Massflow Values from KM Monitor

%EffizienzMonitor06_2 = data2(:,20);
%Effizienz_DiffusorMonitor06_2 = data2(:,21);
%Effizienz_FrontFluegeMonitor06_2 = data2(:,22);
%Effizienz_HeckFluegeMonitor06_2 = data2(:,23);
%Effizienz_SeitenKastenMonitor06_2 = data2(:,24);

%Columns Containing Effizienz Values in order of - Effizienz Monitor,
%Diffusor Monitor, Front Fluege Monitor, Heck Fluege Monitor, Seiten Kasten
%Monitor /-

%Iteration2_2 = data2(:,25);

%Column of Second Iteration Values, purpose and function unknown

%Bunched Multidimensional Matrices from data4

downforce_2 = data2(:, [2:10]);

%Columns Containing Downforce Values, from left to right in order of
% - Downforce Monitor, Diffusor Monitor, Front Fluege Monitor, Heck Fluege
% Monitor, HI Monitor, SeitenKasten Monitor, SeitenKasten Flap Monitor,
% Seiten Kasten Main Monitor, VO Monitor /- 

c_2 = data2(:, [11 12]); %Columns Containing C Monitors in order of - Cx, Cz /-

luftwiderstand_2 = data2(:, [13:18]);

%Columns Containing Luftwiderstand Values in order of - Luftwiderstand
%Monitor, Front Fluege Monitor, Heckfluege Monitor, Seiten Kasten Monitor,
%Seiten Kasten Flap Monitor, Seiten Kasten Main Monitor /-

massflow_2 = data2(:,19); %Column Containing Massflow Values from KM Monitor

effizienz_2 = data2(:, [20:24]);


%Columns Containing Effizienz Values in order of - Effizienz Monitor,
%Diffusor Monitor, Front Fluege Monitor, Heck Fluege Monitor, Seiten Kasten
%Monitor /-


%Means for Last 50 Iterations 


%Calculate Mean along Colums aka dim 1

m_downforce_2 = mean(downforce_2([end-50:end],:))
%Columns Containing Downforce Means, from left to right in order of
% - Downforce Monitor, Diffusor Monitor, Front Fluege Monitor, Heck Fluege
% Monitor, HI Monitor, SeitenKasten Monitor, SeitenKasten Flap Monitor,
% Seiten Kasten Main Monitor, VO Monitor /- 

m_c_2 = mean(c_2([end-50:end],:)) %Columns Containing C Monitors Means in order of - Cx, Cz /-

m_luftwiderstand_2 = mean(luftwiderstand_2([end-50:end],:))


%Columns Containing Luftwiderstand Means in order of - Luftwiderstand
%Monitor, Front Fluege Monitor, Heckfluege Monitor, Seiten Kasten Monitor,
%Seiten Kasten Flap Monitor, Seiten Kasten Main Monitor /-

m_massflow_2 = mean(massflow_2([end-50:end],:)) %Column Containing Massflow Means from KM Monitor

m_effizienz_2 = mean(effizienz_2([end-50:end],:))

%Columns Containing Effizienz Means in order of - Effizienz Monitor,
%Diffusor Monitor, Front Fluege Monitor, Heck Fluege Monitor, Seiten Kasten
%Monitor /-
% Data 1
% Sort-Out individual Arrays from data1. Display Means for each relevant Array.



%Indiviudally Sorted Arrays from Column of Datalists
%Uncomment for usage as needed
%Iteration_1 = data1(:,1);

%First Column of Iteration Values

%DownforceMonitor03_1 = data1(:,2);
%Downforce_DiffusorMonitor03_1 = data1(:,3);
%Downforce_FrontFluegelMonitor03_1 = data1(:,4);
%Downforce_HeckFluegelMonitor03_1= data1(:,5);
%Downforce_HIMonitor03_1 = data1(:,6);
%Downforce_SeitenKastenMonitor03_1 = data1(:,7);
%Downforce_SeitenKasten_FlapMonitor03_1= data1(:,8);
%Downforce_SeitenKasten_MainMonitor03_1 = data1(:,9);
%Downforce_VOMonitor03_1 = data1(:,10);

%Columns Containing Downforce Values, from left to right in order of
% - Downforce Monitor, Diffusor Monitor, Front Fluege Monitor, Heck Fluege
% Monitor, HI Monitor, SeitenKasten Monitor, SeitenKasten Flap Monitor,
% Seiten Kasten Main Monitor, VO Monitor /- 

%CxMonitor04_1 = data1(:,11);
%CzMonitor04_1 = data1(:,12);

%Columns Containing C Monitors in order of - Cx, Cz /-

%LuftwiderstandMonitor04_1 = data1(:,13);
%Luftwiderstand_FrontfluegelMonitor04_1 = data1(:,14);
%Luftwiderstand_HeckfluegelMonitor04_1 = data1(:,15);
%Luftwiderstand_SeitenKastenMonitor04_1 = data1(:,16);
%Luftwiderstand_SeitenKasten_FlapMonitor04_1 = data1(:,17);
%Luftwiderstand_SeitenKasten_MainMonitor04_1 = data1(:,18);

%Columns Containing Luftwiderstand Values in order of - Luftwiderstand
%Monitor, Front Fluege Monitor, Heckfluege Monitor, Seiten Kasten Monitor,
%Seiten Kasten Flap Monitor, Seiten Kasten Main Monitor /-

%Massflow_KMMonitor05_1 = data1(:,19);

%Column Containing Massflow Values from KM Monitor

%EffizienzMonitor06_1 = data1(:,20);
%Effizienz_DiffusorMonitor06_1 = data1(:,21);
%Effizienz_FrontFluegeMonitor06_1 = data1(:,22);
%Effizienz_HeckFluegeMonitor06_1 = data1(:,23);
%Effizienz_SeitenKastenMonitor06_1 = data1(:,24);

%Columns Containing Effizienz Values in order of - Effizienz Monitor,
%Diffusor Monitor, Front Fluege Monitor, Heck Fluege Monitor, Seiten Kasten
%Monitor /-

%Iteration2_1 = data1(:,25);

%Column of Second Iteration Values, purpose and function unknown

%Bunched Multidimensional Matrices from data4

downforce_1 = data1(:, [2:10]);

%Columns Containing Downforce Values, from left to right in order of
% - Downforce Monitor, Diffusor Monitor, Front Fluege Monitor, Heck Fluege
% Monitor, HI Monitor, SeitenKasten Monitor, SeitenKasten Flap Monitor,
% Seiten Kasten Main Monitor, VO Monitor /- 

c_1 = data1(:, [11 12]); %Columns Containing C Monitors in order of - Cx, Cz /-

luftwiderstand_1 = data1(:, [13:18]);

%Columns Containing Luftwiderstand Values in order of - Luftwiderstand
%Monitor, Front Fluege Monitor, Heckfluege Monitor, Seiten Kasten Monitor,
%Seiten Kasten Flap Monitor, Seiten Kasten Main Monitor /-

massflow_1 = data1(:,19); %Column Containing Massflow Values from KM Monitor

effizienz_1 = data1(:, [20:24]);


%Columns Containing Effizienz Values in order of - Effizienz Monitor,
%Diffusor Monitor, Front Fluege Monitor, Heck Fluege Monitor, Seiten Kasten
%Monitor /-


%Means for Last 50 Iterations 


%Calculate Mean along Colums aka dim 1

m_downforce_1 = mean(downforce_1([end-50:end],:))
%Columns Containing Downforce Means, from left to right in order of
% - Downforce Monitor, Diffusor Monitor, Front Fluege Monitor, Heck Fluege
% Monitor, HI Monitor, SeitenKasten Monitor, SeitenKasten Flap Monitor,
% Seiten Kasten Main Monitor, VO Monitor /- 

m_c_1 = mean(c_1([end-50:end],:)) %Columns Containing C Monitors Means in order of - Cx, Cz /-

m_luftwiderstand_1 = mean(luftwiderstand_1([end-50:end],:))


%Columns Containing Luftwiderstand Means in order of - Luftwiderstand
%Monitor, Front Fluege Monitor, Heckfluege Monitor, Seiten Kasten Monitor,
%Seiten Kasten Flap Monitor, Seiten Kasten Main Monitor /-

m_massflow_1 = mean(massflow_1([end-50:end],:)) %Column Containing Massflow Means from KM Monitor

m_effizienz_1 = mean(effizienz_1([end-50:end],:))

%Columns Containing Effizienz Means in order of - Effizienz Monitor,
%Diffusor Monitor, Front Fluege Monitor, Heck Fluege Monitor, Seiten Kasten
%Monitor /-