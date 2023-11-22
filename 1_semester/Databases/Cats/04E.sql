SELECT
    Departments.Name AS DepartmentName,
    COUNT(Employees.ID) AS TotalPeople
FROM
    Departments
LEFT JOIN
    Employees ON Departments.ID = Employees.DepartmentID
GROUP BY
    Departments.ID;
