WITH RankedIncidents AS (
    SELECT Specialists.FullName AS FullName, Incidents.Title AS IncidentTitle,
    ROW_NUMBER() OVER(PARTITION BY Specialists.ID ORDER BY Incidents.CreatedAt) AS IncidentRank,
    Specialists.Resolved AS WholeResolved
    FROM Specialists
    JOIN Assignment ON Specialists.ID = Assignment.SpecialistID
    JOIN Incidents ON Assignment.IncidentID = Incidents.ID
)
SELECT FullName, IncidentTitle
FROM RankedIncidents
WHERE IncidentRank > WholeResolved
AND IncidentRank <= 5;
