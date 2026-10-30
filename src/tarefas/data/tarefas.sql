CREATE DATABASE if NOT EXISTS `tarefas`;

use `tarefas`;


CREATE TABLE IF NOT EXISTS `tarefas` (
    `id_tarefa` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `titulo_tarefa` VARCHAR(100) NOT NULL,
    `data_conclusao` DATETIME NULL
);