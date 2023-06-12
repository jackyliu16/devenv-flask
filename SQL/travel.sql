CREATE TABLE user_data (
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

INSERT INTO admin VALUES (1000, "jacky", "123456", NULL);
