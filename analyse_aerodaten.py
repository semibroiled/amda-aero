% SKRIPT zur automatischen Bestimmung der Mittelwerte (�ber Iterationen) einer Aero-Datenbank
clear;

%Parameter
AnzahlMittelung = 400;
GrenzStandardabweichung = 0.5;


%Lese Namen der Spalten aus
sheet = fopen('SaveDataToCSV_DataToCSV_01500.csv');
tline = fgetl(sheet);
splitLineAtKomma = strsplit(tline,',');
fclose(sheet);

%Lese Aerodaten aus
AeroData = csvread('SaveDataToCSV_DataToCSV_01500.csv');
AeroData = AeroData(2:end, :);

%Bestimme Mittelwert �ber letzten x Iterationen und bestimme deren Standardabweichung
Mean_AeroData = mean(AeroData(end-AnzahlMittelung:end,:));
StdAbweichung_AeroData = sqrt(var(AeroData(end-AnzahlMittelung:end,:)));

%Schreibe ein Ausgabefile
filename = "AeroDaten_Auswertung.txt";
fid = fopen (filename, "w");

fprintf(fid, '%s\n', ["AeroDaten wurden ueber ", num2str(AnzahlMittelung)," Iterationen gemittelt."]);
fprintf(fid, '%s\n', ["Die Varianzgrenze betraegt ", num2str(GrenzStandardabweichung),"."]);
fprintf(fid, '%s\n', " ");

lengthNames = size(splitLineAtKomma);
for i=1:lengthNames(2)
  spezName = strsplit(splitLineAtKomma{i},' ');
  spezVar = StdAbweichung_AeroData(i);
  if(spezVar < GrenzStandardabweichung)   %Alle Werte die kaum Schwanken  
    fprintf(fid, '%s\n', [spezName{1}(2:end), " = ", num2str(Mean_AeroData(i))]);
  elseif (strfind(spezName{1}(2:end),'Iteration'))
    %do nothing
  else
    fprintf(fid, '%s\n', ["--> VAR = ",num2str(spezVar)," <-- ",spezName{1}(2:end), " = ", num2str(Mean_AeroData(i))]);
  end
  
end

fclose (fid);


