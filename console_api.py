"""
    This console application consumes the api.football-data.org api.
    It uses the information supplied by the api in json format to beautifully generate the current premier league standings.
    However, you can pass any other leagues by passing their competition ids.
    Examples are:
    Premier league = 426
    Championship = 427
    League One = 428
    Bundesliga = 430
    Serie B = 441

"""


import http.client
import json
from prettytable import PrettyTable


def main():
    competition_id = '426'
    try:
        connection = http.client.HTTPConnection('api.football-data.org')
        headers = { 'X-Auth-Token': '1e5b51b66d134dbc8a56b83c5c9075c7', 'X-Response-Control': 'minified' }
        connection.request('GET', '/v1/competitions/' + competition_id + '/leagueTable', None, headers)
        response = json.loads(connection.getresponse().read().decode())

        print("%s Latest Table Standings " % competition_name(competition_id))
        my_table = PrettyTable(['#', 'Team', 'Played', 'GD', 'PTS'])

        for team in response['standing']:
            my_table.add_row([team['rank'], team['team'], team['playedGames'], team['goalDifference'], team['points']])

        print(my_table)
    except Exception as e:
        print(type(e))
        print(e)


def competition_name(competition_id):
    try:
        connection = http.client.HTTPConnection('api.football-data.org')
        headers = { 'X-Auth-Token': '1e5b51b66d134dbc8a56b83c5c9075c7', 'X-Response-Control': 'minified' }
        connection.request('GET', '/v1/competitions/' + competition_id, None, headers)
        response = json.loads(connection.getresponse().read().decode())
        connection.close()
        return response['caption']
    except Exception as e:
        print(type(e))
        print(e)


if __name__ == '__main__':
    main()
    
