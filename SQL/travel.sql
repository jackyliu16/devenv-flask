CREATE TABLE customer (
    id          INT             PRIMARY KEY AUTO_INCREMENT,
    firstname   VARCHAR(36),
    lastname    VARCHAR(36)     NOT NULL,
    name        VARCHAR(36)     NOT NULL,
    pwd         CHAR(88)        NOT NULL,

    age         INT,
    email       VARCHAR(36)     NOT NULL UNIQUE,
    -- gender ENUM("female", "male", "unknown") NOT NULL DEFAULT "unknown"
    gender      INT             DEFAULT NULL
);

source ./SQL/data/user.sql;

CREATE TABLE admin (
    id      INT             PRIMARY KEY AUTO_INCREMENT,
    name    VARCHAR(36)     NOT NULL,
    pwd     CHAR(88)        NOT NULL,
    email   VARCHAR(36)     NOT NULL
);

source ./SQL/data/admin.sql;

-- TODO maybe we could using this, but it's a kind of shit
-- https://github.com/jackyliu16/small-toys/blob/main/Convert_xlsx_Into_SQL_Insert_Query/generate_sql_from_csv.py
-- source ./SQL/data/insertData.sql;
