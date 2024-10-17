-- List Glam rock bands ranked by their longevity (lifespan in years until 2022)
SELECT 
    band_name,
    CASE
        -- If the band has split, calculate lifespan from formed year to split year
        WHEN split IS NOT NULL THEN (split - formed)
        -- If the band hasn't split, calculate lifespan from formed year to 2022
        ELSE (2022 - formed)
    END AS lifespan
FROM 
    metal_bands
WHERE 
    style = 'Glam rock'
ORDER BY 
    lifespan DESC;
