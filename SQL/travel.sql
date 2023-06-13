CREATE TABLE user (
    id  INT                 PRIMARY KEY AUTO_INCREMENT,

    name    VARCHAR(36)     NOT NULL,
    pwd     VARCHAR(36)     NOT NULL,

    age         INT,
    email       VARCHAR(36),
    gender ENUM("female", "male", "unknown") NOT NULL DEFAULT "unknown"
);

source ./SQL/data/user.sql;

CREATE TABLE admin (
    id      INT             PRIMARY KEY AUTO_INCREMENT,
    name    VARCHAR(36)     NOT NULL,
    pwd     VARCHAR(36)     NOT NULL,
    email   VARCHAR(36)
);

source ./SQL/data/admin.sql;
