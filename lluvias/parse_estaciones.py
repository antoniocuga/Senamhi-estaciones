# -*- coding: utf-8 -*-
import re

codes = [line.rstrip('\n') for line in open('parsing.txt')]

for c in codes:


	print ("%s,%s") % (
		re.search('new GLatLng\((.*),(.*)\);map.addOverlay', c).group(1),
		re.search('new GLatLng\((.*),(.*)\);map.addOverlay', c).group(2),
		re.search("map.addOverlay\(creaMarcador\((.*),(.*) - (.*),'", c).group(2)
		
	)

#re.search('is recorded as deciding (.*) asylum claims', body_text)
#new GLatLng(-6.2083333333333,-77.867166666667);
#var ubica0 = new GLatLng(-6.2083333333333,-77.867166666667);
#map.addOverlay(creaMarcador(ubica0, 'CHACHAPOYAS - 000375', 'Convencional  , Meteorol&oacute;gica ','6 12\' 30\'\' ','77 52\' 1.8\'\' ','AMAZONAS','CHACHAPOYAS','CHACHAPOYAS','000375','M','F'));