-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: member
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.22.04.1

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
-- Table structure for table `session_details`
--

DROP TABLE IF EXISTS `session_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `session_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `login_time` datetime NOT NULL,
  `logout_time` varchar(45) NOT NULL,
  `user` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session_details`
--

LOCK TABLES `session_details` WRITE;
/*!40000 ALTER TABLE `session_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `session_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `surveyor_details`
--

DROP TABLE IF EXISTS `surveyor_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `surveyor_details` (
  `sid` varchar(20) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `phone_no` varchar(20) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `aadhar_no` varchar(16) NOT NULL,
  `pan` varchar(10) NOT NULL,
  `voter_id` varchar(20) NOT NULL,
  `city` varchar(100) NOT NULL,
  `pin` varchar(10) NOT NULL,
  `state` varchar(100) NOT NULL,
  `address_line_1` varchar(200) NOT NULL,
  `address_line_2` varchar(200) DEFAULT NULL,
  `qualification` varchar(20) NOT NULL,
  `joining_date` date NOT NULL,
  PRIMARY KEY (`sid`),
  UNIQUE KEY `phone_no` (`phone_no`),
  UNIQUE KEY `aadhar_no` (`aadhar_no`),
  UNIQUE KEY `pan` (`pan`),
  UNIQUE KEY `voter_id` (`voter_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `surveyor_details`
--

LOCK TABLES `surveyor_details` WRITE;
/*!40000 ALTER TABLE `surveyor_details` DISABLE KEYS */;
INSERT INTO `surveyor_details` VALUES ('SURV-61257b55','Sagar','Nagbanshi','8609685671','sagarnag00@gmail.com','57454365675446','2343223','32434564554354','ewewr','54654','sdfsfdsf','gjfteretyiyt','fncvfsdtrtu','dfgdfgfdg','2023-08-28'),('SURV-71e711fc','Sachin','Nagbanshi','8617324472','sachin@realbooks.in','402936109443','4536476565','3242343245','kol','123','wb','dfdsf','sdfsdf','awdasdfas','2023-08-25'),('SURV-b45963ad','virat','kohli','8888888888','virat@gmail.com','3423235','23243','23432234','sdfs','342','sdfsdf','sdfdfhgdfg','dfdgfdg','sdfsdfdsg','2023-09-02');
/*!40000 ALTER TABLE `surveyor_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_details`
--

DROP TABLE IF EXISTS `user_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_details` (
  `uid` varchar(20) NOT NULL,
  `rid` varchar(45) DEFAULT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `phone_no` varchar(20) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `aadhar_no` varchar(16) NOT NULL,
  `pan` varchar(10) NOT NULL,
  `voter_id` varchar(20) NOT NULL,
  `city` varchar(100) NOT NULL,
  `pin` varchar(10) NOT NULL,
  `state` varchar(100) NOT NULL,
  `address_line_1` varchar(200) NOT NULL,
  `address_line_2` varchar(200) DEFAULT NULL,
  `occupation` varchar(20) NOT NULL,
  `is_family_head` enum('yes','no') DEFAULT NULL,
  `no_of_members` varchar(20) NOT NULL,
  `surveyor_name` varchar(100) NOT NULL,
  `surveyor_code` varchar(20) NOT NULL,
  `joining_date` date NOT NULL,
  `relation` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `phone_no` (`phone_no`),
  UNIQUE KEY `aadhar_no` (`aadhar_no`),
  UNIQUE KEY `pan` (`pan`),
  UNIQUE KEY `voter_id` (`voter_id`),
  UNIQUE KEY `uid_UNIQUE` (`uid`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_details`
--

LOCK TABLES `user_details` WRITE;
/*!40000 ALTER TABLE `user_details` DISABLE KEYS */;
INSERT INTO `user_details` VALUES ('USR-25f4e60e','USR-42ea9e67','asdasd','asdasdas','3223523523','abc@gmail.com','234234234','23423423','324234','adfds','234234','edf','asdasdasd','asdasd','asdasd',NULL,'12','Sachin Nagbanshi','SURV-71e711fc','2023-08-31','asdasd'),('USR-42ea9e67',NULL,'Ankit','Nagbanshi','7872771057','ankitnag00@gmail.com','35345667','4536476565','435456546546','dgdff','54646','ghfgdfdh','sdafdsfsd','sdfghgfdgftdfsgf','dfagsdafd','yes','12','Sachin Nagbanshi','SURV-71e711fc','2023-08-25',NULL),('USR-8b92735b',NULL,'Sayan','Bose','9999999999','shona@gmail.com','234543645734543','435345','4353453','sdfsdf','86754','sfds','dsfsdfsd','sdfsdfsfsdgsfsa','sdfdsfdsf','no','34','Sagar Nagbanshi','SURV-61257b55','2023-08-29',NULL),('USR-b6cab18d',NULL,'Rohit','Singh','9064544644','rohit@email.com','4562566989852','345345','45456546','sdfsdfsdfs','54646','dfgdfgdf','errsefgdffsdfdg','sdfghgfdgftdfsgf','fg','no','12','Sachin Nagbanshi','SURV-71e711fc','2023-08-25',NULL),('USR-f50e64f8','USR-42ea9e67','sachin','nag','8000800080','cdf@gmail.com','32523423','3423','32423432','sdfs','dsfs','fdsf','wfsdfsf','sadfsd','sdfsdf',NULL,'12','Sachin Nagbanshi','SURV-71e711fc','2023-08-31','brother');
/*!40000 ALTER TABLE `user_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_master`
--

DROP TABLE IF EXISTS `user_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_master` (
  `id` varchar(20) NOT NULL,
  `rid` varchar(20) DEFAULT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `phone_no` varchar(20) NOT NULL,
  `password1` varchar(200) NOT NULL,
  `password2` varchar(200) NOT NULL,
  `date` varchar(45) NOT NULL,
  `user_type` enum('User','Surveyor') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone_no_UNIQUE` (`phone_no`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_master`
--

LOCK TABLES `user_master` WRITE;
/*!40000 ALTER TABLE `user_master` DISABLE KEYS */;
INSERT INTO `user_master` VALUES ('SURV-61257b55',NULL,'Sagar','Nagbanshi','8609685671','pbkdf2:sha256:600000$7xqrwYJ4JOYrJ6Y3$02afcf515f8b28716a0d6cd2e687f461f5ba8da0596ab4fdd50cee3b9f7fcbe4','pbkdf2:sha256:600000$aEldrs4AsNS4DvQh$ae574bce1972254b7403fd566e911feab8e7b89864ca9709944e0c6561171ec8','2023-08-28 11:42:05.655136','Surveyor'),('SURV-71e711fc',NULL,'Sachin','Nagbanshi','8617324472','pbkdf2:sha256:600000$UoEjWMdLcSfQ8rB0$1e071792e8c1ca5759d82fa465f1aac857bd190009fc6abe3d5050c30354af75','pbkdf2:sha256:600000$3T4ESWgw69ojMFCL$eda57554175ec8dd64341a15343f5e777748e80b55bce286d2f1ddd28ea7bbb5','2023-08-25 11:45:09.904026','Surveyor'),('SURV-b45963ad',NULL,'virat','kohli','8888888888','pbkdf2:sha256:600000$7iA7m2z8bOywFg5M$61bd06a771d9c9dd04ae7449cfd735597147b1215a358e24b5e765094dda7ef6','pbkdf2:sha256:600000$AqYshd34ce9cCQA8$c1d4ce7ff63d1218257694682d53361af753da5981b5b22f6c87cecc5e09bec9','2023-09-02 10:32:57.121083','Surveyor'),('USR-171b57e3','USR-71e711fc','ss','pp','9932167771','pbkdf2:sha256:600000$PnDYb7mmmQsGLR7z$21d5494093619a97ccb0667e377abf35761f4ffd5f02f414b101ba6bb195a11c','pbkdf2:sha256:600000$dF6g3uPNcPFemaF2$e0cd5538b938cd3d64e54d7bd28972e2d8fea26de1ef3cb1ae1bec849b4b6b01','2023-08-31 05:38:49.604523','User'),('USR-42ea9e67','USR-71e711fc','Ankit','Nagbanshi','7872771057','pbkdf2:sha256:600000$Us5EpBBNM8wUxx9k$6125c00d449807d645bb16d832a8903b0f0664bbd7b5645236ef29e930a16644','pbkdf2:sha256:600000$KVEf9MhHiSwki2bW$18c4d387bd9eca4c94218c42ece9c84de77e1a504642d7e2f304f5e1dad9dc38','2023-08-25 11:59:03.060171','User'),('USR-8b92735b','USR-61257b55','Sayan','Bose','9999999999','pbkdf2:sha256:600000$qrUVJ3CzjkHfZgYJ$26f0220c4d942a8cf5cce0ba8f3f9a96effa0c647a0f873547189f0d16aa14ee','pbkdf2:sha256:600000$sWY1mbObEMm8sYvc$601910378d463d0898f30c44541902dad84ef2624ef53d205f4a50e966b5e28c','2023-08-29 07:13:06.618424','User'),('USR-a74886a4','USR-71e711fc','adfass','asdfsdfds','1234567890','pbkdf2:sha256:600000$1E9r5NQiCWRih9Y1$606fded2c9dbab66aa3ba6dd4cd3cfad426feed91b946def1f870f7d15181e18','pbkdf2:sha256:600000$YL9flzdS23wTtUSE$d0a285795c76c38035ee1d9f6fd6b9450b5071523166e2eb358c7ccc9890975d','2023-08-30 10:36:07.721273','User'),('USR-b6cab18d','USR-71e711fc','Rohit','Singh','9064544644','pbkdf2:sha256:600000$ADM7i6fL6F6yzCdl$d73aa0b90a6d2fca70aef3decd910a1a6470282bef37a294c7ecbb9a16b8e379','pbkdf2:sha256:600000$UzhBJcaNKTe5WXIw$fc73b488c031bfa65f7c52c141196a1c74f1d33a3d78248109070a4eec3cda9d','2023-08-25 12:03:45.907720','User');
/*!40000 ALTER TABLE `user_master` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-02 17:39:29
