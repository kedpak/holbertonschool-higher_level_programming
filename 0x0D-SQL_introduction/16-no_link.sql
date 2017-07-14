-- write script that records table
-- Does not list rows without name value, displays name/score, in desc order
SELECT score, name FROM second_table
       WHERE name IS NOT NULL AND name != "" ORDER BY score DESC
