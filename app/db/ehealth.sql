-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: db:3306
-- Generation Time: Oct 18, 2022 at 06:11 PM
-- Server version: 8.0.31
-- PHP Version: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ehealth`
--
CREATE DATABASE IF NOT EXISTS `ehealth` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `ehealth`;

DROP TABLE IF EXISTS `appointment`;
DROP TABLE IF EXISTS `doctor`;
DROP TABLE IF EXISTS `user`;
DROP TABLE IF EXISTS `specialization`;

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `id` int NOT NULL,
  `doctorId` int NOT NULL,
  `patientId` int NOT NULL,
  `date` datetime NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`id`, `doctorId`, `patientId`, `date`, `description`) VALUES
(1, 1, 2, '2022-08-29 17:08:39', 'Release Right Breast, Percutaneous Approach'),
(2, 3, 4, '2022-11-16 17:34:23', 'Excision of Cerebellum, Percutaneous Endoscopic Approach, Diagnostic'),
(3, 3, 6, '2022-07-21 12:48:50', 'Removal of External Fixation Device from Right Carpal, Percutaneous Endoscopic Approach'),
(4, 7, 8, '2022-01-19 13:58:17', 'Extirpation of Matter from Large Intestine, Via Natural or Artificial Opening Endoscopic'),
(5, 5, 10, '2022-11-10 17:04:36', 'Excision of Left Greater Saphenous Vein, Percutaneous Approach, Diagnostic');

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `id` int NOT NULL,
  `specialization` int NOT NULL,
  `salary` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`id`, `specialization`, `salary`) VALUES
(1, 6, 2644),
(3, 2, 2456),
(5, 16, 2714),
(7, 19, 4876),
(9, 18, 1759);

-- --------------------------------------------------------

--
-- Table structure for table `specialization`
--

CREATE TABLE `specialization` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `specialization`
--

INSERT INTO `specialization` (`id`, `name`) VALUES
(1, 'Allergy and immunology'),
(2, 'Anesthesiology'),
(3, 'Dermatology'),
(4, 'Diagnostic radiology'),
(5, 'Emergency medicine'),
(6, 'Family medicine'),
(7, 'Internal medicine'),
(8, 'Medical genetics'),
(9, 'Neurology'),
(10, 'Nuclear medicine'),
(11, 'Obstetrics and gynecology'),
(12, 'Ophthalmology'),
(13, 'Pathology'),
(14, 'Pediatrics'),
(15, 'Physical medicine and rehabilitation'),
(16, 'Preventive medicine'),
(17, 'Psychiatry'),
(18, 'Radiation oncology'),
(19, 'Surgery'),
(20, 'Urology');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int NOT NULL,
  `name` varchar(80) NOT NULL,
  `password` varchar(256) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `password`, `email`) VALUES
(1, 'Jacquelin Labbe', 'gCxS9aPx3', 'jlabbe0@unesco.org'),
(2, 'Wilma Padkin', 'c4dJWraw', 'wpadkin1@paginegialle.it'),
(3, 'Jannel Rustich', '8MYaB2', 'jrustich2@seesaa.net'),
(4, 'Liza Panner', 'wRqWygeoBY', 'lpanner3@va.gov'),
(5, 'Cody Ca', 'gdiLDeeAj', 'cca4@t.co'),
(6, 'Nedi Juppe', 'tF1n9Mt', 'njuppe5@jimdo.com'),
(7, 'Lyndell Arlett', 'S1QjsUD8', 'larlett6@mashable.com'),
(8, 'Monah Hacquard', 'VuYgp2AK', 'mhacquard7@tinypic.com'),
(9, 'Brandise Stranieri', 'DjHY6vh79FAM', 'bstranieri8@illinois.edu'),
(10, 'Lodovico Haysham', 'xZsxPWg3B', 'lhaysham9@gnu.org');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `appointment_pat_user_fk` (`patientId`),
  ADD KEY `appointment_doc_user_fk` (`doctorId`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`id`),
  ADD KEY `doctor_specialization_null_fk` (`specialization`);

--
-- Indexes for table `specialization`
--
ALTER TABLE `specialization`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointment`
--
ALTER TABLE `appointment`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `specialization`
--
ALTER TABLE `specialization`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `appointment`
--
ALTER TABLE `appointment`
  ADD CONSTRAINT `appointment_doc_user_fk` FOREIGN KEY (`doctorId`) REFERENCES `doctor` (`id`),
  ADD CONSTRAINT `appointment_pat_user_fk` FOREIGN KEY (`patientId`) REFERENCES `user` (`id`);

--
-- Constraints for table `doctor`
--
ALTER TABLE `doctor`
  ADD CONSTRAINT `doctor_specialization_null_fk` FOREIGN KEY (`specialization`) REFERENCES `specialization` (`id`),
  ADD CONSTRAINT `doctor_user_null_fk` FOREIGN KEY (`id`) REFERENCES `user` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
