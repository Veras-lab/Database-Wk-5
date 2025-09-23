USE salesDB;

-- Create an index named IdxPhone on the 'phone' column
CREATE INDEX IdxPhone ON customers (phone);
-- Drop the index IdxPhone from customers table
DROP INDEX IdxPhone ON customers;
USE salesDB;

DROP USER 'bob'@'localhost';

CREATE USER 'bob'@'localhost' IDENTIFIED BY 'P$55!23';
GRANT INSERT ON salesDB.* TO 'bob'@'localhost';
FLUSH PRIVILEGES;
ALTER USER 'bob'@'localhost' IDENTIFIED BY 'P$55!23';


