use master;

IF EXISTS (SELECT 1 FROM sys.databases WHERE name = 'CustomerETL')
BEGIN
	DROP DATABASE CustomerETL
END

GO

CREATE DATABASE CustomerETL;
GO

USE CustomerETL;
GO

CREATE TABLE Customers (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    FullName NVARCHAR(100),
    Age INT NULL,
    RegistrationDate DATE NULL,
    Email NVARCHAR(255),
    UserId NVARCHAR(50)
);
