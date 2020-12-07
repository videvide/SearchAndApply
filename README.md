# Semi-automatic job-applier. Crawls, Scrapes, Cleans and Sends.
https://docs.scrapy.org/en/latest/

https://linuxhint.com/install_configure_docker_ubuntu/

https://splash.readthedocs.io/en/stable/install.html

https://github.com/scrapy-plugins/scrapy-splash

sudo docker run -it -p 8050:8050 scrapinghub/splash --disable-private-mode

SCRAPY SHELL EXAMPLE:
scrapy shell 'http://localhost:8050/render.html?url=https://arbetsformedlingen.se/platsbanken/annonser?p=4:apaJ_2ja_LuF&wait=10'

SCRAPY CRAWL EXAMPLE:
scrapy crawl af -s JOBDIR=crawls/af-1 -o af.jl 

'user-input' is any link from where the crawl should start.

With 'user-input' the 'af_spider' and the 'aw_spider' could crawl and scrape either 'Platsbanken' or 'Academic Work' for job-ads of selected type.
'DATA/IT' for Platsbanken(https://arbetsformedlingen.se/platsbanken/annonser?p=4:apaJ_2ja_LuF).
'IT' for Academic work(https://jobs.academicwork.se/it-jobb/?C=IT&s=date).
Both spiders has correct settings to go to next page if this is a first crawl. If not a bit of tweaking is needed, add corresponding value to 'page'.

If you choose to use the 'google_spider' it will crawl google search results of 'user-input' and from linked websites emails will be scraped.
'Digital byrå' at Google(https://www.google.com/search?q=digital+byr%C3%A5). It's IMPORTANT to use this type of query url!

The 'eniro_spider' will crawl the eniro search results of 'user-input' and from linked sites scrape emails.
'Webbyrå' at the 'Företag' section at Eniro(https://www.eniro.se/webbyr%C3%A5/f%C3%B6retag).

You could then clean the data and prepare it for bulk-emailing. This is done with the 'cleaner' and 'appender' .py files.
These are just some python functions, replace the file names with the files you want to use. Duplicates will be removed.
For the Platsbanken data a bit of restructuring is done in order to only have 1 email to use in the sending functions below.

You could then send 500 emails divided by 5. This should only be done each 24h. This 'limit' should be used in order to follow the gmail.smtp 
'bulk-guidelines' and avoiding being black-listed. Add your emails and passwords as envoironment variables with the corresponding names.

The program keeps track of the jobs already applied to. In the end of the emailing function when an email is sent, 
the underlaying item is saved to 'used.txt' which is used for validation. Before sending an email the program checks in the 'used.txt' file,
if the item to be sent excists in the file it moves on to the next one.

To increase execution speed you can save different editions of 'used' lists to avoid reading all lines each time when sending an email. 

# THE USER IS FULLY RESPONSIBLE FOR THE USE OF THIS PROGRAM.

Good luck!
