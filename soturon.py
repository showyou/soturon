#!/usr/bin/env python
#! -*- coding:utf-8 -*-

# 卒論bot
# userは固定で
import twitterscraping
import simplejson
import datetime
import toDate
import random

# ここに卒論書いてる人の名前入れる
user = [ "mickey24" ]

# .user/twdataは自分で作ったアカウントのuserとpasswd入れてね
userdata = simplejson.loads(open(".user/twdata","r").read())
t = twitterscraping.Twitter(userdata)
latest = datetime.datetime.now()
for u in user:
	twitList = t.getWithUser(u)
	for uu in twitList:
		if True:
			print uu[0],
			print ":",
			print uu[1].encode("utf-8"),
			print toDate.toDate(uu[2])

		# 最終更新時刻以前のログはカット
		# timedelta内引数かえると過去n以内の発言に引っかかるようにする
		if latest - toDate.toDate(uu[2]) > datetime.timedelta(minutes =10) :
			print "pass"
			continue;

		print "hit"
		strResult = "@"+uu[0]+" "
		strResult += random.choice([u"論文かけ",u"あともうちょっとよ！",u"ほーらかかんか",u"dn"])
		strResult = strResult.encode('utf-8')
		t.put(unicode(strResult,'utf-8','ignore'))
		break
