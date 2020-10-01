# Program for finding that the particular string is made up of alphabets or not.
# If not then String will not be accepted by the function
# If yed then String will be accepted
import re 

def run(string): 

	regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
	 
	if(regex.search(string) == None): 
		print("String accepted") 
		
	else: 
		print("String is not accepted.") 
	


if __name__ == '__main__' : 
	
	
	string = "Programming$for$Life"
	
	 
	run(string) 
