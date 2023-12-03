CREATE VIEW ShowITEmployees AS
  WITH RECURSIVE IT_Department AS (
    SELECT ID, FullName, PositionID, ChiefID
    FROM Employees
    WHERE PositionID IN (SELECT ID FROM Positions WHERE Title = 'PC Principal')

    UNION ALL

    SELECT e.ID, e.FullName, e.PositionID, e.ChiefID
    FROM Employees e
    JOIN IT_Department itd ON e.ChiefID = itd.ID
  )
  SELECT IT_Department.ID, IT_Department.FullName, Positions.Title AS Position, IT_Department.ChiefID
  FROM IT_Department
  LEFT JOIN Positions ON IT_Department.PositionID = Positions.ID;
