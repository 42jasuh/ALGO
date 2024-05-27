SELECT 
    COUNT(*) AS FISH_COUNT, 
    MAX(IFNULL(LENGTH, 10)) AS MAX_LENGTH, 
    fish_type 
FROM 
    fish_info 
GROUP BY 
    fish_type 
HAVING 
    AVG(IFNULL(LENGTH, 10)) >= 33 
ORDER BY fish_type;
