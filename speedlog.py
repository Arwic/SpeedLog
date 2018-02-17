import speedtest
import sqlite3

db_filename = "speedtest.db"

def init_db():
    db = sqlite3.connect(db_filename)
    cur = db.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS results 
        (id INTEGER PRIMARY KEY,
        download REAL,
        upload REAL,
        ping REAL,
        server_url TEXT,
        server_lat REAL,
        server_lon REAL,
        server_name TEXT,
        server_country TEXT,
        server_cc TEXT,
        server_sponsor TEXT,
        server_id INTEGER,
        server_url2 TEXT,
        server_host TEXT,
        server_d REAL,
        server_latency REAL,
        timestamp TEXT,
        bytes_sent INTEGER,
        bytes_received INTEGER,
        share TEXT,
        client_ip TEXT,
        client_lat REAL,
        client_lon REAL,
        client_isp REAL,
        client_isprating REAL,
        client_rating REAL,
        client_ispdlavg REAL,
        client_ispulavg REAL,
        client_loggedin INTEGER,
        client_country TEXT);
        ''')
    db.commit()

def insert_results(results):
    db = sqlite3.connect(db_filename)
    cur = db.cursor()
    cur.execute('''
        INSERT INTO results 
        (download,
        upload,
        ping,
        server_url,
        server_lat,
        server_lon,
        server_name,
        server_country,
        server_cc,
        server_sponsor,
        server_id,
        server_url2,
        server_host,
        server_d,
        server_latency,
        timestamp,
        bytes_sent,
        bytes_received,
        share,
        client_ip,
        client_lat,
        client_lon,
        client_isp,
        client_isprating,
        client_rating,
        client_ispdlavg,
        client_ispulavg,
        client_loggedin,
        client_country)
        VALUES 
        (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);
        ''',
        (results['download'],
        results['upload'],
        results['ping'],
        results['server']['url'],
        results['server']['lat'],
        results['server']['lon'],
        results['server']['name'],
        results['server']['country'],
        results['server']['cc'],
        results['server']['sponsor'],
        results['server']['id'],
        results['server']['url2'],
        results['server']['host'],
        results['server']['d'],
        results['server']['latency'],
        results['timestamp'],
        results['bytes_sent'],
        results['bytes_received'],
        results['share'],
        results['client']['ip'],
        results['client']['lat'],
        results['client']['lon'],
        results['client']['isp'],
        results['client']['isprating'],
        results['client']['rating'],
        results['client']['ispdlavg'],
        results['client']['ispulavg'],
        results['client']['loggedin'],
        results['client']['country']))
    db.commit()

def test_speed():
    s = speedtest.Speedtest()
    s.get_servers([])
    s.get_best_server()
    s.download()
    s.upload()
    return s.results.dict()

def main():
    init_db()
    results = test_speed()
    insert_results(results)

if __name__ == "__main__":
    main()
