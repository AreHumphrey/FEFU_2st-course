SELECT a.model, SUM(s1.odometer - s2.odometer) AS total_mileage_tampering
FROM AUTO AS a
JOIN sellrecord AS s1 ON a.id = s1.auto_id
JOIN sellrecord AS s2 ON a.id = s2.auto_id AND s2.date < s1.date
GROUP BY a.model
ORDER BY total_mileage_tampering DESC;
