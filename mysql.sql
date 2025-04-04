CREATE DATABASE HaNoi_Foodie;

CREATE TABLE Restaurants (
RestaurantID int PRIMARY KEY AUTO_INCREMENT,
RestaurantName varchar(255) NOT NULL,
Address varchar(255) NOT NULL,
OppeningTime DATETIME,
Rating float
);

CREATE TABLE Dishes (
DishID int PRIMARY KEY AUTO_INCREMENT,
DishName varchar(255) NOT NULL,
Cmt varchar(255),
CONSTRAINT UX_Dishes UNIQUE (Cmt)
);

CREATE TABLE Restaurants_Dishes (
Price BIGINT NOT NULL,
RestaurantID int,
DishID int,
FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID) ,
FOREIGN KEY (DishID) REFERENCES Dishes(DishID) 
);
SELECT 
d.DishID, d.DishName, rd.Price, r.RestaurantName, r.Address, r.OppeningTime, d.Cmt, r.Rating
FROM ((Restaurants_Dishes rd
JOIN Restaurants r ON r.RestaurantID = rd.RestaurantID)
JOIN Dishes d ON d.DishID = rd.DishID); 

SET SQL_SAFE_UPDATES = 0;

