import hashlib
import getpass
import argparse
import json

PASSWD_FILE = './etc/passwd'


def validate_user(real, username, password):
    pwhash = hashlib.sha512(password).hexdigest()
    hashes = read_hashes(PASSWD_FILE)
    if(pwhash == hashes.get(username, None)):
        return True
    else:
        return False


def add(username, password=None):
    if password is None:
        password = getpass.getpass('Password?: ')
        if not password:
            print('no password entered')
            return
    pwhash = hashlib.sha512(password).hexdigest()
    data = {username: pwhash}
    new_hashes = read_hashes(PASSWD_FILE)
    if not new_hashes:
        new_hashes = data
    else:
        new_hashes.update(data)
    write_hashes(PASSWD_FILE, new_hashes)


def delete(username):
    hashes = read_hashes(PASSWD_FILE)
    if not hashes:
        return
    else:
        try:
            hashes.pop(username)
        except:
            return
        write_hashes(PASSWD_FILE, hashes)


def read_hashes(conf):
    with open(conf, 'r') as json_hashes:
        try:
            hashes = json.load(json_hashes)
        except:
            # TODO write exception
            hashes = None
        return hashes


def write_hashes(conf, hashes):
    with open(conf, 'w') as json_hashes:
        try:
            json_hashes.write(json.dumps(hashes))
        except:
            # TODO write exception
            print("Oops..")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate or delete an entry in passwd')
    parser.add_argument('username', metavar='username', nargs=1,
                        help='username of the affected user')
    parser.add_argument('--add', action='store_true',
                        help='add a user and hashed password')
    parser.add_argument('--del', dest='delete', action='store_true',
                        help='remove a user and hashed password')
    args = parser.parse_args()
    if(args.add):
        add(args.username[0])
    elif(args.delete):
        delete(args.username[0])
    else:
        print('Something went wrong..')
