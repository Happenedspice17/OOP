--CREATE TABLE users (username TEXT NOT NULL PRIMARY KEY, password NOT NULL, email NOT NULL);

--Una vez que creas la tabla, debes comentar el CREATE

-- El sql es el que crea la base de datos, los queries pues, los comandos
INSERT INTO users (username, password, email)
VALUES ("Charles", "mypassword", "charles@gamil.com");