SELECT COUNT(*) AS TotalPeopleWithMI
FROM (
    SELECT Doctors.PersonalDataID AS PersonID
    FROM Doctors
    JOIN PersonalData ON Doctors.PersonalDataID = PersonalData.ID
    LEFT JOIN MedicalInsurance ON PersonalData.MedicalInsuranceID = MedicalInsurance.ID AND MedicalInsurance.Status = 'active'
    WHERE MedicalInsurance.ID IS NOT NULL

    UNION

    SELECT Patients.PersonalDataID AS PersonID
    FROM Patients
    JOIN PersonalData ON Patients.PersonalDataID = PersonalData.ID
    LEFT JOIN MedicalInsurance ON PersonalData.MedicalInsuranceID = MedicalInsurance.ID AND MedicalInsurance.Status = 'active'
    WHERE MedicalInsurance.ID IS NOT NULL
) AS PeopleWithMI;
