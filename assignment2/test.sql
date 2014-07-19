-- Problem 1: Inspecting the Reuters Dataset; Basic Relational Algebra

-- reuters.db has just one table:
-- frequency(docid, term, count)

-- a)
-- SELECT COUNT(*)
-- FROM frequency
-- WHERE docid = "10398_txt_earn";
-- sqlite3 reuters.db < test.sql > select.txt

-- b)
-- SELECT COUNT(term)
-- FROM frequency
-- WHERE docid = "10398_txt_earn"
-- 	AND count = 1;
-- sqlite3 reuters.db < test.sql > select_project.txt

-- c)
-- SELECT COUNT(*)
-- FROM (
-- 	SELECT term
-- 	FROM frequency
-- 	WHERE docid = "10398_txt_earn"
-- 		AND count = 1
-- 	UNION
-- 	SELECT term
-- 	FROM frequency
-- 	WHERE docid = "925_txt_trade"
-- 		AND count = 1
-- ) x;
-- sqlite3 reuters.db < test.sql > union.txt

-- d)
-- SELECT COUNT(docid)
-- FROM frequency
-- WHERE term = "parliament";
-- sqlite3 reuters.db < test.sql > count.txt

-- e)
-- SELECT COUNT(*)
-- FROM (
-- 	SELECT docid
-- 	FROM frequency
-- 	GROUP BY docid
-- 	HAVING SUM(count) > 300
-- ) x;
-- sqlite3 reuters.db < test.sql > big_documents.txt

-- f)
-- SELECT COUNT(DISTINCT x.docid)
-- FROM frequency x, frequency y
-- WHERE x.docid = y.docid
-- 	AND x.term = "transactions"
-- 	AND y.term = "world";
-- sqlite3 reuters.db < test.sql > two_words.txt


-- Problem 2: Matrix Multiplication in SQL

-- g)

-- matrix.db has two tables:
-- A(row_num, col_num, value)
-- B(row_num, col_num, value)

-- SELECT * FROM A;
-- SELECT * FROM B;

-- SELECT C.value
-- FROM (
-- 	SELECT A.row_num,
-- 		B.col_num,
-- 		SUM(A.value * B.value) as value
-- 	FROM A, B
-- 	WHERE A.col_num = B.row_num
-- 	GROUP BY A.row_num, b.col_num
-- ) AS C
-- WHERE C.row_num = 2
-- 	AND C.col_num = 3;
-- sqlite3 matrix.db < test.sql > multiply.txt

-- The GROUP BY means we're going to get one row for every combination of row in A an column in B
-- Then we join appropriately -> every cell in col 1 table A is joined with every cell in row 1 table B; same with col 2 A/row 2 B, etc.
-- Finally, we just want the value of cell (2,3)
-- Then we sum the products


-- Problem 3: Working with a Term-Document Matrix

-- h)

-- SELECT SUM(x.count * y.count)
-- FROM frequency x, frequency y
-- WHERE x.term = y.term
-- 	AND x.docid = '10080_txt_crude'
-- 	AND y.docid = '17035_txt_earn'
-- GROUP BY x.docid, y.docid;
-- sqlite3 reuters.db < test.sql > similarity_matrix.txt

-- i)

-- CREATE VIEW frequency_view AS
-- SELECT * FROM frequency
-- UNION
-- SELECT 'q' as docid, 'washington' as term, 1 as count
-- UNION
-- SELECT 'q' as docid, 'taxes' as term, 1 as count
-- UNION
-- SELECT 'q' as docid, 'treasury' as term, 1 as count;

SELECT MAX(z.similarity)
FROM (
	SELECT x.docid,
		y.docid,
		SUM(x.count * y.count) as similarity
	FROM frequency_view x, frequency_view y
	WHERE x.term = y.term
		AND x.docid = 'q'
	GROUP BY x.docid, y.docid
) z;
-- sqlite3 reuters.db < test.sql > keyword_search.txt