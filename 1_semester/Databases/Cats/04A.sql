SELECT 
    MIN(Value) AS MinValue,
    MAX(Value) AS MaxValue,
    SUM(Value) AS SumValue,
    COUNT(Value) AS CountValue,
    AVG(Value) AS AvgValue
FROM Numbers;
