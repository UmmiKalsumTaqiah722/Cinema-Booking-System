-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 16, 2024 at 05:26 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cinema_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `membership`
--

CREATE TABLE `membership` (
  `IC_Number` varchar(30) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Email` varchar(20) NOT NULL,
  `State` varchar(20) NOT NULL,
  `Age` int(20) NOT NULL,
  `Category` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `membership`
--

INSERT INTO `membership` (`IC_Number`, `Name`, `Email`, `State`, `Age`, `Category`) VALUES
('050306100045', 'Aiman', 'man@306', 'Johor', 19, 'Adult');

-- --------------------------------------------------------

--
-- Table structure for table `movie`
--

CREATE TABLE `movie` (
  `Movie_Name` varchar(30) NOT NULL,
  `Duration` varchar(30) NOT NULL,
  `Genre` varchar(30) NOT NULL,
  `Classification` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `movie`
--

INSERT INTO `movie` (`Movie_Name`, `Duration`, `Genre`, `Classification`) VALUES
('', '', '', ''),
('', '', '', ''),
('The Marvels', '105 minutes', 'Action/Fantasy', 'PG13');

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

CREATE TABLE `ticket` (
  `IC_Number` varchar(30) NOT NULL,
  `Selected_Movie` varchar(30) NOT NULL,
  `Date` varchar(30) NOT NULL,
  `Seat_Number` varchar(30) NOT NULL,
  `Pax` int(30) NOT NULL,
  `Price` int(30) NOT NULL,
  `Booking_ID` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ticket`
--

INSERT INTO `ticket` (`IC_Number`, `Selected_Movie`, `Date`, `Seat_Number`, `Pax`, `Price`, `Booking_ID`) VALUES
('050306100045\n', 'The Marvels', '24/01/25', 'Seat 4', 2, 34, '754');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
