/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50714
Source Host           : localhost:3306
Source Database       : analysis

Target Server Type    : MYSQL
Target Server Version : 50714
File Encoding         : 65001

Date: 2018-07-18 09:11:48
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for spider_autohome_brand
-- ----------------------------
DROP TABLE IF EXISTS `spider_autohome_brand`;
CREATE TABLE `spider_autohome_brand` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text,
  `title` text,
  `datetime` timestamp NULL DEFAULT NULL,
  `sort` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=146 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for spider_autohome_firms
-- ----------------------------
DROP TABLE IF EXISTS `spider_autohome_firms`;
CREATE TABLE `spider_autohome_firms` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bid` int(11) DEFAULT NULL,
  `name` text,
  `type` varchar(100) DEFAULT NULL,
  `title` text,
  `datetime` timestamp NULL DEFAULT NULL,
  `sort` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=202 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for spider_autohome_vehicles
-- ----------------------------
DROP TABLE IF EXISTS `spider_autohome_vehicles`;
CREATE TABLE `spider_autohome_vehicles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fid` int(11) DEFAULT NULL,
  `name` text,
  `title` text,
  `datetime` timestamp NULL DEFAULT NULL,
  `sort` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=718 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for spider_car_data
-- ----------------------------
DROP TABLE IF EXISTS `spider_car_data`;
CREATE TABLE `spider_car_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `price1` varchar(100) DEFAULT NULL,
  `price2` varchar(100) DEFAULT NULL,
  `price3` varchar(100) DEFAULT NULL,
  `describes` text,
  `content` text,
  `datetime` timestamp NULL DEFAULT NULL,
  `type` int(5) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for spider_lianjia_data
-- ----------------------------
DROP TABLE IF EXISTS `spider_lianjia_data`;
CREATE TABLE `spider_lianjia_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `datetime` timestamp NOT NULL,
  `price1` varchar(100) DEFAULT NULL,
  `price2` varchar(100) DEFAULT NULL,
  `describes` text,
  `city` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9001 DEFAULT CHARSET=utf8;
SET FOREIGN_KEY_CHECKS=1;
