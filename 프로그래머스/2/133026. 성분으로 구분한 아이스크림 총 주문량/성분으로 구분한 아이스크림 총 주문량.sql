-- 코드를 입력하세요
SELECT I.INGREDIENT_TYPE, SUM(FH.TOTAL_ORDER) AS TOTAL_ORDER
    FROM FIRST_HALF AS FH
    INNER JOIN ICECREAM_INFO AS I ON FH.FLAVOR = I.FLAVOR
    GROUP BY INGREDIENT_TYPE
    ORDER BY TOTAL_ORDER;