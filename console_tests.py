import http.client
import json


def main():
    competition_id = '426'
    try:
        connection = http.client.HTTPConnection('api.football-data.org')
        headers = { 'X-Auth-Token': '1e5b51b66d134dbc8a56b83c5c9075c7', 'X-Response-Control': 'minified' }
        connection.request('GET', '/v1/competitions/' + competition_id + '/leagueTable', None, headers)
        response = json.loads(connection.getresponse().read().decode())

        print("_____________________________________________")
        print("%s Latest Table Standings " % competition_name(competition_id))
        print("_____________________________________________")

        #print("# /t Team /t Played /t GD /t PTS")
        standings = []
        for team in response['standing']:
            standings.append([team['rank'], team['team'], team['playedGames'], team['goalDifference'], team['points']])
        print(standings)
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