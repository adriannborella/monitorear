import os
import requests
from datetime import datetime, timezone
import json

FILE_CONFIG = 'config.json'


class Program():
    token = ''
    url = ''
    files = []

    def __init__(self) -> None:
        self.read_config()
    
    def read_config(self):
        # TODO: leer la configuracion desde el archivo json
        file = open(FILE_CONFIG)
        data = json.load(file)
        file.close()
        
        self.token = data['token']
        self.url = data['url']
        self.files = data['files']

    def request_site(self, file_info):    
        result = requests.get(self.url, file_info)
        return result

    def report_files(self):        
        for ruta in self.files:                   
            stat = os.stat(ruta)
            modified = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc)
            info = {
                'name' : ruta.split('/')[-1],
                'path' : ruta,
                'last_date_update' : modified,
                'token' : self.token
            }
            result = self.request_site(info)

if __name__ == "__main__":
    instance = Program()
    instance.report_files()