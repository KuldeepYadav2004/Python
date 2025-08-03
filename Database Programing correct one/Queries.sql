INSERT into Person(name, AGE, City) VALUES("Vijay Verma", 23, 'Greater Noida');

INSERT into Person(name, AGE, City) 
VALUES
("Mahima Gupta", 22, 'Noida'),
("Pankaj Mishra", 24, 'Greater Noida');

SELECT * from Person;

SELECT Name, Id from Person;

SELECT * FROM Person WHERE City = 'Greater Noida';

UPDATE Person set Name = 'Manik Mehta' where Id = 3;

UPDATE Person set Name = 'Roshini Verma', Age = 21, City = 'New Delhi' where Id = 4;

DELETE FROM Person WHERE Id = 3;

DELETE FROM Person WHERE City = 'Greater Noida';