from update import create_query_dict

def create_alderman(r):
    '''
    Creates a list of alderman objects

    Input:
        r: results from query

    Returns:
        alderman_list: list of alderman objects

    '''
    alderman_list =[]
    for i in r: 
        alderman_list.append(Alderman(i["alderman"], i["email"], i["ward"]))
    return alderman_list


def email_ward(ward, message, db):
    '''
    Emails alderman from a ward a message

    Inputs:
        ward: ward number of alderman
        message: message for alderman
        db: database name

    '''
    query = '''SELECT * FROM aldermen WHERE ward == ?'''
    arg = (int(ward),)
    dic = create_query_dict(query, db, arg)
    alderman = create_alderman(dic)
    alderman = alderman[0]
    alderman.email(message)
    return True 
