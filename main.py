import requests
from bs4 import BeautifulSoup


def main():

    url = "https://retosdeprogramacion.com/semanales2022"
    req = requests.get(url)

    soup = BeautifulSoup(req.content, 'html.parser')

    challenge = soup.select("""section.palette-1.section.section-left > div > 
                            div > article > h4 > span > span""")[0].text

    pos1 = challenge.find("#") + 1
    pos2 = challenge.find(":", pos1)

    challengeNumber = challenge[pos1: pos2]

    print(f"::set-output name=challengeNumber::{challengeNumber}")


if __name__ == "__main__":
    main()
