import requests, bs4, time, sys

print('''
 Proxy-Parser. hussaroff
''')

def main():
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		       'Accept-Encoding': 'none',
		       'Accept-Language': 'en-US,en;q=0.8',
		       'Connection': 'keep-alive'}
	print("Premium прокси:\nhussaroff - only hussaroff and my donaters\n- быстрые, анонимные прокси. [private bomb DDoS]]\n\nПолучить прокси бесплатно: \n(1) - comp0\n(2) - webanetlabs")
	print("(3) - ab57\n(4) - proxy-daily [Low DDoS / Http/Https]\n(5) - proxy-daily [Bomb DDoS / socks4 + socks5]")
	print("\nЧтобы выбрать сайт с которого парсим, введите его число.")
	parseit = input("Откуда парсим?: ")
	if parseit == '1':
		s = requests.get('http://comp0.ru/proxylist.html', headers=headers)
		b = bs4.BeautifulSoup(s.text, "html.parser")

		html1 = b.select('pre')
		parse = html1[0].getText()
		parsesave = parse

		print('Прокси: \n' + parse)

		# сохранение в текстовый файл.
		saveproxy = input("Сохранить в .txt данный прокси-лист?[Y/N]: ").upper()
		if saveproxy == 'Y':
			print("Сохранится на рабочем столе с названием 'proxy-hussaroff.txt'.")
			savep = open("proxy-hussaroff.txt", "w")
			savep.write(parsesave)
			savep.close()
		elif saveproxy == 'N':
			print("Выключается через 5 секунд.")
			time.sleep(5)
			sys.exit()
		else:
			print("Ответ не верный.")
			time.sleep(5)
			main()
	elif parseit == '2':
		s = requests.get('https://webanetlabs.net/publ/24', headers=headers)
		b = bs4.BeautifulSoup(s.text, "html.parser")

		html1 = b.select('div .eMessage p')
		parse = html1[0].getText()
		html2 = b.select('div .eMessage p')
		parse1 = html2[1].getText()
		html3 = b.select('div .eMessage p')
		parse2 = html3[2].getText()
		parsesave = parse, parse1, parse2

		print('Прокси: \n' + parse + parse1 + parse2)

		# сохранение в текстовый файл.
		saveproxy = input("Сохранить в .txt данный прокси-лист?[Y/N]: ").upper()
		if saveproxy == 'Y':
			print("Сохранится там, где и программа. Даю название 'proxy-hussaroff.txt'.")
			savep = open("proxy-hussaroff.txt", "w")
			savep.write('\n'.join(parsesave))
			savep.close()
		elif saveproxy == 'N':
			print("Выключается через 5 секунд.")
			time.sleep(5)
			sys.exit()
		else:
			print("Ответ не верный.")
			time.sleep(5)
			main()
	elif parseit == '3':
		s = requests.get('https://ab57.ru/proxylist.html', headers=headers)
		b = bs4.BeautifulSoup(s.text, "html.parser")

		html1 = b.select('pre')
		parse = html1[0].getText()
		parsesave = parse

		print('Прокси: \n' + parse)

		# сохранение в текстовый файл.
		saveproxy = input("Сохранить в .txt данный прокси-лист?[Y/N]: ").upper()
		if saveproxy == 'Y':
			print("Сохранится там, где и программа. Даю название 'proxy-hussaroff.txt'.")
			savep = open("proxy-hussaroff.txt", "w")
			savep.write(parsesave)
			savep.close()
		elif saveproxy == 'N':
			print("Выключается через 5 секунд.")
			time.sleep(5)
			sys.exit()
		else:
			print("Ответ не верный.")
			time.sleep(5)
			main()
	elif parseit == '4':
		s = requests.get('http://proxy-daily.com', headers=headers)
		b = bs4.BeautifulSoup(s.text, "html.parser")

		html1 = b.select('center div')
		parse = html1[0].getText()
		parsesave = parse

		print('Прокси: \n' + parse)

		# сохранение в текстовый файл.
		saveproxy = input("Сохранить в .txt данный прокси-лист?[Y/N]: ").upper()
		if saveproxy == 'Y':
			print("Сохранится там, где и программа. Даю название 'proxy-hussaroff.txt'.")
			savep = open("proxy-hussaroff.txt", "w")
			savep.write(parsesave)
			savep.close()
		elif saveproxy == 'N':
			print("Выключается через 5 секунд.")
			time.sleep(5)
			sys.exit()
		else:
			print("Ответ не верный.")
			time.sleep(5)
			main()
	elif parseit == '5':
		s = requests.get('http://proxy-daily.com', headers=headers)
		b = bs4.BeautifulSoup(s.text, "html.parser")

		html2 = b.select('center div')
		parse1 = html2[1].getText()
		html3 = b.select('center div')
		parse2 = html3[2].getText()
		parsesave = parse1#, parse2

		print('Прокси: \n' + parse1)

		# сохранение в текстовый файл.
		saveproxy = input("Сохранить в .txt данный прокси-лист?[Y/N]: ").upper()
		if saveproxy == 'Y':
			print("Сохранится там, где и программа. Даю название 'proxy-hussaroff.txt'.")
			savep = open("proxy-hussaroff.txt", "w")
			savep.write(parsesave)
			savep.close()
		elif saveproxy == 'N':
			print("Выключается через 5 секунд.")
			time.sleep(5)
			sys.exit()
		else:
			print("Ответ не верный.")
			time.sleep(5)
			main()
	else:
		print("\nНужно вводить целое число!\n")
		main()
main()
