/*
Jayti Arora
CS257
October 21, 2021
*/

--List all the NOCs (National Olympic Committees), in alphabetical order by abbreviation.
SELECT noc_regions.noc
FROM noc_regions
ORDER BY noc_regions.noc;


--List the names of all the athletes from Kenya. If your database design allows it, sort the athletes by last name.
--Note:My database does not split first and last names so the sort is by first name.
SELECT DISTINCT athletes.name                                                 
FROM athletes, teams, event_results                                          
WHERE athletes.id = event_results.athlete_id                                    
AND teams.name = 'Kenya'                                                   
AND event_results.team_id = teams.id
ORDER BY athletes.name;

--List all the medals won by Greg Louganis, sorted by year. Include whatever fields in this output that you think appropriate.
SELECT event_results.medal, olympics.season, olympics.year
FROM event_results, athletes, olympics
WHERE athletes.name = 'Greg Louganis'
AND athletes.id = event_results.athlete_id
AND olympics.id = event_results.olympic_id
ORDER BY olympics.year;

--List all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals.
SELECT noc_regions.noc, COUNT(event_results.medal)
FROM noc_regions, event_results
WHERE event_results.medal = 'Gold'
AND noc_regions.id = event_results.noc_id
GROUP BY noc_regions.noc
ORDER BY COUNT(event_results.medal) DESC;
