#You will need to make sure you have installed the requests module from PyPi (pip install)

import requests #to request API data from api.pwnedpasswords.com
import hashlib #imported to get the hashed type of the password
import sys

def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char #the url for the API where query_char is the hashed pwd
	res = requests.get(url) #store the response
	if res.status_code != 200: #If the response is 400 raise error
		raise RuntimeError('Error fetching: {}, check the api and try again'.forma(res.status_code))
	return res

def get_password_leaks_count(hashes, hash_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines()) #to split the lines for every ':' in every line in the hashes with the same first 5 chars
	for h, count in hashes:
		if h == hash_to_check:
			return count
	return 0 

def pwned_api_check(password):
  	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() #get the hashed pwd for the users pwd
  	first5_char, tail = sha1password[:5], sha1password[5:] #split the pwd for the first 5 chars since you should never share the complete pwd with anything/anyone
  	response = request_api_data(first5_char) #set the API data from api.pwnedpasswords.com to response
  	return get_password_leaks_count(response, tail) #to check the number of types the pwd was included in a pwd breach

def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count: #If >= 1 and the password is not recommended at all!
			print('{} was found {} times... you should probably change your password!'.format(password, count))
		else: #If 0 and the password is good to use
			print('{} was NOT found. Carry on!'.format(password))
	return 'process finished!'

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:])) #running the file with as many arguments provided

