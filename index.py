import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def crickapi():
	html_text = requests.get('https://sports.ndtv.com/cricket/live-scores').text
	soup = BeautifulSoup(html_text, "html.parser")
	sect = soup.find_all('div', class_='sp-scr_wrp ind-hig_crd vevent')

	section = sect
	description = section.find('span', class_='description').text
	location = section.find('span', class_='location').text
	current = section.find('div', class_='scr_dt-red').text
	link = "https://sports.ndtv.com/" + section.find(
	'a', class_='scr_ful-sbr-txt').get('href')

	try:
		status = section.find_all('div', class_="scr_dt-red")[1].text
		block = section.find_all('div', class_='scr_tm-wrp')
		team1_block = block[0]
		team1_name = team1_block.find('div', class_='scr_tm-nm').text
		team1_score = team1_block.find('span', class_='scr_tm-run').text
		team2_block = block[1]
		team2_name = team2_block.find('div', class_='scr_tm-nm').text
		team2_score = team2_block.find('span', class_='scr_tm-run').text
		result = {
			"Description": description,
			"Location": location,
			"Status": status,
			"Current": current,
			"Team A": team1_name,
			"Team A Score": team1_score,
			"Team B": team2_name,
			"Team B Score": team2_score,
			"Full Scoreboard": link,
			"Credits": "NDTV Sports"
		}
	except:
		pass
	return jsonify(result)

if __name__ == "__main__":
	app.run(debug=True)


