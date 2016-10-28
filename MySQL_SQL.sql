-- MySQL dump 10.13  Distrib 5.7.12, for Win32 (AMD64)
--
-- Host: 211.253.29.113    Database: sogangdb
-- ------------------------------------------------------
-- Server version	5.5.52-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_52fdd58701c5f563_fk_first_suser_sUserID` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_first_suser_sUserID` FOREIGN KEY (`user_id`) REFERENCES `first_suser` (`sUserID`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `first_clist`
--

DROP TABLE IF EXISTS `first_clist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `first_clist` (
  `CID` int(11) NOT NULL,
  `Category` varchar(255) DEFAULT NULL,
  `ProgramNuame` varchar(255) DEFAULT NULL,
  `EpisodeNum` int(11) NOT NULL,
  `VideoURL` varchar(255) DEFAULT NULL,
  `VideoFileName` varchar(255) DEFAULT NULL,
  `VideoThumb` varchar(255) DEFAULT NULL,
  `FPS` double NOT NULL,
  `RegisterDateTime` datetime NOT NULL,
  `LastSavedDateTime` datetime NOT NULL,
  `TagStatus` int(11) NOT NULL,
  `User` varchar(255) DEFAULT NULL,
  `ProgramNameKor` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`CID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `first_filtering`
--

DROP TABLE IF EXISTS `first_filtering`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `first_filtering` (
  `sUserID_id` varchar(50) NOT NULL,
  `serviceProvider` varchar(128) NOT NULL,
  `degree` varchar(64) NOT NULL,
  `price` varchar(64) NOT NULL,
  PRIMARY KEY (`sUserID_id`),
  CONSTRAINT `first_filteri_sUserID_id_510469195128371e_fk_first_suser_sUserID` FOREIGN KEY (`sUserID_id`) REFERENCES `first_suser` (`sUserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `first_group`
--

DROP TABLE IF EXISTS `first_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `first_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` varchar(20) DEFAULT NULL,
  `group` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `first_shotinfo`
--

DROP TABLE IF EXISTS `first_shotinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `first_shotinfo` (
  `ShotID` int(11) NOT NULL,
  `ShotNum` int(11) NOT NULL,
  `StartFrame` int(11) NOT NULL,
  `EndFrame` int(11) NOT NULL,
  `ThumbURL` varchar(255) DEFAULT NULL,
  `CID_id` int(11) NOT NULL,
  PRIMARY KEY (`ShotID`),
  KEY `first_shotinfo_CID_id_7f2e1041ac4015be_fk_first_clist_CID` (`CID_id`),
  CONSTRAINT `first_shotinfo_CID_id_7f2e1041ac4015be_fk_first_clist_CID` FOREIGN KEY (`CID_id`) REFERENCES `first_clist` (`CID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `first_survey`
--

DROP TABLE IF EXISTS `first_survey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `first_survey` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cID` int(11) NOT NULL,
  `shotID` int(11) NOT NULL,
  `time` datetime NOT NULL,
  `fileName` varchar(256) NOT NULL,
  `preference` double NOT NULL,
  `reason` varchar(256) NOT NULL,
  `sUserID_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `first_survey_sUserID_id_555c214de32d57ab_uniq` (`sUserID_id`,`shotID`),
  KEY `first_survey_036b5b1d` (`sUserID_id`),
  CONSTRAINT `first_survey_sUserID_id_49dc5f27668ec867_fk_first_suser_sUserID` FOREIGN KEY (`sUserID_id`) REFERENCES `first_suser` (`sUserID`)
) ENGINE=InnoDB AUTO_INCREMENT=181592 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `first_suser`
--

DROP TABLE IF EXISTS `first_suser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `first_suser` (
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `sUserID` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `group` varchar(5) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `sex` varchar(5) DEFAULT NULL,
  `married` varchar(5) DEFAULT NULL,
  `children` varchar(5) DEFAULT NULL,
  `job` varchar(128) DEFAULT NULL,
  `company` varchar(128) DEFAULT NULL,
  `hobby` varchar(128) DEFAULT NULL,
  `currentShot` int(11) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `phone` varchar(20),
  PRIMARY KEY (`sUserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `first_suser_groups`
--

DROP TABLE IF EXISTS `first_suser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `first_suser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `suser_id` varchar(50) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `suser_id` (`suser_id`,`group_id`),
  KEY `first_suser_groups_group_id_606b543f0144fc78_fk_auth_group_id` (`group_id`),
  CONSTRAINT `first_suser_groups_group_id_606b543f0144fc78_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `first_suser_gro_suser_id_39a9520fc789df15_fk_first_suser_sUserID` FOREIGN KEY (`suser_id`) REFERENCES `first_suser` (`sUserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `first_suser_user_permissions`
--

DROP TABLE IF EXISTS `first_suser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `first_suser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `suser_id` varchar(50) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `suser_id` (`suser_id`,`permission_id`),
  KEY `first_suser_permission_id_5aec3aa9b2a38b6b_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `first_suser_permission_id_5aec3aa9b2a38b6b_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `first_suser_use_suser_id_5adb5883d4c5addb_fk_first_suser_sUserID` FOREIGN KEY (`suser_id`) REFERENCES `first_suser` (`sUserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `star_ratings_rating`
--

DROP TABLE IF EXISTS `star_ratings_rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `star_ratings_rating` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `count` int(10) unsigned NOT NULL,
  `total` int(10) unsigned NOT NULL,
  `average` decimal(6,3) NOT NULL,
  `object_id` int(10) unsigned DEFAULT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `star_ratings_rating_content_type_id_1fea23398f983929_uniq` (`content_type_id`,`object_id`),
  CONSTRAINT `star__content_type_id_34387b1f1996111a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `star_ratings_userrating`
--

DROP TABLE IF EXISTS `star_ratings_userrating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `star_ratings_userrating` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  `ip` char(39) DEFAULT NULL,
  `score` smallint(5) unsigned NOT NULL,
  `rating_id` int(11) NOT NULL,
  `user_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `star_ratings_userrating_user_id_5a83a88db79dd2cf_uniq` (`user_id`,`rating_id`),
  KEY `star_rating_rating_id_1603aaaa4f6f2354_fk_star_ratings_rating_id` (`rating_id`),
  CONSTRAINT `star_ratings_use_user_id_709e3d8dec7a0fe8_fk_first_suser_sUserID` FOREIGN KEY (`user_id`) REFERENCES `first_suser` (`sUserID`),
  CONSTRAINT `star_rating_rating_id_1603aaaa4f6f2354_fk_star_ratings_rating_id` FOREIGN KEY (`rating_id`) REFERENCES `star_ratings_rating` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping events for database 'sogangdb'
--

--
-- Dumping routines for database 'sogangdb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-10-28 14:19:29
