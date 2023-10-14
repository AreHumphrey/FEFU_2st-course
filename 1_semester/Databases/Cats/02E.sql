SELECT DISTINCT SUBSTRING(Author, 1, 1) AS Initials
FROM Books
INTO OUTFILE '/path/to/output/file.txt'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n';
