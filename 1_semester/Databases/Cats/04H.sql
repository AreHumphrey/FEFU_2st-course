SELECT DISTINCT BEASTS.NAME AS `BEAST.NAME`, 
COUNT(DISTINCT PLACES.CONT) AS COUNT 
FROM ENCOUNTERS 
LEFT JOIN BEASTS ON BEASTS.ROWI = ENCOUNTERS.BEAST
JOIN PLACES ON PLACES.ROWI = ENCOUNTERS.PLACE
GROUP BY BEASTS.NAME
HAVING COUNT(DISTINCT PLACES.CONT) > 1
ORDER BY BEASTS.NAME ASC;
