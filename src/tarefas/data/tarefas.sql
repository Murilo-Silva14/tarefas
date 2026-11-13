CREATE DATABASE IF NOT EXISTS `tarefa`;

USE tarefa;

CREATE TABLE tarefas (
    id_tarefa BIGINT AUTO_INCREMENT PRIMARY KEY,
    titulo_tarefa VARCHAR(100) NOT NULL,
    data_conclusao DATETIME NULL
);