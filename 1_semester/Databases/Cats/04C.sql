SELECT P.Title AS Title, C.Name AS CategoryName, P.SellingPrice AS SellingPrice
FROM Products P
    LEFT JOIN (SELECT PI.ProductID, SUM(PI.QuantityBought) AS SumBought FROM PurchaseItems AS PI GROUP BY PI.ProductID) AS Bought ON P.ID = Bought.ProductID
    LEFT JOIN (SELECT S.ProductID, SUM(S.QuantitySold) AS SumSold FROM SalesItems AS S GROUP BY S.ProductID) AS Sold ON P.ID = Sold.ProductID
    LEFT JOIN Categories C ON P.CategoryID = C.ID
WHERE SumBought = SumSold OR P.ID IS NULL
ORDER BY SellingPrice DESC;
