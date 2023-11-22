SELECT Employees.FullName AS EmployeeFullNames, ROUND(SUM(Positions.Salary * Salaries.SalaryPercentage)) AS SumSalary
FROM Employees
LEFT JOIN Salaries ON Employees.ID = Salaries.EmployeeID
LEFT JOIN Positions ON Positions.ID = Salaries.PositionID
GROUP BY Employees.ID
HAVING SumSalary <
(SELECT ROUND(SUM(Positions.Salary * Salaries.SalaryPercentage)) /
(SELECT COUNT(DISTINCT Salaries.EmployeeID) FROM Employees)
FROM Employees
LEFT JOIN Salaries ON Employees.ID = Salaries.EmployeeID
LEFT JOIN Positions ON Positions.ID = Salaries.PositionID)
ORDER BY SumSalary ASC, EmployeeFullNames ASC;
