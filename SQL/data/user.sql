-- CREATE TABLE user (
--     id          INT             PRIMARY KEY AUTO_INCREMENT,
--     firstname   VARCHAR(36),
--     lastname    VARCHAR(36)     NOT NULL,
--     name        VARCHAR(36)     NOT NULL,
--     pwd         CHAR(88)        NOT NULL,

--     age         INT,
--     email       VARCHAR(36)     NOT NULL UNIQUE,
--     -- gender ENUM("female", "male", "unknown") NOT NULL DEFAULT "unknown"
--     gender      INT             DEFAULT NULL,
--     auth        TINYINT 	    NOT NULL DEFAULT 0
--     -- 0 user, 1 admin
-- );
-- ADMIN
INSERT INTO user (auth, lastname, name, email, pwd) VALUES (1, "jacky", "jacky", "18922251299@163.com", "sha256$AH62hcfABzGv07dX$cc410d510852a5f49bd6bb544c7b0305e1c371c9dc4a494fa5912c089be9137a");
-- CUSTOM auth default 0
INSERT INTO user (auth, lastname, name, email, pwd) VALUES (0, "Anonymous", "Anonymous", "Anonymous@163.com", "sha256$AH62hcfABzGv07dX$cc410d510852a5f49bd6bb544c7b0305e1c371c9dc4a494fa5912c089be9137a");

INSERT INTO user (auth, firstname, lastname, name, email, pwd) VALUES (0, "", "jacky", "jacky1", "1891@163.com", "sha256$AH62hcfABzGv07dX$cc410d510852a5f49bd6bb544c7b0305e1c371c9dc4a494fa5912c089be9137a");
INSERT INTO user (auth, firstname, lastname, name, email, pwd) VALUES (0, "", "jacky", "jacky2", "1892@163.com", "sha256$AH62hcfABzGv07dX$cc410d510852a5f49bd6bb544c7b0305e1c371c9dc4a494fa5912c089be9137a");
INSERT INTO user (auth, firstname, lastname, name, email, pwd) VALUES (0, "", "jacky", "jacky3", "1893@163.com", "sha256$AH62hcfABzGv07dX$cc410d510852a5f49bd6bb544c7b0305e1c371c9dc4a494fa5912c089be9137a");
INSERT INTO user (auth, firstname, lastname, name, email, pwd) VALUES (0, "", "jacky", "jacky4", "1894@163.com", "sha256$AH62hcfABzGv07dX$cc410d510852a5f49bd6bb544c7b0305e1c371c9dc4a494fa5912c089be9137a");
INSERT INTO user (auth, firstname, lastname, name, email, pwd) VALUES (0, "", "jacky", "jacky5", "1895@163.com", "sha256$AH62hcfABzGv07dX$cc410d510852a5f49bd6bb544c7b0305e1c371c9dc4a494fa5912c089be9137a");
INSERT INTO user (auth, firstname, lastname, name, email, pwd) VALUES (0, "", "jacky", "jacky6", "1896@163.com", "sha256$AH62hcfABzGv07dX$cc410d510852a5f49bd6bb544c7b0305e1c371c9dc4a494fa5912c089be9137a");
