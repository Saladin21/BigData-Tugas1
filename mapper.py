#!/home/bigdata/anaconda3/bin/python
import json
import sys
import datetime

for line in sys.stdin:
	try:
		data = json.loads(line.strip())
	except Exception as e:
		# sys.stderr.write("unable to read log: %s" % e)
		continue
	if (type(data)is not list):
		continue
	for d in data:
		media = d.get('crawler_target')
		if media is not None:
			media = media.get('specific_resource_type')
		elif media is None and 'instagram' in d.get('link'):
			media = 'instagram'
		elif media is None:
			continue
		if media == 'facebook':
			date = d.get('created_time').split('T')[0]
			print(f"{media},{date},1")
			if len(d.get('comments')['data']) > 0:
				for i in d.get('comments')['data']:
					print(f'{media},{i.get("created_time").split("T")[0]},1')
		elif media == 'instagram':
			date = datetime.datetime.utcfromtimestamp(int(d.get('created_time'))).strftime('%Y-%m-%d')
			print(f"{media},{date},1")
		elif media == 'twitter':
			date = datetime.datetime.strptime(d.get('created_at'), "%a %b %d %H:%M:%S %z %Y").strftime('%Y-%m-%d')
			print(f"{media},{date},1")
		elif media == 'youtube':
			date = d.get('snippet').get('publishedAt')
			if (date is not None):
				print(f"{media},{date.split('T')[0]},1")
		else:
			continue