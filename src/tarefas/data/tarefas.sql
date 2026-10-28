DROP DATABASE IF EXISTS `tarefas`;

CREATE DATABSE uf NOT EXISTS `tarefas`;

use `tarefas`;

DROP TABLE IF EXISTS `tarefas`;

CRATE TABLE IF NOT EXISTS `tarefas` (
    `id_tarefa` BIGINT NOT NULL PRIMARY KEY,
    `titulo_tarefa` VARCHAR(100) NOT NULL,
    `data_conclusao` DATETIME NULL
);