from __future__ import division
from Net import *


class musicRecom():

    def getSongId(self, musicTitle):
        print(musicTitle)

        res = NetEaseAPI().search(musicTitle)
        return res['result']['songs'][0]['id']

    def musicRank(self, musicDict):
        maxSubCount = 0
        maxLsitCount = 0
        maxMusicCount = 0
        for music in musicDict:
            print(music)
            if musicDict[music]['listSubscribedCount'] > maxSubCount:
                maxSubCount = musicDict[music]['listSubscribedCount']
            if musicDict[music]['listCount'] > maxLsitCount:
                maxLsitCount = musicDict[music]['listCount']
            if musicDict[music]['musicPlayCount'] > maxMusicCount:
                maxMusicCount = musicDict[music]['musicPlayCount']
        for music in musicDict:
            musicDict[music]['score'] = musicDict[music]['listSubscribedCount'] / maxSubCount + musicDict[music]['listCount'] / maxLsitCount + musicDict[music]['musicPlayCount'] / maxMusicCount
        return sorted(musicDict.items(), key=lambda d: d[1]['score'], reverse=True)

