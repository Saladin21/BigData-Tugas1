#!/home/bigdata/anaconda3/bin/python
import sys
result = {}
for line in sys.stdin:
	media, date, count = line.split(',')
	if result.get(media) is None:
		result[media] = {}
	if result[media].get(date) is None:
		result[media][date] = 0
	result[media][date] += 1

for k1, v1 in result.items():
	for k2, v2 in v1.items():
		print(f"{k1},{k2},{v2}")