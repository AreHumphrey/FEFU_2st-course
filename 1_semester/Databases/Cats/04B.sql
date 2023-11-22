SELECT Sellers.LastName || ' ' ||  Sellers.FirstName AS SellerFullName,
SUM(SalesItems.QuantitySold * Products.SellingPrice) AS TotalRevenue,
COUNT(DISTINCT SalesItems.SaleId) AS CountOfSales
FROM Sellers
JOIN Sales ON Sales.SellerID = Sellers.ID
JOIN SalesItems ON Sales.ID = SalesItems.SaleID
JOIN Products ON SalesItems.ProductID = Products.ID
GROUP BY Sellers.ID 
ORDER BY TotalRevenue DESC LIMIT 10;
