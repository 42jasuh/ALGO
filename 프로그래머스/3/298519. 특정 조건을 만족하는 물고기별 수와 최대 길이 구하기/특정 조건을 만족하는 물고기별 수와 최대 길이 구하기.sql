SELECT 
    COUNT(*) AS FISH_COUNT, 
    MAX(length) AS MAX_LENGTH, 
    fish_type 
FROM 
    fish_info 
GROUP BY 
    fish_type 
HAVING 
    AVG(length) >= 33
order by fish_type;