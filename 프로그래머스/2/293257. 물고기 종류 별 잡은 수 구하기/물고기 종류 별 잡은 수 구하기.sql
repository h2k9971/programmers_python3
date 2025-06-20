-- 코드를 작성해주세요
SELECT COUNT(N.FISH_NAME) AS FISH_COUNT, N.FISH_NAME
    FROM FISH_INFO AS F
    INNER JOIN FISH_NAME_INFO AS N ON F.FISH_TYPE = N.FISH_TYPE
    GROUP BY N.FISH_NAME
    ORDER BY FISH_COUNT DESC;