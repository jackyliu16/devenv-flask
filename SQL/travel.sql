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
INSERT INTO admin VALUES (1, "jacky", "sha256$AH62hcfABzGv07dX$cc410d510852a5f49bd6bb544c7b0305e1c371c9dc4a494fa5912c089be9137a", "18922251299@163.com");

-- TODO maybe we could using this, but it's a kind of shit
-- https://github.com/jackyliu16/small-toys/blob/main/Convert_xlsx_Into_SQL_Insert_Query/generate_sql_from_csv.py
-- source ./SQL/data/insertData.sql;

CREATE TABLE feedback (
    id        INT PRIMARY KEY AUTO_INCREMENT,
    user_id      INT DEFAULT 0,    -- for others ref to a user
    email    VARCHAR(36)  NOT NULL,
    comment  VARCHAR(500) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES customer(id)
);
INSERT INTO feedback VALUES(1, 1, "18922251299@163.com", "what a good website");
