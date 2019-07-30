###############################################################################
# START HERE: Tutorial 3: More advanced scraping. Shows how to follow 'next' 
# links from page to page: use functions, so you can call the same code 
# repeatedly. SCROLL TO THE BOTTOM TO SEE THE START OF THE SCRAPER.
###############################################################################

import scraperwiki
import urlparse
import lxml.html

# scrape_table function: gets passed an individual page to scrape
def scrape_table(jim):
# define the function and call the parameter it will use (aka the cake "filling") as 'jim' - or any other name
    rows = jim.cssselect("table.Trolley.table tr")  # selects all <tr> blocks within <table class="Trolley table"> and puts in list variable 'rows'
# tell the function what it will do with 'jim'
#     My guess is it knows to make a list variable because either 'cssselect' function has that written in or it does it automatically because there are multiple table rows
# If a class name has a space in it, replace this with a . --> "Trolley table" > "Trolley.table"
    for row in rows:
        # Set up our data record - we'll need it later
        record = {}
        table_cells = row.cssselect("td")
        if table_cells: 
            record['Date'] = table_cells[0].text
            record['Hospital'] = table_cells[1].text
            record['Region'] = table_cells[2].text
            record['Trolley total'] = table_cells[3].text
            record['Ward total'] = table_cells[4].text
            # Print out the data we've gathered
            print record, '------------'
            # Finally, save the record to the datastore - 'Artist' is our unique key
            scraperwiki.sqlite.save(["Hospital"], record)
        
# # scrape_and_look_for_next_link function: calls the scrape_table function
def scrape_and_look_for_next_link(starting_url):
# #   HOW DOES IT KNOW WHAT TO PUT IN URL?
    html = scraperwiki.scrape(starting_url)
    print html
    root = lxml.html.fromstring(html)
# define the variable you plan to put into the scrape_table function as its argument (the actual "filling" e.g. custard or jam)
    scrape_table(root)
# when you call scrape_table choose what specific argument you're replacing the parameter (jim) with (root) - ie. custard

# ---------------------------------------------------------------------------
# START HERE: define your starting URL - then 
# call a function to scrape the first page in the series.
# ---------------------------------------------------------------------------

starting_url = 'http://inmo.ie/6022'
scrape_and_look_for_next_link(starting_url)

