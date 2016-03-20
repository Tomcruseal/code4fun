SELECT Student.ID,Student.Name FROM Student;
SELECT Student.ID,Student.Name,Course.CourseName,Choose.Score FROM Student,Course,Choose;
SELECT * FROM Student ORDER BY ID DESC;
SELECT ID,avg(Score) FROM Choose GROUP BY ID;
SELECT ID,COUNT(CourseID) FROM Choose GROUP BY ID;
SELECT CourseID,COUNT(ID) FROM Choose GROUP BY CourseID;
SELECT ID FROM Choose WHERE CourseID='C1' AND Score>80;
SELECT ID FROM Choose WHERE CourseID='C2';
SELECT Department,AVG(Age) FROM Student GROUP BY Department; 
 
