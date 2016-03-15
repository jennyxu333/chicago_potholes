import sqlite3
import datetime


def find_potholes(args_requested):
    '''
    Takes in args_requested: dictionary of search inputs and returns the query statement
    and arguments for finding pothole data based on the search criteria.
    '''
    args = []
    cond = []

    if 'status' in args_requested and args_requested['status'] != '':
        status = args_requested['status']
        cond.append('status = ?')
        args.append(status)

    if 'start_date' in args_requested and args_requested['start_date'] != '':       
        start_date = str(args_requested['start_date'])
        end_date = str(args_requested['end_date'])
        args.append(start_date)
        args.append(end_date)
        cond.append('''creation_date >= ? AND creation_date <= ?''')

    if 'zip_code' in args_requested and args_requested['zip_code'] != '':
        zipcode = args_requested['zip_code']
        args.append(zipcode)
        cond.append('zip = ?')

    if 'urgency' in args_requested and args_requested['urgency'] != '':
        urgency = args_requested['urgency']
        args.append(urgency)
        cond.append('urgency = ?')

    q1 = '''SELECT * FROM potholes WHERE '''
    q2 = " AND ".join(cond)

    query = q1 + q2
    return query, args
    


    