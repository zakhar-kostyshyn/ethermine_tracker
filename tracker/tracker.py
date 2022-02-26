from urllib.request import Request, urlopen

import json
import os
import psycopg2
import time
import uuid
from psycopg2 import Error

url = "https://api.ethermine.org/miner/{0}/currentStats".format(os.environ["ETHERMINE_API_KEY"])
headers = {'User-Agent': 'Mozilla/5.0'}
db_name = os.environ['POSTGRES_DB']
db_user = os.environ['POSTGRES_USER']
db_pass = os.environ['POSTGRES_PASSWORD']
db_host = os.environ['POSTGRES_HOST']
db_port = os.environ['POSTGRES_PORT']


def main():
    print(url)
    response = json.load(urlopen(Request(url, headers=headers)))
    data = response["data"]

    try:

        connection = psycopg2.connect(
            user=db_user,
            password=db_pass,
            host=db_host,
            port=db_port,
            database=db_name
        )
        cursor = connection.cursor()

        entry_id = str(uuid.uuid4())
        cursor.execute(
            """
                insert into ethermine(
                    id,
                    time,
                    lastSeen,
                    reportedHashrate,
                    currentHashrate,
                    validShares,
                    invalidShares,
                    staleShares,
                    activeWorkers,
                    averageHashrate,
                    coinsPerMin
                ) values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}')
            """.format(
                entry_id,
                data["time"],
                data["lastSeen"],
                data["reportedHashrate"],
                data["currentHashrate"],
                data["validShares"],
                data["invalidShares"],
                data["staleShares"],
                data["activeWorkers"],
                data["averageHashrate"],
                data["coinsPerMin"],
            )
        )

        connection.commit()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection is not None:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    print("Program started")
    while True:

        print("Main started")
        main()
        print("Main finished")

        print('Go to sleep')
        time.sleep(5 * 60)
        print('Awake')
