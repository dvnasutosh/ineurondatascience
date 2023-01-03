DELIMITER //
CREATE PROCEDURE crtbattr()
BEGIN 
    CREATE TABLE IF NOT EXISTS attributes(
        `CRA` INT NOT NULL,
        `Style` VARCHAR,
        `Price` VARCHAR,
        `Rating` DOUBLE,
        `Size` VARCHAR(5),
        `Season` VARCHAR,
        `NeckLine` VARCHAR,
        `SleeveLength` VARCHAR,
        `Material` VARCHAR,
        `FabricType` VARCHAR,
        `DECORATION` VARCHAR,
        `Pattern_type` VARCHAR,
        `RECOMENDATION` BOOLEAN,
        PRIMARY KEY(`CRA`)
    );

END //
CREATE PROCEDURE crtbsls()
BEGIN
    CREATE TABLE IF NOT EXISTS `sales`(
        
        `Dress_ID` INT NOT NULL,
        `Date` DATE NOT NULL,
        `sales` INT
        FOREIGN KEY `Dress_ID`
            REFERENCES attribute(CRA)
            ON UPDATE CASCADE
    );
END
DELIMITER ;

