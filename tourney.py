import requests
from bs4 import BeautifulSoup
from pprint import pprint
from string import Template
import xml.etree.ElementTree as ET
import time


#get all the teams by bracket
# make matchups
# get the list
# start at the middle
# favorite is located at n/2-1
# underdog is located at n/2+1

#api call
#grab_tourney = 'http://api.sportsdatallc.org/ncaamb-{access}{version}/tournaments/{tournament_id}/schedule.xml?api_key={key}'.format(access = 't',
 #                                                                                                                                    version = '3',
  #                                                                                                                                   tournament_id = '83c03d12-e03b-4f71-846c-5d42ba90eeb1',
#grab_tourney = 'http://api.sportsdatallc.org/ncaamb-{access}{version}/tournaments/{tournament_id}/schedule.xml?api_key={key}'.format(access = 't',
 #                                                                                                                                    version = '3',
  #                                                                                                                                   tournament_id = '83c03d12-e03b-4f71-846c-5d42ba90eeb1',
#
#


#tourney_id = '541807c8-9a76-4999-a2ad-c0ba8a553c3d'
#url = 'http://api.sportsdatallc.org/ncaamb-t3/tournaments/541807c8-9a76-4999-a2ad-c0ba8a553c3d/schedule.xml?api_key=h7xctejux9gwa7tdjf99bfge'
#send = requests.get(grab_tourney)
filename = '2015MarchMadness.xml'
#file = open(filename,'wr+')
#file.write(send.content)
#file.close()

def parseXML(filename):
    tree = ET.parse(filename)
    root = tree.getroot()[0]
    for round in root:
        if round.get('sequence') == '1':
            new_root = round
    for bracket in new_root:
        for game in bracket:
            home = game[0].get('alias')
            home_id = game[0].get('id')
            away = game[1].get('alias')
            away_id = game[1].get('id')
            #snag regular season stats for both teams
            print home
            home_url = 'http://api.sportsdatallc.org/ncaamb-{access}{version}/seasontd/{season}/{ncaa_season}/teams/{team_id}/statistics.xml?api_key={key}'.format(access='t',
                                                                                                                                                                   version='3',
                                                                                                                                                                   season='2014',
                                                                                                                                                                   ncaa_season='reg',
                                                                                                                                                                   team_id = home_id,
                                                                                                                                                                   key = 'h7xctejux9gwa7tdjf99bfge')
            print away
            away_url = 'http://api.sportsdatallc.org/ncaamb-{access}{version}/seasontd/{season}/{ncaa_season}/teams/{team_id}/statistics.xml?api_key={key}'.format(access='t',
                                                                                                                                                                   version='3',
                                                                                                                                                                   season='2014',
                                                                                                                                                                   ncaa_season='reg',
                                                                                                                                                                   team_id = away_id,
                                                                                                                                                                   key = 'h7xctejux9gwa7tdjf99bfge')

            time.sleep(1.0)
            home_stats_req = requests.get(home_url)
            time.sleep(1.0)
            away_stats_req = requests.get(away_url)
            home_file = open('%s.xml'%home,'wr+')
            away_file = open('%s.xml'%away,'wr+')
            home_file.write(home_stats_req.content)
            away_file.write(away_stats_req.content)


parseXML(filename)




