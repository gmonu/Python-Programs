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
