-- 코드를 입력하세요
SELECT P.PRODUCT_CODE, SUM(O.SALES_AMOUNT) * P.PRICE AS SALES
    FROM PRODUCT AS P 
    RIGHT JOIN OFFLINE_SALE AS O ON P.PRODUCT_ID = O.PRODUCT_ID
    GROUP BY P.PRODUCT_CODE
    ORDER BY SALES DESC, P.PRODUCT_CODE;
    
    