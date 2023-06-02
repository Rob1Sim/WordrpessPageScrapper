from server import start_server
from wpScrapper import start_scrapp

app = start_server()


if __name__ == '__main__':
    start_scrapp()
    app.run(host='0.0.0.0', port=5000)
