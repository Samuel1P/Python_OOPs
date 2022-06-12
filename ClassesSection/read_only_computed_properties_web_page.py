import time
from requests import get
from time import perf_counter

class WebPage:
    def __init__(self, url) -> None:
        self.url = url
        self._page_size = None
        self._time_taken = None
        self._status_code = None
    
    @property
    def page_size(self):
        if self._page_size is None:
            self.make_request()
        return self._page_size

    @property
    def time_taken(self):
        if self._time_taken is None:
            self.make_request()
        return self._time_taken
        
    @property
    def status_code(self):
        if self._status_code is None:
            self.make_request()
        return self._status_code

    def make_request(self):
        print (f"making request to {self.url}")
        start = perf_counter()
        resp = get(url=self.url)
        end = perf_counter()
        self._time_taken = end - start
        self._status_code = resp.status_code
        self._page_size = len(resp.content)

sites = ["http://www.gmail.com", "http://www.facebook.com", "http://www.linkedin.com"]
for site in sites:
    page = WebPage(site)
    print (f"{page.url} took {page.time_taken:.2f} secs to download {format(page.page_size, '_')} with status {page.status_code}")
    print (f"{page.url} took {page.time_taken} to download {page.page_size} with status {page.status_code}")


"""
making request to http://www.gmail.com
http://www.gmail.com took 1.475102503 to download 95493 with status 200
http://www.gmail.com took 1.475102503 to download 95493 with status 200
making request to http://www.facebook.com
http://www.facebook.com took 1.1264945929999999 to download 218683 with status 200
http://www.facebook.com took 1.1264945929999999 to download 218683 with status 200
making request to http://www.linkedin.com
http://www.linkedin.com took 0.776505711 to download 89137 with status 200
http://www.linkedin.com took 0.776505711 to download 89137 with status 200
12:43am sam@macbook:/Python_OOPs > 
"""