CREATE DATABASE `TodoApp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `TodoApp`;


-- TodoApp.projects definition

CREATE TABLE `projects` (
	`id`			INT NOT NULL AUTO_INCREMENT,
	`name`			VARCHAR(50) NOT NULL,
	`description`	VARCHAR(255) DEFAULT NULL,
	`createdAt`		DATETIME NOT NULL,
	`updatedAt`		DATETIME NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- TodoApp.tasks definition

CREATE TABLE `tasks` (
	`id`			INT NOT NULL AUTO_INCREMENT,
	`idProject`		INT NOT NULL,
	`name`			VARCHAR(50) NOT NULL,
	`description`	VARCHAR(255) DEFAULT NULL,
	`completed`		TINYINT(1) NOT NULL,
	`notes`			VARCHAR(255) DEFAULT NULL,
	`deadline`		DATE DEFAULT NULL,
	`createdAt`		DATETIME NOT NULL,
	`updatedAt`		DATETIME NOT NULL,
	PRIMARY KEY (`id`),
	KEY `tasks_FK` (`idProject`),
	CONSTRAINT `tasks_FK` FOREIGN KEY (`idProject`) REFERENCES `projects` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
