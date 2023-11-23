SELECT Department.ID, Alterego.Name, COUNT(Patient.Id) AS count
FROM Alterego
JOIN Patient ON Alterego.ID = Patient.Alterego
JOIN Department ON Department.ID = Patient.Department
GROUP BY Alterego.Name, Department.id
HAVING COUNT(Patient.ID) = (
SELECT MAX(count)
FROM (
SELECT Department.Id AS department_id, COUNT(Patient.Id) AS count
FROM Alterego
JOIN Patient ON Alterego.ID = Patient.Alterego
JOIN Department ON Department.id = Patient.Department
GROUP BY Patient.Alterego, Department.id
) AS otvet 

WHERE otvet.department_id = Department.Id
)
ORDER BY Department.ID ASC, Alterego.Name ASC LIMIT 2000;
