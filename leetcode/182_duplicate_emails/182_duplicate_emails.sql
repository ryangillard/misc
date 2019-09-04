# Write your MySQL query statement below
SELECT
    Email
FROM
    Person
GROUP BY
    Email
HAVING
    COUNT(Email) > 1


SELECT
    Email
FROM (
    SELECT
        Email,
        COUNT(*) AS cnt
    FROM
        Person
    GROUP BY
        Email) AS A
WHERE
    cnt > 1