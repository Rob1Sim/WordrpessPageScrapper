from .scrapPages import WpScrapper

scrapper = WpScrapper()


def start_scrapp():
    """
    Lance le scrapping
    :return:
    """
    scrapper.login()
    scrapper.crawl_website("annuaires/")
