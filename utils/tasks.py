import csv
import requests

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSgvJqfMhrpd8K_BeV9rvmPsBqTWisYCBzdKqyOcXCwUMttOlZFIjqsU1L4dco4JSXdeHyvHInXDvTV/pub?gid=62876918&single=true&output=csv"

sections = ['Erobot App', 'Task', 'UX UI Design', 'Mobile Development (API)', 'Mobile Development (Admin API)',
           'Mobile Development (flutter_bluetooth_serial)', 'API Development', 'Testing & Fix bugs', 'Launch']
           
with requests.Session() as session:
    download = session.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)

    tasks = [x[1] for x in my_list if x[1] != '' and x[1] not in sections]

print(tasks)
