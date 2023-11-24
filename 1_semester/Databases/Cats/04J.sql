WITH summi AS (
    SELECT 
        s.id AS sale_id, 
        s.auto_id, 
        s.odometer AS now_odometer, 
        LAG(s.odometer) OVER(PARTITION BY s.auto_id ORDER BY s.date) AS previous_odometer
    FROM sellrecord s
)
SELECT a.model,
SUM(
CASE WHEN su.now_odometer < su.previous_odometer THEN su.previous_odometer - su.now_odometer ELSE 0 END
) AS probeg
FROM auto a
JOIN summi su ON a.id = su.auto_id
GROUP BY a.model
ORDER BY probeg DESC;
