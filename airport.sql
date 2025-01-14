CREATE DATABASE  IF NOT EXISTS `airport` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `airport`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: airport
-- ------------------------------------------------------
-- Server version	9.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `aviones`
--

DROP TABLE IF EXISTS `aviones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aviones` (
  `id_avion` int NOT NULL AUTO_INCREMENT,
  `modelo` varchar(30) DEFAULT NULL,
  `fecha_adquisicion` date DEFAULT NULL,
  `ultimo_chequeo` datetime DEFAULT NULL,
  `cantidad_asientos` int DEFAULT NULL,
  PRIMARY KEY (`id_avion`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aviones`
--

LOCK TABLES `aviones` WRITE;
/*!40000 ALTER TABLE `aviones` DISABLE KEYS */;
INSERT INTO `aviones` VALUES (1,'BOEING-737','2023-12-09','2024-12-31 00:00:00',162),(2,'AIRBUS-A320','2024-01-10','2024-12-29 00:00:00',146),(3,'BOEING-777','2024-01-12','2025-01-02 00:00:00',472),(4,'AIRBUS-A340','2024-02-07','2024-12-29 00:00:00',359);
/*!40000 ALTER TABLE `aviones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservaciones`
--

DROP TABLE IF EXISTS `reservaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservaciones` (
  `id_reservacion` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `nombre_persona` varchar(45) DEFAULT NULL,
  `id_avion` int DEFAULT NULL,
  `id_vuelo` int DEFAULT NULL,
  `asiento` varchar(4) DEFAULT NULL,
  `fecha_reservacion` date DEFAULT NULL,
  PRIMARY KEY (`id_reservacion`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservaciones`
--

LOCK TABLES `reservaciones` WRITE;
/*!40000 ALTER TABLE `reservaciones` DISABLE KEYS */;
INSERT INTO `reservaciones` VALUES (1,1,'Alberto',1,1,'7B','2024-12-30'),(2,2,'Erik',1,1,'8A','2024-12-30'),(3,3,'Javier',1,1,'7C','2024-12-31');
/*!40000 ALTER TABLE `reservaciones` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `actualizar_asientos` AFTER INSERT ON `reservaciones` FOR EACH ROW BEGIN 
	UPDATE vuelos
    SET asientos_disponibles = asientos_disponibles - 1
    WHERE id_vuelo = NEW.id_vuelo
      AND id_avion = NEW.id_avion;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) DEFAULT NULL,
  `edad` int DEFAULT NULL,
  `username` varchar(12) DEFAULT NULL,
  `contraseña` varchar(12) DEFAULT NULL,
  `ciudad` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Alberto',20,'AlbertoHH','lol','Los Mochis'),(2,'Erik',20,'Erikson','12345678','Los Mochis'),(3,'Javier',20,'Pabi','123456789','Los Mochis'),(4,'Ruben',20,'Rubo','Ruben1','Los Mochis'),(5,'Alejandro',21,'Alexan','987456123','Mazatlan');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vuelos`
--

DROP TABLE IF EXISTS `vuelos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vuelos` (
  `id_vuelo` int NOT NULL AUTO_INCREMENT,
  `id_avion` int DEFAULT NULL,
  `fecha_vuelo` date DEFAULT NULL,
  `hora_estimada` time DEFAULT NULL,
  `asientos_disponibles` int DEFAULT NULL,
  `ciudad_salida` varchar(45) DEFAULT NULL,
  `ciudad_llegada` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_vuelo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vuelos`
--

LOCK TABLES `vuelos` WRITE;
/*!40000 ALTER TABLE `vuelos` DISABLE KEYS */;
INSERT INTO `vuelos` VALUES (1,1,'2025-01-27','14:00:00',162,'LOS MOCHIS','CDMX');
/*!40000 ALTER TABLE `vuelos` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `asignar_asientos_disponibles` AFTER INSERT ON `vuelos` FOR EACH ROW BEGIN
    DECLARE capacidad_avion INT;

    -- Obtener la cantidad de asientos del avión desde la tabla aviones
    SELECT cantidad_asientos INTO capacidad_avion
    FROM aviones
    WHERE id_avion = NEW.id_avion;

    -- Actualizar la columna asientos_disponibles en la tabla vuelos
    UPDATE vuelos
    SET asientos_disponibles = capacidad_avion
    WHERE id_vuelo = NEW.id_vuelo
      AND id_avion = NEW.id_avion;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Dumping events for database 'airport'
--

--
-- Dumping routines for database 'airport'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-14 13:38:53
