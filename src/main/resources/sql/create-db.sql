DROP TABLE Users IF EXISTS;

CREATE TABLE Users (
  name        VARCHAR(30) PRIMARY KEY,
  password    VARCHAR(50)
);
