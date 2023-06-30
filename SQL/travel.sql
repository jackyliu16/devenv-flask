-- NOTE: maybe we could using [this](https://github.com/jackyliu16/small-toys/tree/main/Convert_xlsx_Into_SQL_Insert_Query) to convert xlsx into sql
-- (but some part of it should be refactor)
CREATE TABLE user (
    id          INT             PRIMARY KEY AUTO_INCREMENT,
    firstname   VARCHAR(36),
    lastname    VARCHAR(36)     NOT NULL,
    name        VARCHAR(36)     NOT NULL,
    pwd         CHAR(88)        NOT NULL,

    age         INT,
    email       VARCHAR(36)     NOT NULL UNIQUE,
    -- gender ENUM("female", "male", "unknown") NOT NULL DEFAULT "unknown"
    gender      INT             DEFAULT NULL,
    auth        TINYINT 	    NOT NULL DEFAULT 0
    -- 0 customer, 1 admin
);

source ./SQL/data/user.sql;

CREATE TABLE feedback (
    id        INT PRIMARY KEY AUTO_INCREMENT,
    user_id      INT DEFAULT 0,    -- for others ref to a user
    email    VARCHAR(36)  NOT NULL,
    comment  VARCHAR(500) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

INSERT INTO feedback VALUES(1, 1, "18922251299@163.com", "what a good website");

CREATE TABLE product_detail (
    id       INT PRIMARY KEY AUTO_INCREMENT,
    name      VARCHAR(36)    NOT NULL,
    intro     TEXT,
    content   LONGTEXT       NOT NULL,
    price     VARCHAR(36)    NOT NULL,
    mask      SMALLINT       NOT NULL
);
source ./SQL/data/product_detail.sql;

CREATE TABLE bill {
    id      INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    fname   VARCHAR(36),
    lname   VARCHAR(36),
    cname   VARCHAR(36),
    zipcode VARCHAR(8),
    email   VARCHAR(36),
    phone   VARCHAR(15),
    city    VARCHAR(36),
    address VARCHAR(36),
    product_id INT,
    pay_method VARCHAR(8),
    unit    TINYINT, 
    price   INT,
    start_time VARCHAR(16),
    end_time VARCHAR(16),

    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (product_id) REFERENCES product_detail(id),
}

-- NOTE: what about we just search it in the path with specify name 
-- CREATE TABLE images (
--   id INT(11) NOT NULL AUTO_INCREMENT,
--   name  VARCHAR(255) DEFAULT NULL,
--   product_id  INT NOT NULL,
--   url   VARCHAR(255) DEFAULT NULL,
--   PRIMARY KEY (id)
--   FOREIGN KEY (product_id) REFERENCES product_detail(id)
-- );
-- TODO: readd feedback
-- INSERT INTO feedback VALUES(1, 1, "18922251299@163.com", "what a good website");

