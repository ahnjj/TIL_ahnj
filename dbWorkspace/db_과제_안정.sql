-- 과제 
-- 안정

-- 1 . 1. department와 employees 테이블을 생성
CREATE TABLE department(
	dpt_no VARCHAR(10) NOT NULL PRIMARY KEY,
    dpt_name VARCHAR(20) NOT NULL,
    dpt_phone VARCHAR(13) NOT NULL
);

CREATE TABLE employees(
	emp_no VARCHAR(10) NOT NULL PRIMARY KEY,
    emp_name VARCHAR(20) NOT NULL,
    emp_phone VARCHAR(13) NOT NULL,
    emp_address VARCHAR(100),
    emp_email VARCHAR(50),
    dpt_no VARCHAR(10) NOT NULL,
    FOREIGN KEY (dpt_no) REFERENCES department(dpt_no)
);

-- 2. 각 테이블에 데이터 3개씩 저장
INSERT INTO department VALUES ('1', '영업부', '02-1111-2222');
INSERT INTO department VALUES ('2', '인사부', '02-2222-3333');
INSERT INTO department VALUES ('3', '총무부', '02-3333-4444');

INSERT INTO employees VALUES ('1001', '홍길동', '010-1111-1111', '서울시 강남구', 'hong@naver.com', '1');
INSERT INTO employees VALUES ('1002', '이몽룡', '010-2222-2222', '부산광역시 해운대구', 'lee@daum.net', '2');
INSERT INTO employees VALUES ('1003', '성춘향', '010-3333-3333', '서울시 종로구', 'sch@gmail.com', '1');

-- 3. employees 테이블의 전체 내용 조회
SELECT * FROM employees;

-- 4. employees 테이블에서 ‘영업부’ 직원만 검색'
SELECT *
FROM employees AS e
	 LEFT JOIN department AS d ON e.dpt_no = d.dpt_no
WHERE dpt_name LIKE '영업부';


-- 5. employees 테이블의 전체 데이터 삭제
DELETE FROM employees;


