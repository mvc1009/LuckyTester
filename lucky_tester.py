#!/bin/python3
import sys,os

try:
	import json
except:
	print('[!] json is not installed. Try "pip install json"')
	sys.exit(0)


try:
	import argparse
except:
	print('[!] argparse is not installed. Try "pip install argparse"')
	sys.exit(0)

def test_lucky13(filename):
	with open(filename, 'r') as f:
		data = f.read().split()
		for url in data:
			os.system("testssl -x CBC --quiet --json %s" % url)

def print_results():
	files = os.listdir()
	for file in files:
		if '.json' in file:
			with open(file, 'r') as jsonfile:
				data = json.load(jsonfile)
				for i in data:
					if 'service' in i['id']:
						url = i['ip'].split('/')[0] + ':' + i['port']
						print("• %s\n" % url)
					elif 'cipher' in i['id']:
						cipher = [x for x in i['finding'].split(' ') if x]
						print("	• %s" % cipher[1])
				print("\n")




def main():
	
	# Parsing arguments
	parser = argparse.ArgumentParser(description='LuckyTester is used for enumerate CBC ciphers.\n\n', epilog='Thanks for using me!')
	parser.add_argument('-f', '--file', action='store', dest='file', help='File of URLs to test')
	parser.add_argument('--only-parse', action="store_true", dest='parse', help='Only parse previous results')
	global args
	args =  parser.parse_args()

	#Usage
	if len(sys.argv) < 2:
		parser.print_help()
		sys.exit(0)


	if args.file:
		if not args.parse:
			test_lucky13(args.file)
		print_results()
	else:
		parser.print_help()
		sys.exit()


try:
	if __name__ == "__main__":
		main()
except KeyboardInterrupt:
	print("[!] Keyboard Interrupt. Shutting down")
