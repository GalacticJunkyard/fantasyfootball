import requests
import os

def fetch_espn_standings(league_id, season_id):
    print(f"Fetching standings for League ID: {league_id} and Season: {season_id}")
    
    url = f"https://fantasy.espn.com/apis/v3/games/ffl/seasons/{season_id}/segments/0/leagues/{league_id}"
    response = requests.get(url, params={"view": "mStandings"})
    
    if response.status_code == 200:
        print("Standings fetched successfully!")
        return response.json()
    else:
        raise Exception(f"Failed to fetch standings: {response.status_code}, Response: {response.text}")

def parse_standings(standings_data):
    print("Parsing standings data...")
    teams = standings_data["teams"]
    standings = []
    
    for team in teams:
        team_name = team["location"] + " " + team["nickname"]
        wins = team["record"]["overall"]["wins"]
        losses = team["record"]["overall"]["losses"]
        standings.append({"team_name": team_name, "wins": wins, "losses": losses})
    
    print("Standings parsed successfully!")
    return standings

def standings_to_html(standings):
    print("Converting standings to HTML...")
    html = "<table border='1'><tr><th>Team Name</th><th>Wins</th><th>Losses</th></tr>"
    for team in standings:
        html += f"<tr><td>{team['team_name']}</td><td>{team['wins']}</td><td>{team['losses']}</td></tr>"
    html += "</table>"
    
    print("HTML generation successful!")
    return html

# Using your League ID and the current season
league_id = "570788430"  # Your league ID
season_id = 2024  # Update if needed

try:
    standings_data = fetch_espn_standings(league_id, season_id)
    standings = parse_standings(standings_data)
    html_code = standings_to_html(standings)

    # Save the HTML file
    html_file_path = os.path.join(os.getcwd(), "standings.html")
    with open(html_file_path, "w") as file:
        file.write(html_code)

    print(f"HTML file generated and saved at: {html_file_path}")

except Exception as e:
    print(f"Error: {e}")
