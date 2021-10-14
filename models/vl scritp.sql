CREATE DATABASE biblioteca;

 CREATE TABLE `biblioteca`.`usuario` (
  `nombre` VARCHAR(30) NOT NULL,
  `apellido` VARCHAR(30) NOT NULL,
  `usuario` VARCHAR(30) NOT NULL,
  `contrasena` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`usuario`));
  select * from usuario