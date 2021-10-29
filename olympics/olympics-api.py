'''
Jayti Arora
CS257: Software Design
October 28, 2021
'''
import sys
import argparse
import flask
import json
import psycopg2

#connect to the database
try:
    connection = psycopg2.connect(database='olympics', user='jaytiarora', password='')
    cursor = connection.cursor()
except Exception as e:
    print(e)
    exit()

app = flask.Flask(__name__)

@app.route('/games')
def get_games():
# RESPONSE: a JSON list of dictionaries, each of which represents one
# Olympic games, sorted by year.
   query = '''SELECT *                                          
            FROM olympics
            ORDER BY olympics.year'''
   try:
      cursor.execute(query)
   except Exception as e:
      print(e)
      exit()

   games_list = []
   for game in cursor:
      game_info = {'id':int(game[0]), 'year':int(game[1]), 'season':game[2], 'city':game[3]}
      games_list.append(game_info)
    
   return json.dumps(games_list)
   

@app.route('/nocs')
def get_nocs():
# Returns a JSON list of dictionaries, each of which represents one
# National Olympic Committee, alphabetized by NOC abbreviation.

   query = '''SELECT *                                          
            FROM noc_regions
            ORDER BY noc_regions.noc'''
   try:
      cursor.execute(query)
   except Exception as e:
      print(e)
      exit()

   noc_list = []
   for noc in cursor:
      noc_info = {'abbreviation':noc[1], 'name':noc[2]}
      noc_list.append(noc_info)
    
   return json.dumps(noc_list)

@app.route('/medalists/games/<games_id>')
def get_medalists(games_id):
# Returnsa JSON list of dictionaries, each representing one athlete
# who earned a medal in the specified games.
# If the GET parameter noc=noc_abbreviation is present, this endpoint will return
# only those medalists who were on the specified NOC's team during the specified
# games.
   noc = flask.request.args.get('noc')

   if noc is not None:
      query = '''SELECT athletes.id, athletes.name, athletes.sex, events.sport, events.name, event_results.medal
                  FROM events, athletes, event_results, olympics, noc_regions
                  WHERE olympics.id = %s
                  AND event_results.athlete_id = athletes.id
                  AND event_results.event_id = events.id
                  AND event_results.olympic_id = olympics.id
                  AND event_results.noc_id = noc_regions.id
                  AND noc_regions.noc LIKE %s
                  AND event_results.medal LIKE %s;'''
      try:
         cursor.execute(query, (int(games_id), noc, '%'))
      except Exception as e:
         print(e)
         exit()
   
   else:
      query = '''SELECT athletes.id, athletes.name, athletes.sex, events.sport, events.name, event_results.medal
                  FROM events, athletes, event_results, olympics
                  WHERE olympics.id = %s
                  AND event_results.athlete_id = athletes.id
                  AND event_results.event_id = events.id
                  AND event_results.olympic_id = olympics.id
                  AND event_results.medal LIKE %s;'''
      try:
         cursor.execute(query, (int(games_id), '%'))
      except Exception as e:
         print(e)
         exit()
    
   medalist_list = []
   for medalist in cursor:
      medalist_info = {'athlete_id':int(medalist[0]), 'athlete_name':medalist[1],
      'athlete_sex':medalist[2], 'sport':medalist[3], 'event':medalist[4], 'medal':medalist[5]}
      medalist_list.append(medalist_info)
   
   return json.dumps(medalist_list)

#main functin to parse through the command line
if __name__ == "__main__":
    parser = argparse.ArgumentParser('Olympics Database Flask App')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)