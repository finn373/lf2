-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server Version:               10.4.19-MariaDB - mariadb.org binary distribution
-- Server Betriebssystem:        Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Exportiere Datenbank Struktur für hardware_db
CREATE DATABASE IF NOT EXISTS `hardware_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `hardware_db`;

-- Exportiere Struktur von Tabelle hardware_db.cpu_tbl
CREATE TABLE IF NOT EXISTS `cpu_tbl` (
  `Cpu_ID` int(100) NOT NULL,
  `Cpu_Name` varchar(50) NOT NULL DEFAULT '',
  `Cpu_Speed` varchar(50) NOT NULL DEFAULT '',
  `Cpu_Sockel` varchar(50) NOT NULL DEFAULT '',
  `Cpu_Price` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`Cpu_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Exportiere Daten aus Tabelle hardware_db.cpu_tbl: ~4 rows (ungefähr)
/*!40000 ALTER TABLE `cpu_tbl` DISABLE KEYS */;
INSERT INTO `cpu_tbl` (`Cpu_ID`, `Cpu_Name`, `Cpu_Speed`, `Cpu_Sockel`, `Cpu_Price`) VALUES
	(1, 'i7 9700K', '3.60Ghz', '1151', '277,00€'),
	(2, 'i7 8700K', '3.70Ghz', '1151', '337,99€'),
	(3, 'Ryzen 5 1600', '3.20Ghz', 'AM4', '129,00€'),
	(4, 'Ryzen 5 3600', '3.60Ghz', 'AM4', '199,00€');
/*!40000 ALTER TABLE `cpu_tbl` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle hardware_db.gpu_tbl
CREATE TABLE IF NOT EXISTS `gpu_tbl` (
  `gpu_ID` int(100) NOT NULL,
  `gpu_Name` varchar(50) DEFAULT NULL,
  `gpu_Memory` varchar(50) DEFAULT NULL,
  `gpu_Price` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`gpu_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Exportiere Daten aus Tabelle hardware_db.gpu_tbl: ~4 rows (ungefähr)
/*!40000 ALTER TABLE `gpu_tbl` DISABLE KEYS */;
INSERT INTO `gpu_tbl` (`gpu_ID`, `gpu_Name`, `gpu_Memory`, `gpu_Price`) VALUES
	(1, 'Nvidia GeForce RTX 3090 Founders Edition', '24GB', '2.499,9€'),
	(2, 'MSI GeForce RTX 3060 Gaming X', '12GB', '899,00€'),
	(3, 'MSI GeForce GTX 1650 D6 Ventus XS OCV2', '4GB', '289,00€'),
	(4, 'ASUS Phoenix GeForce GTX 1050 Ti', '4GB', '198,99€');
/*!40000 ALTER TABLE `gpu_tbl` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle hardware_db.motherboard_tbl
CREATE TABLE IF NOT EXISTS `motherboard_tbl` (
  `motherboard_ID` int(11) NOT NULL,
  `Motherboard_Name` varchar(50) DEFAULT NULL,
  `Motherboard_Price` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`motherboard_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Exportiere Daten aus Tabelle hardware_db.motherboard_tbl: ~2 rows (ungefähr)
/*!40000 ALTER TABLE `motherboard_tbl` DISABLE KEYS */;
INSERT INTO `motherboard_tbl` (`motherboard_ID`, `Motherboard_Name`, `Motherboard_Price`) VALUES
	(1, 'MSI Z390-A PRO Intel Z390', '104,00€'),
	(2, 'MSI B550-A Pro AMD B550', '108,00€');
/*!40000 ALTER TABLE `motherboard_tbl` ENABLE KEYS */;

-- Exportiere Struktur von Tabelle hardware_db.ram_tbl
CREATE TABLE IF NOT EXISTS `ram_tbl` (
  `ram_ID` int(100) NOT NULL,
  `ram_Name` varchar(50) DEFAULT NULL,
  `ram_Memory` varchar(50) DEFAULT NULL,
  `ram_Price` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ram_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Exportiere Daten aus Tabelle hardware_db.ram_tbl: ~2 rows (ungefähr)
/*!40000 ALTER TABLE `ram_tbl` DISABLE KEYS */;
INSERT INTO `ram_tbl` (`ram_ID`, `ram_Name`, `ram_Memory`, `ram_Price`) VALUES
	(1, 'Patriot Viper 4', '8GB', '45,49€'),
	(2, 'Crucial Ballistix', '16GB', '81,80€'),
	(3, 'G.Skill Rip Jaws V', '32GB', '159,40€');
/*!40000 ALTER TABLE `ram_tbl` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
