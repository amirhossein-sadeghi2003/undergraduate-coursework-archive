IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'AirlineDB')
BEGIN
    CREATE DATABASE AirlineDB;
END
GO

USE AirlineDB;
GO

IF OBJECT_ID('payment', 'U') IS NOT NULL DROP TABLE payment;
IF OBJECT_ID('reservationlog', 'U') IS NOT NULL DROP TABLE reservationlog;
IF OBJECT_ID('reservation', 'U') IS NOT NULL DROP TABLE reservation;
IF OBJECT_ID('ticket', 'U') IS NOT NULL DROP TABLE ticket;
IF OBJECT_ID('flight', 'U') IS NOT NULL DROP TABLE flight;
IF OBJECT_ID('customer', 'U') IS NOT NULL DROP TABLE customer;
IF OBJECT_ID('airport', 'U') IS NOT NULL DROP TABLE airport;
IF OBJECT_ID('airline', 'U') IS NOT NULL DROP TABLE airline;
GO

IF OBJECT_ID('flightavailability', 'V') IS NOT NULL DROP VIEW flightavailability;
IF OBJECT_ID('activereservations', 'V') IS NOT NULL DROP VIEW activereservations;
IF OBJECT_ID('ticketdetails', 'V') IS NOT NULL DROP VIEW ticketdetails;
IF OBJECT_ID('flighttickets', 'V') IS NOT NULL DROP VIEW flighttickets;
GO

IF OBJECT_ID('gettotalpaidbycustomer', 'FN') IS NOT NULL DROP FUNCTION gettotalpaidbycustomer;
IF OBJECT_ID('getreservationstatus', 'FN') IS NOT NULL DROP FUNCTION getreservationstatus;
IF OBJECT_ID('getsoldticketscount', 'FN') IS NOT NULL DROP FUNCTION getsoldticketscount;
IF OBJECT_ID('searchflights', 'P') IS NOT NULL DROP PROCEDURE searchflights;
IF OBJECT_ID('cancelreservation', 'P') IS NOT NULL DROP PROCEDURE cancelreservation;
IF OBJECT_ID('addnewticket', 'P') IS NOT NULL DROP PROCEDURE addnewticket;
GO

IF OBJECT_ID('insteadofinsertflighttickets', 'TR') IS NOT NULL DROP TRIGGER insteadofinsertflighttickets;
IF OBJECT_ID('logafterreservationconfirm', 'TR') IS NOT NULL DROP TRIGGER logafterreservationconfirm;
IF OBJECT_ID('checkticketpricebeforeinsert', 'TR') IS NOT NULL DROP TRIGGER checkticketpricebeforeinsert;
GO

CREATE TABLE airline (
    airlineid INT PRIMARY KEY,
    airlinename NVARCHAR(100) NOT NULL,
    contactinfo NVARCHAR(200),
    country NVARCHAR(100)
);

CREATE TABLE airport (
    airportid INT PRIMARY KEY,
    airportcode NVARCHAR(10) NOT NULL UNIQUE,
    airportname NVARCHAR(100) NOT NULL,
    city NVARCHAR(100) NOT NULL,
    country NVARCHAR(100) NOT NULL
);

CREATE TABLE customer (
    id INT PRIMARY KEY,
    firstname NVARCHAR(50) NOT NULL,
    lastname NVARCHAR(50) NOT NULL,
    phonenumber NVARCHAR(15),
    dateofbirth DATE,
    address NVARCHAR(200),
    password NVARCHAR(100) NOT NULL
);

CREATE TABLE flight (
    flightid INT PRIMARY KEY,
    airlineid INT NOT NULL,
    departureairportid INT NOT NULL,
    arrivalairportid INT NOT NULL,
    departuretime DATETIME NOT NULL,
    totalcapacity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    CONSTRAINT fk_flight_airline FOREIGN KEY (airlineid) REFERENCES airline(airlineid),
    CONSTRAINT fk_flight_departureairport FOREIGN KEY (departureairportid) REFERENCES airport(airportid),
    CONSTRAINT fk_flight_arrivalairport FOREIGN KEY (arrivalairportid) REFERENCES airport(airportid),
    CONSTRAINT chk_capacity CHECK (totalcapacity > 0),
    CONSTRAINT chk_price CHECK (price > 0),
    CONSTRAINT chk_differentairports CHECK (departureairportid != arrivalairportid)
);

CREATE TABLE ticket (
    ticketid INT PRIMARY KEY,
    flightid INT NOT NULL,
    departuredatetime DATETIME NOT NULL,
    departurelocation NVARCHAR(100) NOT NULL,
    arrivallocation NVARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    customerid INT NOT NULL,
    CONSTRAINT fk_ticket_flight FOREIGN KEY (flightid) REFERENCES flight(flightid),
    CONSTRAINT fk_ticket_customer FOREIGN KEY (customerid) REFERENCES customer(id)
);

CREATE TABLE reservation (
    reservationid INT PRIMARY KEY,
    customerid INT NOT NULL,
    ticketid INT NOT NULL,
    traveldate DATE NOT NULL,
    paidamount DECIMAL(10, 2) NOT NULL,
    status NVARCHAR(20) NOT NULL CHECK (status IN ('confirmed', 'cancelled', 'pending')),
    CONSTRAINT fk_reservation_customer FOREIGN KEY (customerid) REFERENCES customer(id),
    CONSTRAINT fk_reservation_ticket FOREIGN KEY (ticketid) REFERENCES ticket(ticketid),
    CONSTRAINT chk_paidamount CHECK (paidamount >= 0),
    CONSTRAINT uq_reservation_ticket UNIQUE (ticketid)
);

CREATE TABLE payment (
    paymentid INT PRIMARY KEY,
    customerid INT NOT NULL,
    reservationid INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    CONSTRAINT fk_payment_customer FOREIGN KEY (customerid) REFERENCES customer(id),
    CONSTRAINT fk_payment_reservation FOREIGN KEY (reservationid) REFERENCES reservation(reservationid),
    CONSTRAINT chk_amount CHECK (amount >= 0)
);

CREATE TABLE reservationlog (
    logid INT PRIMARY KEY IDENTITY(1,1),
    reservationid INT NOT NULL,
    status NVARCHAR(20) NOT NULL,
    logtime DATETIME NOT NULL,
    FOREIGN KEY (reservationid) REFERENCES reservation(reservationid)
);
GO

INSERT INTO airline (airlineid, airlinename, contactinfo, country) VALUES
(1, 'IranAir', 'info@iranair.com', 'Iran'),
(2, 'MahanAir', 'contact@mahanair.ir', 'Iran'),
(3, 'AsemanAirlines', 'support@asemanair.com', 'Iran');

INSERT INTO airport (airportid, airportcode, airportname, city, country) VALUES
(1, 'IKA', 'ImamKhomeini', 'Tehran', 'Iran'),
(2, 'THR', 'Mehrabad', 'Tehran', 'Iran'),
(3, 'MHD', 'MashhadIntl', 'Mashhad', 'Iran'),
(4, 'SYZ', 'ShirazIntl', 'Shiraz', 'Iran');

INSERT INTO customer (id, firstname, lastname, phonenumber, dateofbirth, address, password) VALUES
(1, 'Ali', 'Rezaei', '09123456789', '1990-05-15', 'Tehran, Valiasr St', 'ali123'),
(2, 'Sara', 'Mohammadi', '09351234567', '1985-08-22', 'Mashhad, Kargar St', 'sara456'),
(3, 'Hossein', 'Hosseini', '09011223344', '1995-03-10', 'Shiraz, Zand St', 'hossein789'),
(4, 'Maryam', 'Ahmadi', '09187654321', '1988-11-30', 'Tehran, Azadi St', 'maryam101');

INSERT INTO flight (flightid, airlineid, departureairportid, arrivalairportid, departuretime, totalcapacity, price) VALUES
(1, 1, 1, 3, '2025-05-01 08:00:00', 150, 1500.00),
(2, 2, 2, 4, '2025-05-02 14:30:00', 120, 1200.00),
(3, 3, 3, 1, '2025-05-03 11:00:00', 100, 1300.00);

INSERT INTO ticket (ticketid, flightid, departuredatetime, departurelocation, arrivallocation, price, customerid) VALUES
(1, 1, '2025-05-01 08:00:00', 'Tehran', 'Mashhad', 1500.00, 1),
(2, 2, '2025-05-02 14:30:00', 'Tehran', 'Shiraz', 1200.00, 2),
(3, 3, '2025-05-03 11:00:00', 'Mashhad', 'Tehran', 1300.00, 3),
(4, 1, '2025-05-01 08:00:00', 'Tehran', 'Mashhad', 1500.00, 4);

INSERT INTO reservation (reservationid, customerid, ticketid, traveldate, paidamount, status) VALUES
(1, 1, 1, '2025-05-01', 1500.00, 'confirmed'),
(2, 2, 2, '2025-05-02', 1200.00, 'pending'),
(3, 3, 3, '2025-05-03', 1300.00, 'confirmed'),
(4, 4, 4, '2025-05-01', 1500.00, 'cancelled');

INSERT INTO payment (paymentid, customerid, reservationid, amount) VALUES
(1, 1, 1, 1500.00),
(2, 2, 2, 600.00),
(3, 3, 3, 1300.00),
(4, 4, 4, 0.00);
GO

CREATE TRIGGER checkTicketPriceBeforeInsert
ON ticket
INSTEAD OF INSERT
AS
BEGIN
    INSERT INTO ticket (ticketid, flightid, departuredatetime, departurelocation, arrivallocation, price, customerid)
    SELECT 
        ticketid, 
        flightid, 
        departuredatetime, 
        departurelocation, 
        arrivallocation, 
        CASE 
            WHEN price < 0 THEN 0 
            ELSE price 
        END, 
        customerid
    FROM inserted;
END;
GO

CREATE TRIGGER logAfterReservationConfirm
ON reservation
AFTER UPDATE
AS
BEGIN
    INSERT INTO reservationlog (reservationid, status, logtime)
    SELECT 
        i.reservationid, 
        i.status, 
        GETDATE()
    FROM inserted i
    JOIN deleted d ON i.reservationid = d.reservationid
    WHERE i.status = 'confirmed' AND d.status != 'confirmed';
END;
GO

CREATE VIEW flightTickets
AS
SELECT 
    f.flightid, 
    f.departuretime, 
    f.totalcapacity, 
    f.price AS flightprice,
    t.ticketid, 
    t.departuredatetime, 
    t.departurelocation, 
    t.arrivallocation, 
    t.price AS ticketprice, 
    t.customerid
FROM flight f
JOIN ticket t ON f.flightid = t.flightid;
GO

CREATE TRIGGER insteadOfInsertFlightTickets
ON flightTickets
INSTEAD OF INSERT
AS
BEGIN
    DECLARE @ticket_count INT;
    DECLARE @total_capacity INT;
    DECLARE @flightid INT;

    SELECT @flightid = flightid FROM inserted;

    SELECT @ticket_count = COUNT(*)
    FROM ticket
    WHERE flightid = @flightid;

    SELECT @total_capacity = totalcapacity
    FROM flight
    WHERE flightid = @flightid;

    IF @total_capacity IS NULL
    BEGIN
        INSERT INTO flight (flightid, airlineid, departureairportid, arrivalairportid, departuretime, totalcapacity, price)
        SELECT flightid, 1, 1, 2, departuretime, totalcapacity, flightprice
        FROM inserted;
        
        SET @total_capacity = (SELECT totalcapacity FROM inserted);
        SET @ticket_count = 0;
    END

    IF @ticket_count < @total_capacity
    BEGIN
        INSERT INTO ticket (ticketid, flightid, departuredatetime, departurelocation, arrivallocation, price, customerid)
        SELECT ticketid, flightid, departuredatetime, departurelocation, arrivallocation, ticketprice, customerid
        FROM inserted;
    END
    ELSE
    BEGIN
        RAISERROR ('Flight capacity is full. Cannot issue more tickets.', 16, 1);
    END
END;
GO

CREATE FUNCTION getSoldTicketsCount (@flightid INT)
RETURNS INT
AS
BEGIN
    DECLARE @soldtickets INT;
    
    SELECT @soldtickets = COUNT(*)
    FROM ticket
    WHERE flightid = @flightid;
    
    RETURN @soldtickets;
END;
GO

CREATE FUNCTION getReservationStatus (@customerid INT, @ticketid INT)
RETURNS NVARCHAR(20)
AS
BEGIN
    DECLARE @status NVARCHAR(20);
    
    SELECT @status = status
    FROM reservation
    WHERE customerid = @customerid AND ticketid = @ticketid;
    
    IF @status IS NULL
        RETURN 'not found';
    
    RETURN @status;
END;
GO

CREATE FUNCTION getTotalPaidByCustomer (@customerid INT)
RETURNS DECIMAL(10, 2)
AS
BEGIN
    DECLARE @totalpaid DECIMAL(10, 2);
    
    SELECT @totalpaid = SUM(amount)
    FROM payment
    WHERE customerid = @customerid;
    
    IF @totalpaid IS NULL
        RETURN 0.00;
    
    RETURN @totalpaid;
END;
GO

CREATE PROCEDURE addNewTicket
    @flightid INT,
    @customerid INT,
    @ticketid INT,
    @departuredatetime DATETIME,
    @departurelocation NVARCHAR(100),
    @arrivallocation NVARCHAR(100),
    @price DECIMAL(10, 2)
AS
BEGIN
    DECLARE @totalcapacity INT;
    DECLARE @soldtickets INT;

    SELECT @totalcapacity = totalcapacity
    FROM flight
    WHERE flightid = @flightid;

    SELECT @soldtickets = COUNT(*)
    FROM ticket
    WHERE flightid = @flightid;

    IF @soldtickets >= @totalcapacity
    BEGIN
        RAISERROR ('Flight capacity is full. Cannot issue ticket.', 16, 1);
        RETURN;
    END

    INSERT INTO ticket (ticketid, flightid, departuredatetime, departurelocation, arrivallocation, price, customerid)
    VALUES (@ticketid, @flightid, @departuredatetime, @departurelocation, @arrivallocation, @price, @customerid);

    SELECT 'Ticket added successfully.' AS result;
END;
GO

CREATE PROCEDURE cancelReservation
    @reservationid INT
AS
BEGIN
    IF NOT EXISTS (SELECT 1 FROM reservation WHERE reservationid = @reservationid)
    BEGIN
        RAISERROR ('Reservation not found.', 16, 1);
        RETURN;
    END

    UPDATE reservation
    SET status = 'cancelled', paidamount = 0.00
    WHERE reservationid = @reservationid;

    UPDATE payment
    SET amount = 0.00
    WHERE reservationid = @reservationid;

    SELECT 'Reservation cancelled successfully.' AS result;
END;
GO

CREATE PROCEDURE searchFlights
    @departurecity NVARCHAR(100),
    @arrivalcity NVARCHAR(100),
    @traveldate DATE
AS
BEGIN
    SELECT 
        f.flightid,
        f.departuretime,
        f.price,
        a1.city AS departurecity,
        a2.city AS arrivalcity,
        air.airlinename
    FROM flight f
    JOIN airport a1 ON f.departureairportid = a1.airportid
    JOIN airport a2 ON f.arrivalairportid = a2.airportid
    JOIN airline air ON f.airlineid = air.airlineid
    WHERE a1.city = @departurecity 
    AND a2.city = @arrivalcity
    AND CAST(f.departuretime AS DATE) = @traveldate;
END;
GO

CREATE VIEW ticketDetails
AS
SELECT 
    t.ticketid,
    t.departuredatetime,
    t.departurelocation,
    t.arrivallocation,
    t.price AS ticketprice,
    c.firstname + ' ' + c.lastname AS customername,
    f.flightid,
    a.airlinename
FROM ticket t
JOIN customer c ON t.customerid = c.id
JOIN flight f ON t.flightid = f.flightid
JOIN airline a ON f.airlineid = a.airlineid;
GO

CREATE VIEW flightAvailability
AS
SELECT 
    f.flightid,
    f.departuretime,
    a1.city AS departurecity,
    a2.city AS arrivalcity,
    f.totalcapacity,
    COUNT(t.ticketid) AS soldtickets,
    f.totalcapacity - COUNT(t.ticketid) AS remainingcapacity
FROM flight f
JOIN airport a1 ON f.departureairportid = a1.airportid
JOIN airport a2 ON f.arrivalairportid = a2.airportid
LEFT JOIN ticket t ON f.flightid = t.flightid
GROUP BY f.flightid, f.departuretime, a1.city, a2.city, f.totalcapacity;
GO

CREATE VIEW activeReservations
AS
SELECT 
    r.reservationid,
    c.firstname + ' ' + c.lastname AS customername,
    t.departurelocation,
    t.arrivallocation,
    r.traveldate,
    r.status,
    r.paidamount
FROM reservation r
JOIN customer c ON r.customerid = c.id
JOIN ticket t ON r.ticketid = t.ticketid
WHERE r.status IN ('confirmed', 'pending');
GO


INSERT INTO airport (airportid, airportcode, airportname, city, country) VALUES
(100, 'TBZ2', 'Tabriz Intl 2', 'Tabriz', 'Iran'),
(101, 'KIH2', 'Kish Intl 2', 'Kish', 'Iran'),
(102, 'AZD2', 'Yazd Intl 2', 'Yazd', 'Iran');


INSERT INTO airline (airlineid, airlinename, contactinfo, country) VALUES
(100, 'KishAir', 'info@kishair.ir', 'Iran'),
(101, 'QeshmAir', 'contact@qeshmair.ir', 'Iran'),
(102, 'TabanAir', 'info@tabanair.ir', 'Iran');

INSERT INTO customer (id, firstname, lastname, phonenumber, dateofbirth, address, password) VALUES
(100, 'Nima', 'Karimi', '09125554433', '1993-04-12', 'Tabriz, Shariati St', 'nima123'),
(101, 'Elham', 'Jafari', '09357778899', '1992-06-18', 'Kish, Pardis Blvd', 'elham321'),
(102, 'Mohammad', 'Yazdi', '09134445566', '1990-01-01', 'Yazd, Azadi Sq', 'mohammad456');

INSERT INTO flight (flightid, airlineid, departureairportid, arrivalairportid, departuretime, totalcapacity, price) VALUES
(100, 100, 100, 1, '2025-05-21 09:00:00', 100, 1450.00),
(101, 101, 101, 2, '2025-05-22 13:00:00', 90, 1200.00),
(102, 102, 102, 3, '2025-05-23 15:30:00', 85, 1300.00);

INSERT INTO ticket (ticketid, flightid, departuredatetime, departurelocation, arrivallocation, price, customerid) VALUES
(100, 100, '2025-05-21 09:00:00', 'Tabriz', 'Tehran', 1450.00, 100),
(101, 101, '2025-05-22 13:00:00', 'Kish', 'Tehran', 1200.00, 101),
(102, 102, '2025-05-23 15:30:00', 'Yazd', 'Mashhad', 1300.00, 102);

INSERT INTO reservation (reservationid, customerid, ticketid, traveldate, paidamount, status) VALUES
(100, 100, 100, '2025-05-21', 1450.00, 'confirmed'),
(101, 101, 101, '2025-05-22', 1200.00, 'pending'),
(102, 102, 102, '2025-05-23', 1300.00, 'confirmed');


INSERT INTO payment (paymentid, customerid, reservationid, amount) VALUES
(100, 100, 100, 1450.00),
(101, 101, 101, 1200.00),
(102, 102, 102, 1300.00);

select * from payment;
select * from reservation;
select * from ticket;
select * from flight;
select * from customer;
select * from airline;
select * from airport;
