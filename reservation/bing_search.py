import json
import urllib
import urllib.request as urllib2

BING_API_KEY = '0a65bff1f2074718bf24ad3fd8160e19'

def run_query(search_terms):
    root_url = 'https://bingapis.azure-api.net/api/v5/search/'

    count = 10
    safesearch = 'Moderate'
    offset = 0

    # Wrap quotes around our query terms as required by the Bing API.
    # The query we will then use is stored within variable query.
    query = "'{0}'".format(search_terms)
    query = urllib.parse.quote(query)

    # Construct the latter part of our request's URL.
    # Sets the format of the response to JSON and sets other properties.
    # Noticed that this URL will change. For more information, click the link below:
    # https://msdn.microsoft.com/en-US/library/mt712546.aspx
    search_url = "{0}?q={1}&count={2}&offset={3}&safesearch={4}".format(
        root_url,
        query,
        count,
        offset,
        safesearch,)

    # Setup authentication with the Bing servers.
    # The username MUST be a blank string, and put in your API key!
    username = ''


    # Create a 'password manager' which handles authentication for us.
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, search_url, username, BING_API_KEY)    

    # Create our results list which we'll populate.
    results = []

    try:
        # Prepare for connecting to Bing's servers.
        #handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        #opener = urllib2.build_opener(handler)
        #urllib2.install_opener(opener)

        # Connect to the server and read the response generated.
        response = urllib2.urlopen(search_url).read()

        # Convert the string response to a Python dictionary object.

        json_response = json.loads(response)

        # Loop through each page returned, populating out results list.
        for result in json_response['d']['results']:
            results.append({
            'title': result['name'],
            'link': result['url'],
            'summary': result['snippet']})
    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError as e:
        print("Error when querying the Bing API")

    # Return the list of results to the calling function.
    return results

