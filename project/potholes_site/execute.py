import os
import sys
import stat

def go(arg):
    '''
    Creates the database and updates it with information
    '''
    
    #Grants permission to edit
    traffic = "traffic.py"
    alderman = "aldermen.py"
    update = "update.py"
    os.chmod(traffic, stat.S_IRWXU)
    os.chmod(alderman, stat.S_IRWXU)
    os.chmod(update, stat.S_IRWXU)
    
    #Runs files
    pothole= "python3 potholes.py "+ arg
    traffic = "python3 traffic.py"
    alderman = "python3 aldermen.py"
    update = "python3 update.py chicago.db"
    print("Creating pothole table")
    os.system(pothole)
    print("Creating traffic table")
    os.system(traffic)
    print("Creating alderman table")
    os.system(alderman)
    print("Updating database")
    os.system(update)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 {} <pothole csv file>".format(sys.argv[0]))
        sys.exit(1)

    go(sys.argv[1])
