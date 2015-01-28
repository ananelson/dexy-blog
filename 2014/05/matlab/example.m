%% Hello
% This is an example document.

%% Patients

%%
% Create a table from individual workspace variables.
load patients
patients = table(LastName,Gender,Age,Height,Weight,Smoker,Systolic,Diastolic);

%%
% Select the rows for patients who smoke, and a subset of the variables.
smokers = patients(patients.Smoker == true, {'LastName' 'Gender' 'Systolic' 'Diastolic'})

%%
% Convert the two blood pressure variables into a single variable.
patients.BloodPressure = [patients.Systolic patients.Diastolic];
patients(:,{'Systolic' 'Diastolic'}) = [];

%%
% Pick out two specific patients by the LastName variable.
patients(ismember(patients.LastName,{'Smith' 'Jones'}), :)
