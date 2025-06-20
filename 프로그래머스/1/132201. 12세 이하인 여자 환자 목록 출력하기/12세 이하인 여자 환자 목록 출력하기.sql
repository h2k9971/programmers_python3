-- 코드를 입력하세요
SELECT PT_NAME, PT_NO, GEND_CD, AGE, 
    CASE
        WHEN TLNO is null then 'NONE'
        ELSE TLNO
    END AS TLNO
    FROM PATIENT
    WHERE AGE <= 12 and GEND_CD = 'W'
    ORDER BY AGE DESC, PT_NAME;