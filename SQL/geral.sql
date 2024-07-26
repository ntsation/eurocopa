# List all player information for Euro 2024
SELECT * FROM datasets.euro2024_players


#Find players from a specific country
SELECT * FROM datasets.euro2024_players
WHERE Country = 'Portugal'


# List players by age (youngest to oldest)
SELECT * FROM datasets.euro2024_players
ORDER BY Age ASC


# List players over 30 years
SELECT * FROM datasets.euro2024_players
WHERE Age > 30


# Find the 10 most valuable players
SELECT * FROM datasets.euro2024_players
ORDER BY marketvalue DESC
limit 10


# Count the number of players per country
SELECT Country, COUNT(*) as PlayersCount
FROM datasets.euro2024_players
GROUP BY Country


# Calculate the average height of players by position 
SELECT Position, AVG(Height) as AverageHeight
FROM datasets.euro2024_players
GROUP BY Position


# List players who scored more than 10 goals 
SELECT * FROM datasets.euro2024_players
WHERE Goals > 10


# Find players who play whit their left foot
SELECT * FROM datasets.euro2024_players
WHERE Foot = 'Left'


# List players and their respective clubs, ordered by market value
SELECT Name, Club, MarketValue
FROM datasets.euro2024_players
ORDER BY MarketValue DESC


# Calculate the average age of players by country
SELECT Country, AVG(Age) as AverageAge
FROM datasets.euro2024_players
GROUP BY Country


# List players with more 50 games played
SELECT * FROM datasets.euro2024_players
WHERE caps > 50


# Find the clubs with the most players in the Euro 2024
SELECT Club, COUNT(*) as PlayersCount
FROM datasets.euro2024_players
GROUP BY Club
ORDER BY PlayersCount DESC
