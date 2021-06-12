import sys
def input_file_names():
	input_file=input("Enter the name of Encrpted File:")
	input_file=open_files(input_file,"br")
	output_file=input("Enter the name of Output Decrypted File:")
	output_file = open_files(output_file,"w")

	encryption_function(input_file,output_file)

def open_files(file_name,mode="w"):
	if mode == "w":
		file_pointer = open(file_name+".txt" , "w")
		
	elif mode== "br":
		try:
			file_pointer=open(file_name+".txt","br")
		except:
			print("{} not Found".format(file_name))
			input("Press any key to exit!")
			sys.exit()
	return file_pointer


def close_files(original_file_pointer,encrypted_file_pointer):
	original_file_pointer.close()
	encrypted_file_pointer.close()
	
	



def encryption_function(original_file_pointer,encrypted_file_pointer):
	
	byte=original_file_pointer.read(1)
	while byte:
		encrypted_file_pointer.write(chr(ord(byte)-5))
		byte=original_file_pointer.read(1)

	close_files(original_file_pointer,encrypted_file_pointer)





if __name__ == "__main__":
	input_file_names()
	input("Done!")

	


	

	
