CREATE TABLE user (
    id          INT             PRIMARY KEY AUTO_INCREMENT,

    name        VARCHAR(36)     NOT NULL,
    pwd         CHAR(88)        NOT NULL,

    age         INT,
    email       VARCHAR(36),
    -- gender ENUM("female", "male", "unknown") NOT NULL DEFAULT "unknown"
    gender      INT             DEFAULT 2
    -- authority   BOOLEAN         
);

source ./SQL/data/user.sql;

CREATE TABLE admin (
    id      INT             PRIMARY KEY AUTO_INCREMENT,
    name    VARCHAR(36)     NOT NULL,
    pwd     CHAR(88)        NOT NULL,
    email   VARCHAR(36)
);

source ./SQL/data/admin.sql;
