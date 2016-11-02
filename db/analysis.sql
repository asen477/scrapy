-- phpMyAdmin SQL Dump
-- version 4.5.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 2016-11-02 15:52:01
-- 服务器版本： 5.7.11
-- PHP Version: 5.6.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `analysis`
--
CREATE DATABASE IF NOT EXISTS `analysis` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `analysis`;

-- --------------------------------------------------------

--
-- 表的结构 `spider_autohome_brand`
--

DROP TABLE IF EXISTS `spider_autohome_brand`;
CREATE TABLE `spider_autohome_brand` (
  `id` int(11) NOT NULL,
  `name` text,
  `title` text,
  `datetime` timestamp NULL DEFAULT NULL,
  `sort` int(11) NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `spider_autohome_firms`
--

DROP TABLE IF EXISTS `spider_autohome_firms`;
CREATE TABLE `spider_autohome_firms` (
  `id` int(11) NOT NULL,
  `bid` int(11) DEFAULT NULL,
  `name` text,
  `type` varchar(100) DEFAULT NULL,
  `title` text,
  `datetime` timestamp NULL DEFAULT NULL,
  `sort` int(11) DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `spider_autohome_vehicles`
--

DROP TABLE IF EXISTS `spider_autohome_vehicles`;
CREATE TABLE `spider_autohome_vehicles` (
  `id` int(11) NOT NULL,
  `fid` int(11) DEFAULT NULL,
  `name` text,
  `title` text,
  `datetime` timestamp NULL DEFAULT NULL,
  `sort` int(11) DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `spider_car_data`
--

DROP TABLE IF EXISTS `spider_car_data`;
CREATE TABLE `spider_car_data` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `price1` varchar(100) DEFAULT NULL,
  `price2` varchar(100) DEFAULT NULL,
  `price3` varchar(100) DEFAULT NULL,
  `describes` text,
  `content` text,
  `datetime` timestamp NULL DEFAULT NULL,
  `type` int(5) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `spider_lianjia_data`
--

DROP TABLE IF EXISTS `spider_lianjia_data`;
CREATE TABLE `spider_lianjia_data` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `datetime` timestamp NOT NULL,
  `price1` varchar(100) DEFAULT NULL,
  `price2` varchar(100) DEFAULT NULL,
  `describes` text
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `spider_autohome_brand`
--
ALTER TABLE `spider_autohome_brand`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `spider_autohome_firms`
--
ALTER TABLE `spider_autohome_firms`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `spider_autohome_vehicles`
--
ALTER TABLE `spider_autohome_vehicles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `spider_car_data`
--
ALTER TABLE `spider_car_data`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `spider_lianjia_data`
--
ALTER TABLE `spider_lianjia_data`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `spider_autohome_brand`
--
ALTER TABLE `spider_autohome_brand`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `spider_autohome_firms`
--
ALTER TABLE `spider_autohome_firms`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `spider_autohome_vehicles`
--
ALTER TABLE `spider_autohome_vehicles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `spider_car_data`
--
ALTER TABLE `spider_car_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `spider_lianjia_data`
--
ALTER TABLE `spider_lianjia_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
