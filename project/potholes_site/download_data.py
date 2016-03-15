import webbrowser
def go():
    '''
    Opens the webbrowser to a link that downloads
    the pothole data from the City of Chicago
    '''
    webbrowser.open('https://data.cityofchicago.org/api/views/7as2-ds3y/rows.csv?accessType=DOWNLOAD')

if __name__ == "__main__":
    go()