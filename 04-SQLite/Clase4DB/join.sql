-- CREATE TABLE Departamentos (
--     DepartamentoID INTEGER PRIMARY KEY,
--     NombreDepartamento TEXT NOT NULL
-- );

-- CREATE TABLE Empleados (
--     EmpleadoID INTEGER PRIMARY KEY,
--     Nombre TEXT NOT NULL,
--     DepartamentoID INTEGER,
--     FOREIGN KEY (DepartamentoID) REFERENCES Departamentos(DepartamentoID)
-- );

-- -- Inseertar un departamento
-- INSERT INTO Departamentos (NombreDepartamento) VALUES ("Recursos Humanos");
-- -- Insertar un empleado en el departamento creado
-- INSERT INTO Empleados (Nombre, DepartamentoID) VALUES ("Juan Perez", 1);

---- Actuualizar un valor en la tabla
--UPDATE Empleados SET DepartamentoID = 2 WHERE EmpleadoID = 1;


-- -- Para vincular después de crear la tabla y no lo metiste
-- SELECT Empleados.Nombre, Departamentos.NombreDepartamento
-- FROM Empleados
-- INNER JOIN Departamentos ON Empleados.DepartamentoID = Departamentos.DepartamentoID