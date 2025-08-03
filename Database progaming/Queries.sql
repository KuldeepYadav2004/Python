insert into Person (name,age,city) VALUES("Vijay Verma",23,"Greater Noida");
select* from Person;
insert into Person (name,age,city) 
VALUES
("Mahima Gupta",22," Noida"),
("Pankaj Mishra",21,"Greater Noida");

SELECT*from Person;

select Name,Id from Person;
select*from Person where city = "Greater Noida";
update Person set Name = "Manik Mehta" where id =3;
update Person set Name = "Roshini Verma",age =21,city="noida" where id=4;
update Person set Name = "Happy" where id =3;

DELETE from Person where id =3;


