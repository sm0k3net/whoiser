-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb2+deb7u6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 14, 2017 at 08:07 AM
-- Server version: 5.5.53
-- PHP Version: 5.4.45-0+deb7u6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
--

-- --------------------------------------------------------

--
-- Table structure for table `whoiser`
--

CREATE TABLE IF NOT EXISTS `whoiser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(256) NOT NULL,
  `creDate` varchar(24) NOT NULL,
  `expDate` varchar(24) NOT NULL,
  `updDate` varchar(24) NOT NULL,
  `registrar` text NOT NULL,
  `domain_status` text NOT NULL,
  `name` text NOT NULL,
  `country` varchar(3) NOT NULL,
  `phone` varchar(32) NOT NULL,
  `email` text NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
