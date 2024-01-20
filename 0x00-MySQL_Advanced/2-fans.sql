-- This script ranks country origins of bands,
-- and orders them by the number of (non-unique) fans
SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
