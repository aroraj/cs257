'''
Jayti Arora
CS257: Software Design
'''
import sys
import argparse
import flask
import json


try:
    connection = psycopg2.connect(database='olympics', user='jaytiarora', password='')
    cursor = connection.cursor()
except Exception as e:
    print(e)
    exit()

app = flask.Flask(__name__)

@app.route('/games')
   '''
   REQUEST: /games

   RESPONSE: a JSON list of dictionaries, each of which represents one
   Olympic games, sorted by year. Each dictionary in this list will have
   the following fields.

      id -- (INTEGER) a unique identifier for the games in question
      year -- (INTEGER) the 4-digit year in which the games were held (e.g. 1992)
      season -- (TEXT) the season of the games (either "Summer" or "Winter")
      city -- (TEXT) the host city (e.g. "Barcelona")
   '''
def get_games():
   query = '''SELECT olympics.id, olympics.year, olympics.season, olympics.city                                          
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
   '''
   REQUEST: /nocs

   RESPONSE: a JSON list of dictionaries, each of which represents one
   National Olympic Committee, alphabetized by NOC abbreviation. Each dictionary
   in this list will have the following fields.

      abbreviation -- (TEXT) the NOC's abbreviation (e.g. "USA", "MEX", "CAN", etc.)
      name -- (TEXT) the NOC's full name (see the noc_regions.csv file)
   '''
get_nocs():
   query = '''SELECT olympics.id, olympics.year, olympics.season, olympics.city                                          
            FROM olympics
            ORDER BY olympics.year'''

@app.route('/medalists/games/<games_id>?[noc=noc_abbreviation]')
   '''
   REQUEST: /medalists/games/<games_id>?[noc=noc_abbreviation]

   RESPONSE: a JSON list of dictionaries, each representing one athlete
   who earned a medal in the specified games. Each dictionary will have the
   following fields.

      athlete_id -- (INTEGER) a unique identifier for the athlete
      athlete_name -- (TEXT) the athlete's full name
      athlete_sex -- (TEXT) the athlete's sex as specified in the database ("F" or "M")
      sport -- (TEXT) the name of the sport in which the medal was earned
      event -- (TEXT) the name of the event in which the medal was earned
      medal -- (TEXT) the type of medal ("gold", "silver", or "bronze")

   If the GET parameter noc=noc_abbreviation is present, this endpoint will return
   only those medalists who were on the specified NOC's team during the specified
   games.
   '''

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)