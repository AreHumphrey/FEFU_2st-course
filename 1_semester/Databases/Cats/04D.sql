SELECT ProductName
FROM Sales
GROUP BY ProductName
ORDER BY SUM(QuantitySold) DESC 
LIMIT 10;
