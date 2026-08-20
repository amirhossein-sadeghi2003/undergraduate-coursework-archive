create table airline (
    airlineid int primary key,
    airlinename nvarchar(100) not null,
    contactinfo nvarchar(200),
    country nvarchar(100)
);

create table airport (
    airportid int primary key,
    airportcode nvarchar(10) not null unique,
    airportname nvarchar(100) not null,
    city nvarchar(100) not null,
    country nvarchar(100) not null
);

create table customer (
    id int primary key,
    firstname nvarchar(50) not null,
    lastname nvarchar(50) not null,
    phonenumber nvarchar(15),
    dateofbirth date,
    address nvarchar(200),
    password nvarchar(100) not null
);

create table flight (
    flightid int primary key,
    airlineid int not null,
    departureairportid int not null,
    arrivalairportid int not null,
    departuretime datetime not null,
    totalcapacity int not null,
    price decimal(10, 2) not null,
    constraint fk_flight_airline foreign key (airlineid) references airline(airlineid),
    constraint fk_flight_departureairport foreign key (departureairportid) references airport(airportid),
    constraint fk_flight_arrivalairport foreign key (arrivalairportid) references airport(airportid),
    constraint chk_capacity check (totalcapacity > 0),
    constraint chk_price check (price > 0),
    constraint chk_differentairports check (departureairportid != arrivalairportid)
);

create table ticket (
    ticketid int primary key,
    flightid int not null,
    departuredatetime datetime not null,
    departurelocation nvarchar(100) not null,
    arrivallocation nvarchar(100) not null,
    price decimal(10, 2) not null,
    customerid int not null,
    constraint fk_ticket_flight foreign key (flightid) references flight(flightid),
    constraint fk_ticket_customer foreign key (customerid) references customer(id)
);

create table reservation (
    reservationid int primary key,
    customerid int not null,
    ticketid int not null,
    traveldate date not null,
    paidamount decimal(10, 2) not null,
    status nvarchar(20) not null check (status in ('confirmed', 'cancelled', 'pending')),
    constraint fk_reservation_customer foreign key (customerid) references customer(id),
    constraint fk_reservation_ticket foreign key (ticketid) references ticket(ticketid),
    constraint chk_paidamount check (paidamount >= 0),
    constraint uq_reservation_ticket unique (ticketid)
);

create table payment (
    paymentid int primary key,
    customerid int not null,
    reservationid int not null,
    amount decimal(10, 2) not null,
    constraint fk_payment_customer foreign key (customerid) references customer(id),
    constraint fk_payment_reservation foreign key (reservationid) references reservation(reservationid),
    constraint chk_amount check (amount >= 0)
);

insert into airline (airlineid, airlinename, contactinfo, country) values
(1, 'iranair', 'info@iranair.com', 'iran'),
(2, 'mahanair', 'contact@mahanair.ir', 'iran'),
(3, 'asemanairlines', 'support@asemanair.com', 'iran');

insert into airport (airportid, airportcode, airportname, city, country) values
(1, 'ika', 'imamkhomeini', 'tehran', 'iran'),
(2, 'thr', 'mehrabad', 'tehran', 'iran'),
(3, 'mhd', 'mashhadintl', 'mashhad', 'iran'),
(4, 'syz', 'shirazintl', 'shiraz', 'iran');

insert into customer (id, firstname, lastname, phonenumber, dateofbirth, address, password) values
(1, 'ali', 'rezaei', '09123456789', '1990-05-15', 'tehran, valiasr st', 'ali123'),
(2, 'sara', 'mohammadi', '09351234567', '1985-08-22', 'mashhad, kargar st', 'sara456'),
(3, 'hossein', 'hosseini', '09011223344', '1995-03-10', 'shiraz, zand st', 'hossein789'),
(4, 'maryam', 'ahmadi', '09187654321', '1988-11-30', 'tehran, azadi st', 'maryam101');

insert into flight (flightid, airlineid, departureairportid, arrivalairportid, departuretime, totalcapacity, price) values
(1, 1, 1, 3, '2025-05-01 08:00:00', 150, 1500.00),
(2, 2, 2, 4, '2025-05-02 14:30:00', 120, 1200.00),
(3, 3, 3, 1, '2025-05-03 11:00:00', 100, 1300.00);

insert into ticket (ticketid, flightid, departuredatetime, departurelocation, arrivallocation, price, customerid) values
(1, 1, '2025-05-01 08:00:00', 'tehran', 'mashhad', 1500.00, 1),
(2, 2, '2025-05-02 14:30:00', 'tehran', 'shiraz', 1200.00, 2),
(3, 3, '2025-05-03 11:00:00', 'mashhad', 'tehran', 1300.00, 3),
(4, 1, '2025-05-01 08:00:00', 'tehran', 'mashhad', 1500.00, 4);

insert into reservation (reservationid, customerid, ticketid, traveldate, paidamount, status) values
(1, 1, 1, '2025-05-01', 1500.00, 'confirmed'),
(2, 2, 2, '2025-05-02', 1200.00, 'pending'),
(3, 3, 3, '2025-05-03', 1300.00, 'confirmed'),
(4, 4, 4, '2025-05-01', 1500.00, 'cancelled');

insert into payment (paymentid, customerid, reservationid, amount) values
(1, 1, 1, 1500.00),
(2, 2, 2, 600.00),
(3, 3, 3, 1300.00),
(4, 4, 4, 0.00);

select r.reservationid, c.firstname, c.lastname, t.departurelocation, t.arrivallocation, r.status
from reservation r
join customer c on r.customerid = c.id
join ticket t on r.ticketid = t.ticketid;
go


create trigger checkticketpricebeforeinsert
on ticket
instead of insert
as
begin
    insert into ticket (ticketid, flightid, departuredatetime, departurelocation, arrivallocation, price, customerid)
    select 
        ticketid, 
        flightid, 
        departuredatetime, 
        departurelocation, 
        arrivallocation, 
        case 
            when price < 0 then 0 
            else price 
        end, 
        customerid
    from inserted;
end;
go

insert into ticket (ticketid, flightid, departuredatetime, departurelocation, arrivallocation, price, customerid)
values (5, 1, '2025-05-01 08:00:00', 'tehran', 'mashhad', -500.00, 1);


select price
from ticket
where ticketid = 5;


create table reservationlog (
    logid int primary key identity(1,1),
    reservationid int not null,
    status nvarchar(20) not null,
    logtime datetime not null,
    foreign key (reservationid) references reservation(reservationid)
);
go


create trigger logafterreservationconfirm
on reservation
after update
as
begin
    insert into reservationlog (reservationid, status, logtime)
    select 
        i.reservationid, 
        i.status, 
        getdate()
    from inserted i
    join deleted d on i.reservationid = d.reservationid
    where i.status = 'confirmed' and d.status != 'confirmed';
end;
go

update reservation
set status = 'confirmed'
where reservationid = 2;


select reservationid, status, logtime
from reservationlog
where reservationid = 2;
go


create view flighttickets
as
select 
    f.flightid, 
    f.departuretime, 
    f.totalcapacity, 
    f.price as flightprice,
    t.ticketid, 
    t.departuredatetime, 
    t.departurelocation, 
    t.arrivallocation, 
    t.price as ticketprice, 
    t.customerid
from flight f
join ticket t on f.flightid = t.flightid;
go


create trigger insteadofinsertflighttickets
on flighttickets
instead of insert
as
begin
    declare @ticket_count int;
    declare @total_capacity int;

    
    declare @flightid int;
    select @flightid = flightid from inserted;

   
    select @ticket_count = count(*)
    from ticket
    where flightid = @flightid;

   
    select @total_capacity = totalcapacity
    from flight
    where flightid = @flightid;

    
    if @total_capacity is null
    begin
        insert into flight (flightid, airlineid, departureairportid, arrivalairportid, departuretime, totalcapacity, price)
        select flightid, 1, 1, 2, departuretime, totalcapacity, flightprice
        from inserted;
        
        set @total_capacity = (select totalcapacity from inserted);
        set @ticket_count = 0;
    end

    if @ticket_count < @total_capacity
    begin
        insert into ticket (ticketid, flightid, departuredatetime, departurelocation, arrivallocation, price, customerid)
        select ticketid, flightid, departuredatetime, departurelocation, arrivallocation, ticketprice, customerid
        from inserted;
    end
    else
    begin
        raiserror ('flight capacity is full. cannot issue more tickets.', 16, 1);
    end
end;
go

insert into flighttickets (flightid, departuretime, totalcapacity, flightprice, ticketid, departuredatetime, departurelocation, arrivallocation, ticketprice, customerid)
values (4, '2025-05-04 09:00:00', 2, 2000.00, 6, '2025-05-04 09:00:00', 'tehran', 'shiraz', 2000.00, 1);


select * from flight where flightid = 4;
select * from ticket where ticketid = 6;


insert into flighttickets (flightid, departuretime, totalcapacity, flightprice, ticketid, departuredatetime, departurelocation, arrivallocation, ticketprice, customerid)
values (4, '2025-05-04 09:00:00', 2, 2000.00, 7, '2025-05-04 09:00:00', 'tehran', 'shiraz', 2000.00, 2);
select * from ticket where ticketid = 7;


begin try
    insert into flighttickets (flightid, departuretime, totalcapacity, flightprice, ticketid, departuredatetime, departurelocation, arrivallocation, ticketprice, customerid)
    values (4, '2025-05-04 09:00:00', 2, 2000.00, 8, '2025-05-04 09:00:00', 'tehran', 'shiraz', 2000.00, 3);
end try
begin catch
    select error_message() as errormessage;
end catch;
go

create function getsoldticketscount (@flightid int)
returns int
as
begin
    declare @soldtickets int;
    
    select @soldtickets = count(*)
    from ticket
    where flightid = @flightid;
    
    return @soldtickets;
end;
go

select flightid, dbo.getsoldticketscount(flightid) as soldtickets
from flight;
go

create function getreservationstatus (@customerid int, @ticketid int)
returns nvarchar(20)
as
begin
    declare @status nvarchar(20);
    
    select @status = status
    from reservation
    where customerid = @customerid and ticketid = @ticketid;
    
    if @status is null
        return 'not found';
    
    return @status;
end;
go

select dbo.getreservationstatus(1, 1) as reservationstatus;
go

create function gettotalpaidbycustomer (@customerid int)
returns decimal(10, 2)
as
begin
    declare @totalpaid decimal(10, 2);
    
    select @totalpaid = sum(amount)
    from payment
    where customerid = @customerid;
    
    if @totalpaid is null
        return 0.00;
    
    return @totalpaid;
end;
go

select id, firstname, lastname, dbo.gettotalpaidbycustomer(id) as totalpaid
from customer;
go

create procedure addnewticket
    @flightid int,
    @customerid int,
    @ticketid int,
    @departuredatetime datetime,
    @departurelocation nvarchar(100),
    @arrivallocation nvarchar(100),
    @price decimal(10, 2)
as
begin
    declare @totalcapacity int;
    declare @soldtickets int;

    select @totalcapacity = totalcapacity
    from flight
    where flightid = @flightid;

    select @soldtickets = count(*)
    from ticket
    where flightid = @flightid;

    if @soldtickets >= @totalcapacity
    begin
        raiserror ('flight capacity is full. cannot issue ticket.', 16, 1);
        return;
    end

    insert into ticket (ticketid, flightid, departuredatetime, departurelocation, arrivallocation, price, customerid)
    values (@ticketid, @flightid, @departuredatetime, @departurelocation, @arrivallocation, @price, @customerid);

    select 'ticket added successfully.' as result;
end;
go

exec addnewticket 
    @flightid = 1, 
    @customerid = 2, 
    @ticketid = 8, 
    @departuredatetime = '2025-05-01 08:00:00', 
    @departurelocation = 'tehran', 
    @arrivallocation = 'mashhad', 
    @price = 1500.00;
go

create procedure cancelreservation
    @reservationid int
as
begin
    
    if not exists (select 1 from reservation where reservationid = @reservationid)
    begin
        raiserror ('reservation not found.', 16, 1);
        return;
    end

    
    update reservation
    set status = 'cancelled', paidamount = 0.00
    where reservationid = @reservationid;

    
    update payment
    set amount = 0.00
    where reservationid = @reservationid;

    select 'reservation cancelled successfully.' as result;
end;
go

exec cancelreservation @reservationid = 2;
go

create procedure searchflights
    @departurecity nvarchar(100),
    @arrivalcity nvarchar(100),
    @traveldate date
as
begin
    select 
        f.flightid,
        f.departuretime,
        f.price,
        a1.city as departurecity,
        a2.city as arrivalcity,
        air.airlinename
    from flight f
    join airport a1 on f.departureairportid = a1.airportid
    join airport a2 on f.arrivalairportid = a2.airportid
    join airline air on f.airlineid = air.airlineid
    where a1.city = @departurecity 
    and a2.city = @arrivalcity
    and cast(f.departuretime as date) = @traveldate;
end;
go

exec searchflights @departurecity = 'tehran', @arrivalcity = 'mashhad', @traveldate = '2025-05-01';
go

create view ticketdetails
as
select 
    t.ticketid,
    t.departuredatetime,
    t.departurelocation,
    t.arrivallocation,
    t.price as ticketprice,
    c.firstname + ' ' + c.lastname as customername,
    f.flightid,
    a.airlinename
from ticket t
join customer c on t.customerid = c.id
join flight f on t.flightid = f.flightid
join airline a on f.airlineid = a.airlineid;
go

select * from ticketdetails;
go

create view flightavailability
as
select 
    f.flightid,
    f.departuretime,
    a1.city as departurecity,
    a2.city as arrivalcity,
    f.totalcapacity,
    count(t.ticketid) as soldtickets,
    f.totalcapacity - count(t.ticketid) as remainingcapacity
from flight f
join airport a1 on f.departureairportid = a1.airportid
join airport a2 on f.arrivalairportid = a2.airportid
left join ticket t on f.flightid = t.flightid
group by f.flightid, f.departuretime, a1.city, a2.city, f.totalcapacity;
go

select * from flightavailability where remainingcapacity > 0;
go

create view activereservations
as
select 
    r.reservationid,
    c.firstname + ' ' + c.lastname as customername,
    t.departurelocation,
    t.arrivallocation,
    r.traveldate,
    r.status,
    r.paidamount
from reservation r
join customer c on r.customerid = c.id
join ticket t on r.ticketid = t.ticketid
where r.status in ('confirmed', 'pending');
go

select * from activereservations;
go