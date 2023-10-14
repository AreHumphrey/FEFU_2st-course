UPDATE Animals 
SET Sex = CASE 
WHEN Sex = 'male' THEN 'm' 
WHEN Sex = 'female' THEN 'w' 
ELSE 'unknown' 
END 
WHERE Sex IS NOT NULL;
