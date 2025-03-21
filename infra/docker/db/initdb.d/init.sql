-- .env, .env.example, .env.testing など、DB_DATABASEの値に合わせること
CREATE DATABASE IF NOT EXISTS python_be_syokyu;
CREATE DATABASE IF NOT EXISTS python_be_syokyu_test;
GRANT ALL ON python_be_syokyu.* TO 'dev'@'%';
GRANT ALL ON python_be_syokyu_test.* TO 'dev'@'%';