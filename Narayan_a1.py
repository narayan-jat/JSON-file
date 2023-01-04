"""
Module for currency exchange This module provides several string parsing functions to
implement a simple currency exchange routine using an online currency service.

The primary function in this module is exchange.

Author :Narayan Jat
Dater :November 30,2022
"""
# Here imported module name requests to get query from website

import requests
def exchange(old ,new ,amt ):
	"""
	Returns the amount of currency received in the given
	exchange. In this exchange, the user is changing amt money in
	currency old to the currency new. The value returned represents
	the amount in currency new.

	The value returned is of float type.

	Parameter old: the currency on hand
	Precondition: old is a string for a valid currency code

	Parameter new: the currency to convert to
	Precondition: new is a string for a valid currency code

	Parameter amt: amount of currency to convert
	Precondition: amt is a float 
	"""
	return float(before_space(get_rhs(query_website(old ,new ,amt ))))

# Function  to cut substring before the space

def before_space(s):
	'''
	Returns the copy of substring upto,not including first space

	Doctests
 	>>> before_space('Narayan Jat')        # testing output when one space between two substring
 	'Narayan'
 	>>> before_space('  Narayan Jat')       # testing output if spaces are provided before any substring
 	''
 	>>> before_space('Narayan   Jat')        # testing output when multiple sapces are between two
 	'Narayan'

	parameters s: string to slice
	precondition : s should be string with at least one space
	'''
	return s[:s.find(' ')].strip()

# function to cut the part of string after space

def after_space(s):
	'''
	Returns a copy of s after the first space

	Doctests
	>>> after_space('Narayan Jat')             # testing when one space between two substring
	'Jat'
	>>> after_space('  Narayan Jat')           # testing when spaces are provided before any substring
	'Narayan Jat'
	>>> after_space('Narayan  Jat')            # testing  when multiple spaces are between two substring
	'Jat'

	Parameter s: the string to slice
	Precondition: s is a string with at least one space
	'''
	return s[s.find(' ') + 1:].strip()

# This is function two find substring in double quotes

def first_inside_quotes(s):
	'''
	Returns the first substring of s between two (double) quotes
	A quote character is one that is inside a string, not one that
	delimits it. We typically use single quotes (') to delimit a
	string if we want to use a double quote character (") inside of it.
	Examples:

	first_inside_quotes('A "B C" D') returns 'B C'
	first_inside_quotes('A "B C" D "E F" G') returns 'B C',

	because it only picks the first such substring

	Doctests:
	>>> first_inside_quotes('ram"siya"ram')       # testing when substring is between two double quotes
	'siya'
	>>> first_inside_quotes('ram "siya" "siya" ram')       #testing when four or more double quotes containing substrings
	'siya'
	>>> first_inside_quotes('ram "si"ya"ram')   # testing when odd number of double quotes in string
	'si'

	Parameter s: a string to search
	Precondition: s is a string containing at least two double quotes
	'''
	return s[s.index('"') + 1:s.index('"',s.index('"') + 1)]

# To get lhs part of json string

def get_lhs(json):
	'''
	Returns the lhs value in the response to a currency query

	Given a JSON response to a currency query, this returns the string inside double quotes (") 
	immediately following the keyword"lhs". For example, if the JSON is
	'{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
	then this function returns '1 Bitcoin' (not '"1 Bitcoin"').
	This function returns the empty string if the JSON response contains an error message.
	Doctests

	>>> get_lhs('"lhs":"5 cup","rhs":"1256.452 Bitcoin","err":""')       # testing when there is no error massage
	'5 cup'

	Parameter json: a json string to parse
	Precondition: json is the response to a currency query	
	'''
	return first_inside_quotes(json[json.index(':'):])

# To get rhs part of json

def get_rhs(json):
	'''
	Returns the rhs value in the response to a currency queryGiven a JSON response to a currency query, 
	this returns thestring inside double quotes (") immediately following the keyword "rhs". 

	For example, if the JSON is '{ "lhs":"1 Bitcoin", "rhs":"19995.85429186 Euros", "err" : "" }'
	then this function returns '19995.85429186 Euros' (not '"38781.518240835 Euros"').

	This function returns the empty string if the JSON response contains an error message.
	Doctests :
	>>> get_rhs('{ "lhs" : "12 euros", "rhs" : "79 cup", "err" : "" }')       # testing when there is no error massage
	'79 cup'

	Parameter json: a json string to parse
	Precondition: json is the response to a currency query
	'''
	return first_inside_quotes(json[json.index('rhs') + 4:])

# Code error testing function  

def has_error(json):
	'''
	Returns True if the query has an error; False otherwise.
	Given a JSON response to a currency query, this returns True if thereis an error message. 

	For example, if the JSON is '{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'
	then the query is not valid, so this function returns True (It does NOT return the message 'Currency amount is invalid.').

	Doctests :
	>>> has_error('{ "lhs":"12 euros", "rhs":"79 cup", "err":"Currency amount is invalid." }')   # testing when there is error in json
	True
	>>> has_error('{ "lhs":"12 euros", "rhs":"79 cup ", "err" : "" }')     # testing when there is no any error
	False

	Parameter json: a json string to parse
	Precondition: json is the response to a currency query
	'''
	return len(first_inside_quotes(json[json.index('err') + 4:])) > 0

# Requesting web to get json

def query_website(old ,new ,amt ):
	'''
	Returns a JSON string that is a response to a currency query. 
	A currency query converts amt money in currency old to the currency new.

	The response should be a string of the form '{ "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'
	where the values old-amount and new-amount contain the value and name for the old and new currencies.
	 If the query is invalid, both old-amount and new-amount will be empty, while"err" 
	 will have an error message.
	 Doctests:
	 >>> query_website('USD','CUP',2.5)           # testing json form 
	 '{ "lhs" : "2.5 United States Dollars", "rhs" : "64.375 Cuban Pesos", "err" : "" }'
	 >>> query_website('usd','CUP',2.0)            # testing when json gorm having error
	 '{ "lhs" : "", "rhs" : "", "err" : "Source currency code is invalid." }'


	Parameter old: the currency on hand
	Precondition: old is a string with no spaces or non-letters

	Parameter new: the currency to convert to 
	Precondition: new is a string with no spaces or non-letters 

	Parameter amt: amount of currency to  convert to 
	precondition : amt is a float
	'''
	target_url=f"http://cs1110.cs.cornell.edu/2022fa/a1/?old={old}&new={new}&amt={amt}"
	json = (requests.get(target_url)).text
	return json

# Teting function for checking enter code validity

def is_currency(code):
	'''
	Returns: True if code is a valid (3 letter code for a currency )It returns False otherwise.

	Parameter code: the currency code to verify
	Precondition: code is a string with no spaces or non-letters.
	
	Doctests:
	>>> is_currency('USD')                        # testing when given currency code is correct
	True
	>>> is_currency('AAA')                        # testing when given currency code is invalid
	False
	'''
	return not(has_error(query_website(code ,code ,amt=5 )))
# this code has been for testing purpose.	
# if __name__=='__main__':
# 	import doctest
# 	doctest.testmod()
