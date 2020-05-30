import argparse
import logging
import os.path
import sys
import twint


debug = False

logger = logging.getLogger()
logger.disabled = True


def exception_handler(exception_type, exception, traceback, debug_hook=sys.excepthook):
	if debug:
		debug_hook(exception_type, exception, traceback)
	else:
		print(f'{exception_type.__name__}: {exception}')


sys.excepthook = exception_handler


def download_tweets(username, csv, include_links, limit):
	"""
	Downloads tweets from a given Twitter account.
	:param username: Twitter @username to download tweets from.
	:param csv: Whether to output tweets to a CSV file. If `False`, tweets will be output to a text file.
	:param include_links: Whether to include tweets containing links.
	:param limit: Maximum number of tweets to download. `None` to download all.
	"""

	output = f'{username.lower()}'
	output += '.csv' if csv else '.txt'

	config = twint.Config()
	config.Format = '{tweet}'
	config.Hide_output = True
	config.Limit = limit
	config.Links = 'include' if include_links else 'exclude'
	config.Output = output
	config.Username = username

	if csv:
		config.Custom['tweet'] = ['tweet']
		config.Store_csv = True

	if os.path.isfile(output):
		open(output, 'w').close()

	print(f'Downloading tweets for @{username}...')
	twint.run.Search(config)
	print(f'Downloaded tweets to {output}.')


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('username')
	parser.add_argument('-c','--csv', action='store_true', default=False, help='output tweets to a CSV file')
	parser.add_argument(
		'-i',
		'--include_links',
		action='store_true',
		default=False,
		help='include tweets containing links'
	)
	parser.add_argument(
		'-l',
		'--limit',
		help='maximum number of tweets to retrieve. Default = all',
		nargs='?',
		type=int
	)

	args = parser.parse_args()

	if not (args.limit > 0 and args.limit % 20 == 0):
		raise ValueError('`limit` must be a positive multiple of 20.')

	download_tweets(args.username, args.csv, args.include_links, args.limit)
