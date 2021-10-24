'''
Jayti Arora
CS257: Software Design
October 21, 2021
'''
import argparse
import psycopg2

#parses through the command line to send in the query
def parse():
    #initialize the parser
    parser = argparse.ArgumentParser()

    #add parameters
    parser.add_argument('-a', '--athletes', nargs=1, type=str, const=None, help='Given an NOC, the database will print all the athletes from that NOC if any')
    parser.add_argument('-n', '--noc_medals', action='store_true', help='Lists all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals.')
    parser.add_argument('-y', '--year', nargs=1, type=int, const=None, help='Given a year, lists all the teams and the number of gold medals they won that year if there was an olympics event held that year')
    
    #parse the arguments
    args = parser.parse_args()

    return args

#List the names of all the athletes from a specified NOC.
def query_athletes(search_term, cursor):
  search_string = search_term
  query = '''SELECT DISTINCT athletes.name
            FROM athletes, event_results, noc_regions
            WHERE athletes.id = event_results.athlete_id
            AND noc_regions.id = event_results.noc_id
            AND noc_regions.noc = %s'''
  try:
      cursor.execute(query, (search_string,))
  except Exception as e:
      print(e)
      exit()

  print('===== Athletes from {0} ====='.format(search_string))
  for row in cursor:
      print(row[0])
  print()


#Lists all the NOCs and the number of gold medals they have won, 
#in decreasing order of the number of gold medals
def query_nocs(cursor):
  query = '''SELECT noc_regions.noc, COUNT(event_results.medal)
          FROM noc_regions, event_results
          WHERE event_results.medal = 'Gold'
          AND noc_regions.id = event_results.noc_id
          GROUP BY noc_regions.noc
          ORDER BY COUNT(event_results.medal) DESC'''
  try:
      cursor.execute(query)
  except Exception as e:
      print(e)
      exit()

  print('===== NOC Medals =====')
  for row in cursor:
      print(row[0], row[1])
  print()

#Lists all the teams and the number of gold medals they won in a specified year 
#ordered in decreasing order of the number of gold medals
def query_year(search_term, cursor):
  search_string = search_term
  query = '''SELECT teams.name, COUNT(event_results.medal)                                           
            FROM olympics, teams, event_results                                          
            WHERE event_results.medal = 'Gold'                                                                                
            AND event_results.team_id = teams.id
            AND olympics.year = %s
            GROUP BY teams.name
            ORDER BY COUNT(event_results.medal) DESC'''
  try:
      cursor.execute(query, (search_string,))
  except Exception as e:
      print(e)
      exit()

  print('===== Athletes with Gold Medals in {0} ====='.format(search_string))
  for row in cursor:
    print(f'{row[0]:50s}{row[1]:4d}')
  print()

#main function
def main():
  #parse the arguments sent in for query
  args = parse()

  #connect to the database
  try:
    connection = psycopg2.connect(database='olympics', user='jaytiarora', password='')
  except Exception as e:
    print(e)
    exit()
  
  try:
    cursor = connection.cursor()
  except Exception as e:
    print(e)
    exit()

  #query the database
  if args.athletes:
    query_athletes(args.athletes[0], cursor)
  elif args.noc_medals:
    query_nocs(cursor)
  elif args.year:
    query_year(str(args.year[0]), cursor)
  
  # close the database connection
  connection.close()
  
if __name__ == '__main__':
    main()