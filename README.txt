metro README
==================
This is a basic train ticketing system intended for metro/passenger trains. 
User can select start and end stations and the system will print out the ticket amount.

========================================
The detailed requirements are as below:
========================================

You are a developer who is called in to design the ticketing system of Central Railway.

The railway stations in the central line are:

CST
Masjid
Sandhurst Road
Byculla
Chinchpokli
Currey Road
Parel
Dadar
Matunga
Sion
Kurla
Vidyavihar
Ghatkopar
Vikhroli
Kanjurmarg
Bhandup
Nahur
Mulund
Thane
Kalyan

Travellers can travel in either direction and the stations are in the order as written above

Pricing:

Minimum number of stations for pricing: 5 stations

For every 5 stations, the price of ticket  is 5 rupees.

For eg: if traveller wants to go from CST to Chinchpokli, there are total of 5 stations (including source and destination stations) so the cost will be 5 rupees

If number of stations are less than 5 then the cost would be the minimum unit of pricing

For eg: If traveller wants to go from CST to Masjid, there are total of 2 stations  so the cost for this will be the minimum unit of pricing which is 5 stations and hence cost will be 5 rupees

Another example:
If traveller wants to go from CST to Parel then there are 7 stations, so the price of the ticket should be 10 rupees (5 stations + 2 stations)

Also, if journey is from beginning of the central line to end, then traveller  should get a 20% discount on the ticket


Program Output:
Your program should be an interactive one taking input from the user and printing out the ticket which contains the date/time of ticket, starting station, ending station and the price. 

For eg:
INPUT

Enter starting station: CST
Enter destination station: Chinchpokli

OUTPUT:

===== CENTRAL RAILWAY======
Ticket Date/Time: 5-June-2015 16:00:00

Journey Begin: CST
Journey End: Chinchpokli

Ticket Cost: 5 rupees
============================


Getting Started
---------------
This is a pyramid web application and can be deployed using standard pyramid deployment methods.

- cd <directory containing this file>

- $VENV/bin/python setup.py develop

- $VENV/bin/initialize_metro_db development.ini

- $VENV/bin/pserve development.ini

