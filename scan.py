import subprocess
import base64
import hashlib
import os
import datetime
import json

try:
	from print_color import print
except:
	print("Please install the print_color library. (pip3 install print-color)")
	exit(1)

class Scanner():
	def __init__(self, profiles:dict) -> None:
		self.profiles = profiles

	#コンパイルに失敗した場合はエラー内容を文字列として返す。正常終了した場合はNoneを返す。
	def compile(self, dir:str, files:tuple, entry:str, output:str, exist_main:bool)->str:
		cmd = ""

		if not exist_main:
			with open("{}/main.c".format(dir), 'w') as f:
				f.write(base64.b64decode(entry.encode()).decode('ascii'))
			cmd = 'clang {}/main.c {}/{} -Wall -Wextra -Werror -o output/{}'.format(dir, dir, f" {dir}/".join(files), output)
		else:
			cmd = 'clang {}/{} -Wall -Wextra -Werror -o output/{}'.format(dir, f" {dir}/".join(files), output)

		res = subprocess.run(cmd, shell=True, text=True, capture_output=True)

		if res.returncode == 0:
			return None
		else:
			return res.stderr

	#指定されたバイナリを実行し、標準出力を文字列として返す。タイムアウトになった場合はNoneを返す。
	def excute(self, bainary:str, timeout:float)->str:
		try:
			res = subprocess.run('./output/{}'.format(bainary), shell=True, text=True, capture_output=True, timeout=timeout)
			return res.stdout
		except subprocess.TimeoutExpired:
			return None

	#文字列からSHA256形式のハッシュ値を取得し、16進数の文字列として返す。
	def hash(self, text:str)->str:
		return hashlib.sha256(text.encode()).hexdigest()

	#ファイルとディレクトリが存在するかをチェックする。もし存在しない場合は、ファイルのタイプとファイル名をTupleで返す。
	def exist(self, dir:str, files:tuple)->tuple:
		error = []

		if not os.path.isdir(dir):
			error.append(['Directory', dir])

		for file in files:
			if not os.path.isfile("{}/{}".format(dir, file)):
				error.append(['File', file])

		return	error

	#個々のプロファイルをもとにスキャンを行います。いずれかの項目でエラーが発生した場合はその時点でスキャンが終了します。
	def	scan(self, profile:dict, print_entry:bool):
		e_res = self.exist(profile['scan']['directory'], profile['scan']['files'])

		if not e_res == []:
			for e in e_res:
				print("{} : {}".format(e[0], e[1]), tag='NO EXIST', tag_color='red', color='red')
			return
		else:
			print("Required files and directories found!", tag='EXIST', tag_color='green', color='green')

		c_res = self.compile(profile['scan']['directory'], profile['scan']['files'], profile['scan']['entry'], "{}.out".format(profile['scan']['directory']) ,profile['scan']['exist_main'])

		if not c_res == None:
			print("\n" + c_res, tag='COMPLITE ERROR', tag_color='red', color='red')
			return
		else:
			print("Compiled successfully!", tag='COMPILED', tag_color='green', color='green')

		e_res = self.excute("{}.out".format(profile['scan']['directory']) , profile['scan']['excute_timeout'])

		if e_res == None:
			print("An error occurred or timed out during execution.", tag='EXCUTE ERROR', tag_color='red', color='red')
			return
		else:
			if print_entry:
				print("\n" + base64.b64decode(profile['scan']['entry'].encode()).decode('ascii'), tag='ENTRY POINT', tag_color='yellow', color='magenta')
			print("\n" + e_res, tag='OUTPUT', tag_color='yellow', color='white')

	#プロファイルのリストをもとに、個々のプロファイルのチェックを呼び出す。
	def run(self, profiles:dict, print_entry:bool):
		print("""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
Project : {}
Profile Author : {}
Execution timestamp : {}
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
		""".format(profiles['Project'], profiles['Author'], datetime.datetime.now().timestamp()))

		if not os.path.exists('output'):
			os.makedirs('output')

		for profile in profiles['profiles']:
			print("Start scanning |{}|...".format(profile['name']), tag='INFO', tag_color='cyan', color='cyan')
			scanner.scan(profile, True)
			print("Scan completed |{}|".format(profile['name']), tag='INFO', tag_color='cyan', color='cyan')

		print("""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
All profiles scan completed!
Thanks you! :)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
		""")



if __name__ == '__main__':
	path = input("Please enter profile name : ")
	dic = {}

	try:
		with open(path, 'r') as f:
			dic = json.load(fp=f)
	except:
		print("Could not open profile...")
		exit(1)

	scanner = Scanner({})
	scanner.run(dic, True)