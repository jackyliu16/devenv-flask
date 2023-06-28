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
-- TODO: readd feedback
-- INSERT INTO feedback VALUES(1, 1, "18922251299@163.com", "what a good website");
