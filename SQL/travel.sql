CREATE TABLE user (
    id          INT             PRIMARY KEY AUTO_INCREMENT,
    firstname   VARCHAR(36),
    lastname    VARCHAR(36)     NOT NULL,
    name        VARCHAR(36)     NOT NULL,
    pwd         CHAR(88)        NOT NULL,

    age         INT,
    email       VARCHAR(36)     NOT NULL,
    -- gender ENUM("female", "male", "unknown") NOT NULL DEFAULT "unknown"
    gender      INT             DEFAULT 2
    CONSTRAINT email UNIQUE (email)
);

source ./SQL/data/user.sql;

CREATE TABLE admin (
    id      INT             PRIMARY KEY AUTO_INCREMENT,
    name    VARCHAR(36)     NOT NULL,
    pwd     CHAR(88)        NOT NULL,
    email   VARCHAR(36)
);

source ./SQL/data/admin.sql;
