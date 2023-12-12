-- creates a table second_table in the database hbtn_0c_0
-- Add-props to the second_table
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);

-- creates maximum 4 rows
INSERT INTO 'second_table' ('id' ,'name', 'score') values (1, "John", 10);
INSERT INTO 'second_table' ('id', 'name', 'score') values (2, "Alex", 3);
INSERT INTO 'second_table' ('id', 'name', 'score') values (3, "Bob", 14);
INSERT INTO 'second_table' ('id', 'name', 'score') values (4, "George", 8);
