/*
Jayti Arora
CS257
October 21, 2021
*/

--Table with athletes and their corresponding ids
CREATE TABLE athletes (
  id INTEGER,
  name TEXT
);

--Table with events and their corresponding ids
CREATE TABLE events (
  id INTEGER,
  name TEXT
);

--Table with teams and their corresponding ids
CREATE TABLE teams (
  id INTEGER,
  name TEXT
);

--Table with games and their corresponding ids
CREATE TABLE games (
  id INTEGER,
  name TEXT
);

--Table with each olympic event including a unqiue id, year, season, and city
CREATE TABLE olympics(
  id INTEGER,
  year TEXT,
  season TEXT,
  city TEXT
);

--Table with each noc, their corrsponding region, notes, and a unique id
CREATE TABLE noc_regions(
  id INTEGER,
  noc TEXT,
  region TEXT,
  notes TEXT
);

--Connector table connecting all the other tables including athletes, events, 
--teams, games, olympics, nocs, and the medals won
CREATE TABLE event_results (
  athlete_id INTEGER,
  event_id INTEGER,
  team_id INTEGER,
  game_id INTEGER,
  olympic_id INTEGER,
  noc_id INTEGER,
  medal TEXT
);