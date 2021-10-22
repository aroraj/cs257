'''
Jayti Arora
CS257: Software Design
October 21, 2021
'''

import csv

# (1) Create a dictionary that maps athlete_id -> athlete_name
#       and then save the results in athletes.csv
athletes = {}
original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
athletes_file = open('athletes.csv', 'w')
writer = csv.writer(athletes_file)
heading_row = next(reader) # eat up and ignore the heading row of the data file
for row in reader:
    athlete_id = row[0]
    athlete_name = row[1]
    if athlete_id not in athletes:
        athletes[athlete_id] = athlete_name
        writer.writerow([athlete_id, athlete_name])
original_data_file.close()
athletes_file.close()

# (2) Create a dictionary that maps event_name -> event_id
#       and then save the results in events.csv
events = {}
original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
events_file = open('events.csv', 'w')
writer = csv.writer(events_file)
heading_row = next(reader) # eat up and ignore the heading row of the data file
for row in reader:
    event_name = row[13]
    if event_name not in events:
        event_id = len(events) + 1
        events[event_name] = event_id
        writer.writerow([event_id, event_name])
events_file.close()

# (3) Create a dictionary that maps team_name -> team_id
#       and then save the results in teamss.csv
teams = {}
original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
teams_file = open('teams.csv', 'w')
writer = csv.writer(teams_file)
heading_row = next(reader) # eat up and ignore the heading row of the data file
for row in reader:
    team_name = row[6]
    if team_name not in teams:
        team_id = len(teams) + 1
        teams[team_name] = team_id
        writer.writerow([team_id, team_name])
teams_file.close()

# (4) Create a dictionary that maps game_name -> game_id
#       and then save the results in games.csv
games = {}
original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
games_file = open('games.csv', 'w')
writer = csv.writer(games_file)
heading_row = next(reader) # eat up and ignore the heading row of the data file
for row in reader:
    game_name = row[8]
    if game_name not in games:
        game_id = len(games) + 1
        games[game_name] = game_id
        writer.writerow([game_id, game_name])
games_file.close()

# (5) Create a dictionary that maps olympic_year -> olympic_id
#       and then save the year, id, season, and city in olympics_year.csv
olympics = {}
original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
olympics_file = open('olympics_year.csv', 'w')
writer = csv.writer(olympics_file)
heading_row = next(reader) # eat up and ignore the heading row of the data file
for row in reader:
    olympic_year = row[9]
    olympic_season = row[10]
    olympic_city = row[11]
    if olympic_year not in olympics:
        olympic_id = len(olympics) + 1
        olympics[olympic_year] = olympic_id
        writer.writerow([olympic_id, olympic_year, olympic_season, olympic_city])
olympics_file.close()
original_data_file.close()

# (6) Create a dictionary that maps noc -> noc_id
#       and then saves noc, region, notes, and id in noc_data.csv
noc_regions = {}
noc_info_file = open('noc_regions.csv', 'rU')
reader = csv.reader(noc_info_file)
noc_file = open('noc_data.csv', 'w')
writer = csv.writer(noc_file)
heading_row = next(reader) # eat up and ignore the heading row of the data file
for row in reader:
    noc = row[0]
    region = row[1]
    notes = row[2]
    if noc not in noc_regions:
        noc_id = len(noc_regions) + 1
        noc_regions[noc] = noc_id
        writer.writerow([noc_id, noc, region, notes])
#Confirming that there are no NOCs left out in the noc_regions.csv that are in the athlete_events.csv
original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
heading_row = next(reader) # eat up and ignore the heading row of the data file
for row in reader:
    noc = row[7]
    region = row[6]
    notes = ''
    if noc not in noc_regions:
        noc_id = len(noc_regions) + 1
        noc_regions[noc] = noc_id
        writer.writerow([noc_id, noc, region, notes])
noc_file.close()

# (7) For each row in the original athlete_events.csv file, build a row
#       for our new event_results.csv table
original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
event_results_file = open('event_results.csv', 'w')
writer = csv.writer(event_results_file)
heading_row = next(reader) # eat up and ignore the heading row of the data file
for row in reader:
    athlete_id = row[0]
    event_name = row[13]
    event_id = events[event_name] # this is guaranteed to work by section (2)
    team_name = row[6]
    team_id = teams[team_name] # this is guaranteed to work by section (3)
    game_name = row[8]
    game_id = games[game_name] # this is guaranteed to work by section (4)
    olympic_year = row[9]
    olympic_id = olympics[olympic_year] # this is guaranteed to work by section (5)
    noc = row[7]
    noc_id = noc_regions[noc] # this is guaranteed to work by section (6)
    medal = row[14]
    writer.writerow([athlete_id, event_id, team_id, game_id, olympic_id, noc_id, medal])
event_results_file.close()

