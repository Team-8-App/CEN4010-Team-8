-- MySQL dump 10.13  Distrib 8.0.34, for macos13 (arm64)
--
-- Host: ls-b2f10f0f8d1f46949bc16b2a5608934e887eb6b0.c1zf3hrzxwhy.us-east-2.rds.amazonaws.com    Database: team_8
-- ------------------------------------------------------
-- Server version	8.0.34

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `Authors`
--

DROP TABLE IF EXISTS `Authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Authors` (
  `author_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `biography` longtext,
  `publisher` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`author_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Authors`
--

LOCK TABLES `Authors` WRITE;
/*!40000 ALTER TABLE `Authors` DISABLE KEYS */;
INSERT INTO `Authors` VALUES (1,'Jayleen ','Espinal','was a cool person','Wafers'),(2,'this','name','was alive','waffles'),(3,'that','name','here','there'),(4,'waffers','hazelnut','was good','food'),(5,'swiss','cheese','cant think','help'),(6,'brownie','espinal','my dog ','dashund');
/*!40000 ALTER TABLE `Authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BookDetails`
--

DROP TABLE IF EXISTS `BookDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BookDetails` (
  `isbn` varchar(13) NOT NULL,
  `book_name` varchar(255) NOT NULL,
  `description` longtext,
  `price` decimal(10,2) NOT NULL,
  `author_id` int DEFAULT NULL,
  `genre` varchar(100) DEFAULT NULL,
  `publisher` varchar(255) DEFAULT NULL,
  `year_published` int DEFAULT NULL,
  `copies_sold` int DEFAULT '0',
  PRIMARY KEY (`isbn`),
  UNIQUE KEY `isbn_UNIQUE` (`isbn`),
  KEY `author_id` (`author_id`),
  CONSTRAINT `BookDetails_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `Authors` (`author_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BookDetails`
--

LOCK TABLES `BookDetails` WRITE;
/*!40000 ALTER TABLE `BookDetails` DISABLE KEYS */;
INSERT INTO `BookDetails` VALUES ('000-0-00-0000','book_name_1','description_1',1.00,1,'genre_1','publisher_1',2000,1),('111-1-11-1111','book_name_2','description_2',2.00,2,'genre_2','publisher_2',2001,2),('222-2-22-2222','book_name_3','description_3',3.00,3,'genre_3','publisher_3',2002,3),('333-3-33-3333','book_name_4','description_4',4.00,4,'genre_4','publisher_4',2003,4),('444-4-44-4444','book_name_5','description_5',5.00,5,'genre_5','publisher_5',2004,5),('555-5-55-5555','book_name_6','description_6',6.00,6,'genre_6','publisher_6',2005,6),('666-6-66-6666','book_name_7','description_7',7.00,7,'genre_7','publisher_7',2006,7),('777-7-77-7777','book_name_8','description_8',8.00,8,'genre_8','publisher_8',2007,8),('888-8-88-8888','book_name_9','description_9',9.00,9,'genre_9','publisher_9',2008,9),('999-9-99-9999','book_name_10','description_10',10.00,10,'genre_10','publisher_10',2009,10);
/*!40000 ALTER TABLE `BookDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BookRatings`
--

DROP TABLE IF EXISTS `BookRatings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BookRatings` (
  `rating_id` int NOT NULL AUTO_INCREMENT,
  `book_id` int NOT NULL,
  `user_id` int NOT NULL,
  `rating` tinyint NOT NULL,
  `comment` text,
  `datestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`rating_id`),
  KEY `book_id` (`book_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `BookRatings_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `Books` (`book_id`),
  CONSTRAINT `BookRatings_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `UserProfile` (`user_id`),
  CONSTRAINT `BookRatings_chk_1` CHECK (((`rating` >= 1) and (`rating` <= 5)))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BookRatings`
--

LOCK TABLES `BookRatings` WRITE;
/*!40000 ALTER TABLE `BookRatings` DISABLE KEYS */;
INSERT INTO `BookRatings` VALUES (1,0,0,1,'was bad','0000-00-00 00:00:00'),(2,0,0,2,'was alright','0000-00-00 00:00:00'),(3,0,0,3,'was good','0000-00-00 00:00:00'),(4,0,0,4,'was great','0000-00-00 00:00:00'),(5,0,0,5,'was fantastic','0000-00-00 00:00:00'),(6,0,0,4,'was a really good book','0000-00-00 00:00:00');
/*!40000 ALTER TABLE `BookRatings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Books`
--

DROP TABLE IF EXISTS `Books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Books` (
  `book_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `genre` varchar(255) NOT NULL,
  `copies_sold` int DEFAULT '0',
  `rating` decimal(3,2) DEFAULT '0.00',
  `publisher` varchar(255) DEFAULT NULL,
  `discount` decimal(5,2) DEFAULT '0.00',
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Books`
--

LOCK TABLES `Books` WRITE;
/*!40000 ALTER TABLE `Books` DISABLE KEYS */;
INSERT INTO `Books` VALUES (1,'title1','mystery',1,5.00,'waffles',12.00),(2,'title2','Horror',12,3.00,'tattoo',0.00),(3,'title3','fantasy',15000,5.00,'strawberry',23.00),(4,'title4','sci-fi',500,3.00,'entertainment',40.00),(5,'title5','childrens',50000,4.00,'toysrus',10.00),(6,'title6','nonfiction',1,2.00,'roman',0.00);
/*!40000 ALTER TABLE `Books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CartItem`
--

DROP TABLE IF EXISTS `CartItem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CartItem` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `cart_id` int DEFAULT NULL,
  `book_id` int DEFAULT NULL,
  `quantity` int DEFAULT '1',
  `price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`item_id`),
  KEY `cart_id` (`cart_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `CartItem_ibfk_1` FOREIGN KEY (`cart_id`) REFERENCES `ShoppingCart` (`cart_id`),
  CONSTRAINT `CartItem_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `Books` (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CartItem`
--

LOCK TABLES `CartItem` WRITE;
/*!40000 ALTER TABLE `CartItem` DISABLE KEYS */;
INSERT INTO `CartItem` VALUES (1,1,1,1,12.99),(2,1,1,2,20.99),(3,1,1,3,35.99),(4,3,1,4,50.00),(5,NULL,NULL,5,75.00),(6,NULL,NULL,6,120.00);
/*!40000 ALTER TABLE `CartItem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CreditCards`
--

DROP TABLE IF EXISTS `CreditCards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CreditCards` (
  `card_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `card_number` varchar(19) NOT NULL,
  `expiry_date` date NOT NULL,
  `cvv` int NOT NULL,
  `card_holder_name` varchar(255) NOT NULL,
  PRIMARY KEY (`card_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `CreditCards_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `UserProfile` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CreditCards`
--

LOCK TABLES `CreditCards` WRITE;
/*!40000 ALTER TABLE `CreditCards` DISABLE KEYS */;
INSERT INTO `CreditCards` VALUES (1,0,'1','2012-12-21',121,'Jayleen Espinal'),(2,NULL,'2','2002-02-22',222,'cant remember'),(3,NULL,'3','2003-03-23',333,'Remember Name'),(4,NULL,'4','2004-04-24',444,'Person Name'),(5,NULL,'5','2005-03-25',555,'That Person'),(6,NULL,'6','2002-03-23',232,'This Name');
/*!40000 ALTER TABLE `CreditCards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ShoppingCart`
--

DROP TABLE IF EXISTS `ShoppingCart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ShoppingCart` (
  `cart_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`cart_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `ShoppingCart_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `UserProfile` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=324 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ShoppingCart`
--

LOCK TABLES `ShoppingCart` WRITE;
/*!40000 ALTER TABLE `ShoppingCart` DISABLE KEYS */;
INSERT INTO `ShoppingCart` VALUES (1,0),(2,0),(323,0),(3,2),(4,2);
/*!40000 ALTER TABLE `ShoppingCart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserProfile`
--

DROP TABLE IF EXISTS `UserProfile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `UserProfile` (
  `user_id` int NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email_address` varchar(255) DEFAULT NULL,
  `home_address` longtext,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `email_address_UNIQUE` (`email_address`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserProfile`
--

LOCK TABLES `UserProfile` WRITE;
/*!40000 ALTER TABLE `UserProfile` DISABLE KEYS */;
INSERT INTO `UserProfile` VALUES (0,'hello		','hello','hello','hello','hello'),(2,'user','user','name','email@email.com','home!'),(3,'user 3 ','password 3','name 3','email 3','home 3'),(4,'blah','blah','blah','blah@blah.com','blah'),(5,'user_5','password 5','name 5','email 5','home 5'),(6,'a','password','name','email','home'),(10,'Ilknur username','Ilknur','Ilknur','Ilknur','Ilknur address'),(11,'Ilknur_unique','Ilknur_2','Ilknur_2','Ilknur_unique','Ilknur address_2'),(12,'unique_3','unique_4','unique_4','unique_3','unique_4'),(13,'unique_6','unique_6','unique_6','unique_5','unique_6'),(14,'unique_8','unique_8','unique_8','unique_7','unique_8'),(21,'newnew','newnew','newnew','newnew','newnew'),(22,'newnew2','newnew2','newnew2','newnew2','newnew2'),(123,'newuser','newpassword','Updated Name','newuser@example.com','123 New Street'),(1234,'newusertest','newpassword','New User','newusertest@example.com','123 New Street'),(1697429176,'1697429176','newpassword','1697429176','1697429176','123 New Street'),(1697429200,'1697429200','newpassword','1697429200','1697429200','123 New Street');
/*!40000 ALTER TABLE `UserProfile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WishListItems`
--

DROP TABLE IF EXISTS `WishListItems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `WishListItems` (
  `wishlist_item_id` int NOT NULL AUTO_INCREMENT,
  `wishlist_id` int NOT NULL,
  `book_id` int NOT NULL,
  `date_added` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`wishlist_item_id`),
  UNIQUE KEY `wishlist_id` (`wishlist_id`,`book_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `WishListItems_ibfk_1` FOREIGN KEY (`wishlist_id`) REFERENCES `WishLists` (`wishlist_id`),
  CONSTRAINT `WishListItems_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `Books` (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WishListItems`
--

LOCK TABLES `WishListItems` WRITE;
/*!40000 ALTER TABLE `WishListItems` DISABLE KEYS */;
INSERT INTO `WishListItems` VALUES (7,6,0,'0000-00-00 00:00:00'),(8,5,0,'0000-00-00 00:00:00'),(9,4,0,'0000-00-00 00:00:00'),(10,3,0,'0000-00-00 00:00:00'),(11,2,0,'0000-00-00 00:00:00'),(12,1,0,'0000-00-00 00:00:00');
/*!40000 ALTER TABLE `WishListItems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WishLists`
--

DROP TABLE IF EXISTS `WishLists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `WishLists` (
  `wishlist_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `wishlist_name` varchar(255) NOT NULL,
  PRIMARY KEY (`wishlist_id`),
  UNIQUE KEY `user_id` (`user_id`,`wishlist_name`),
  CONSTRAINT `WishLists_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `UserProfile` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WishLists`
--

LOCK TABLES `WishLists` WRITE;
/*!40000 ALTER TABLE `WishLists` DISABLE KEYS */;
INSERT INTO `WishLists` VALUES (3,0,'Christmas'),(1,0,'Cool Books'),(5,0,'Ideas'),(2,0,'Need'),(4,0,'want'),(6,0,'Yeah');
/*!40000 ALTER TABLE `WishLists` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-01 21:43:18
