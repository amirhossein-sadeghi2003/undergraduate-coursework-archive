if object_id('prerequistes', 'U') is not null
	drop table prerequistes;


if object_id('available_courses', 'U') is not null
	drop table available_courses;


if object_id('taken_courses', 'U') is not null
	drop table taken_courses;


if object_id('students', 'U') is not null
	drop table students;


if object_id('teachers', 'U') is not null
	drop table teachers;



if object_id('courses', 'U') is not null
	drop table courses;


if object_id('departments', 'U') is not null
	drop table departments;


create table departments(
	name varchar(20) not null,
	id varchar(5) primary key,
	budget numeric(12,2),
	category varchar(15) check (category in 
	('Engineering', 'Science'))
);


create table teachers(
	first_name varchar(20) not null,
	last_name varchar(30) not null,
	id varchar(10),
	birth_year int,
	department_id varchar(5),
	salary numeric(7,2) default 10000.00,
	primary key (id),
	foreign key (department_id) references departments(id)
	);





create table students(
	first_name varchar(20) not null,
	last_name varchar(30) not null,
	student_number varchar(10) primary key,
	birth_year int,
	department_id varchar(5),
	advisor_id varchar(5),
	foreign key (department_id) references departments(id),
	foreign key (advisor_id) references departments(id)
);

alter table students
add pass_credit int;


create table courses(
	id varchar(10) primary key,
	title varchar(50),
	credits int default 0,
	department_id varchar(5) references departments(id)
)

create table available_courses(
	course_id varchar(10),
	semester varchar(10) check(semester in('fall', 'spring')),
	year int,
	teacher_id varchar(10),
	foreign key (course_id) references courses(id),
	foreign key (teacher_id) references teachers(id)
);

create table taken_courses(
	student_id varchar(10),
	course_id varchar(10),
	semester varchar(10) check(semester in ('fall', 'spring')),
	year int,
	grade int,
	primary key(student_id, course_id, semester, year),
	foreign key (course_id) references courses(id),
	foreign key (student_id) references students(student_number)
);

create table prerequistes(
	course_id varchar(10),
	prereq_id varchar(10),
	primary key(course_id, prereq_id),
	foreign key(course_id) references courses(id),
	foreign key(prereq_id) references courses(id)
)
insert into departments values('a', '1', 1000.00, 'Engineering'), ('b', '2', 2000.00, 'Science'),
('c', '3', 3000.00, 'Science');

insert into teachers values('ali', 'sadeghi', '1', 1300, '1', 1000), ('sina', 'rasooli', '2', 1300, '2', 1000),
('mohsen', 'sadeghi', '3', 1300, '3', 1000);

insert into students values('asghar', 'akbari', '123456' , 1298, '1', '1', 0), ('mohsen', 'moosavi', '123457' , 1398, '2', '2', 5),
('mahla', 'kermani', '123458' , 1348, '3', '3', 12);

insert into courses values('1', 'dd', 3, 1), ('2', 'gg', 2, 2), ('3', 'jj', 2, 3);

insert into available_courses values('1', 'fall', 1400, '1');
insert into available_courses values('2', 'spring', 1401, '2');
insert into available_courses values('3', 'fall', 1404, '3');

insert into taken_courses values('123456', '3', 'fall', 1400, 18);
insert into taken_courses values('123457', '2', 'fall', 1400, 15);
insert into taken_courses values('123458', '1', 'fall', 1400, 14);

insert into prerequistes values (1,2), (2, 3);
select* from departments;
select* from teachers;
select* from students;
select* from courses;
select * from available_courses;
select * from taken_courses;
select * from prerequistes;
---------------------------------
----number 2
select p1.course_id as course_z, p2.prereq_id as course_x
from prerequistes p1 join prerequistes p2 on p1.prereq_id = p2.course_id;
---------------------------------
----number 4
select x.course_id
from available_courses x
where x.teacher_id = '1';
---------------------------------
----number 3
update taken_courses
set taken_courses.grade = taken_courses.grade + 1
where taken_courses.course_id in( select x.course_id
									from available_courses x
									where x.teacher_id = '1');
---------------------------------	
----number 1
select x.student_id
from taken_courses x left join prerequistes q on x.course_id = q.course_id
where q.prereq_id is not null and x.student_id not in(select y.student_id
														from taken_courses y
														where y.course_id = q.prereq_id);