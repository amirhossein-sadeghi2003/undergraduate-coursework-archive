# Phase 1 Proposal Summary

## Initial concept

The team proposed an online travel-reservation system similar to Alibaba. Users would search, compare, and reserve airline tickets, train tickets, and hotel rooms. The proposal emphasized simple booking, price comparison, travel details, secure handling of user information, ratings, and promotional offers.

## Proposed entities

1. **Customer:** identity, name, contact information, date of birth, address, join date, and password.
2. **Ticket:** flight or train number, departure and arrival times and locations, price, status, customer, and reservation.
3. **Flight:** flight number, route, times, capacity, price, and availability status.
4. **Train:** train number, stations, times, capacity, price, and availability status.
5. **Hotel:** name, address, rating, room count, and nightly price.
6. **Hotel Room:** hotel, availability, nightly price, capacity, and reservation dates.
7. **Reservation:** customer, ticket, hotel, room, reservation and travel dates, amount paid, and status.
8. **Payment:** customer, reservation, amount, date, and payment status.

## Proposed relationships

- One customer can create multiple reservations.
- A reservation can contain one or more travel tickets.
- Hotel reservations connect customers with hotels and selected rooms.
- A reservation can include multiple rooms for group or family travel.

## Later revision

The broad flights-trains-hotels scope was reduced after instructor feedback. The subsequent phases retain customers, airlines, airports, flights, tickets, reservations, and payments, while train and hotel functionality is removed.
