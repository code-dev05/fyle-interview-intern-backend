-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT COUNT(*)
FROM assignments
WHERE teacher_id = (
    SELECT teacher_id
    FROM (
        SELECT teacher_id, COUNT(*)
        FROM assignments
        WHERE state = 'GRADED'
        GROUP BY teacher_id
        ORDER BY COUNT(*) DESC
        LIMIT 1
    )
)
AND grade = 'A';
