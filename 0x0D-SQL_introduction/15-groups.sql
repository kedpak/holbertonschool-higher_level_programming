-- script lists the number of records with same score on table
-- counts number of each score occurence in second_table
SELECT score, COUNT(*) AS number FROM second_table
       GROUP BY score, number ORDER BY number DESC;
