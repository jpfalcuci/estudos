CREATE DATABASE "todoapp" /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;


-- todoapp.projects definition

CREATE TABLE "projects" (
  "id" int NOT NULL AUTO_INCREMENT,
  "name" varchar(50) COLLATE utf8mb4_0900_bin NOT NULL,
  "description" varchar(255) COLLATE utf8mb4_0900_bin DEFAULT NULL,
  "createdAt" datetime NOT NULL,
  "updatedAt" datetime NOT NULL,
  PRIMARY KEY ("id")
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_bin;


-- todoapp.tasks definition

CREATE TABLE "tasks" (
  "id" int unsigned NOT NULL AUTO_INCREMENT,
  "idProject" int NOT NULL,
  "name" varchar(50) NOT NULL,
  "description" varchar(255) DEFAULT NULL,
  "completed" tinyint(1) NOT NULL,
  "notes" varchar(255) DEFAULT NULL,
  "deadline" date NOT NULL,
  "createdAt" datetime NOT NULL,
  "updatedAt" datetime NOT NULL,
  PRIMARY KEY ("id"),
  KEY "tasks_FK" ("idProject"),
  CONSTRAINT "tasks_FK" FOREIGN KEY ("idProject") REFERENCES "projects" ("id")
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
