import certifi
import requests
import os
import argparse

def dir_path(path):
    if os.path.exists(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_file:{path} is not a valid path")

def parse_arguments():
	parser = argparse.ArgumentParser(description='imports pemfile to truststore')
	parser.add_argument('--pem', type=dir_path)

	return parser.parse_args()

'''
agregar un certificado al trusttore de python
'''
def main_logic(parsed_args):
	cafile = certifi.where()
	pem_file = parsed_args.pem

	print('- target file %s' %(cafile))					
	print('- source file %s' %(pem_file))					

	with open( pem_file, 'rb') as infile:
		customca = infile.read()
	with open(cafile, 'ab') as outfile:
		outfile.write(customca)
		print('That might have worked.')					

def main():
  parsed_args = parse_arguments()
  main_logic(parsed_args)

if __name__ == "__main__":
	main()
