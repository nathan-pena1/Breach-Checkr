import sys
import hashlib
import requests

def sha1_generator(password):
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return hashed_password

def request_api_data(hash_chars):
    url = 'https://api.pwnedpasswords.com/range/' + hash_chars
    api_response = requests.get(url)
    if api_response.status_code != 200:
        raise RuntimeError(f'Error fetching data: {api_response.status_code}, please check api and try again.')
    return api_response

def leaked_password_check(hashes, hash_tail):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hex, leak_count in hashes:
        if hex == hash_tail:
            return int(leak_count)
    return 0


def api_data_check(hashed_password):
    first5, hash_tail = hashed_password[:5], hashed_password[5:]
    api_response = request_api_data(first5)
    return leaked_password_check(api_response, hash_tail)

def main(passwords):
    for password in passwords:
        hashed_password = sha1_generator(password)
        count = api_data_check(hashed_password)
        print(f'Your password: \"{password}\" has appeared in a data leak {count} times.')

print('\nWelcome to Breach-Checkr - The most secure way to check for password leaks.\n')
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
