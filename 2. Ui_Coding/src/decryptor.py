import os
class decryptor():

	def __init__(self,input_file,output_file,path):

		self.input_file = input_file
		self.output_file= output_file


	def func(self):
		try:
			input_file_pointer = open(self.input_file+".txt","br")
		except:
			return self.input_file+" not found!"

		output_file_pointer = open(self.output_file+".txt" , "w")

		byte=input_file_pointer.read(1)
		while byte:
			output_file_pointer.write(chr(ord(byte)-5))
			byte=input_file_pointer.read(1)

		input_file_pointer.close()
		output_file_pointer.close()
		return "Done successfully!"