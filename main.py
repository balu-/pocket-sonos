import os
import pocketcasts
from soco import SoCo

USERNAME = os.environ.get('POCKETCAST_USER')
PASSWORD = os.environ.get('POCKETCAST_PASSWORD')

pocket = pocketcasts.Pocketcasts(USERNAME, PASSWORD)

pList = pocket.get_up_next()

if len(pList) > 0:
	ep = pList[0]
	ep = pocket.get_episode(ep.uuid) # get all attributes
	if ep.playing_status == pocketcasts.Episode.PlayingStatus.Playing:
		print("Currently Playing: " + str(ep.title) + " "+ str(ep.played_up_to)+" Secounds in")
	else:
		print("Next up: "+str(ep.title))

#player = SoCo('<ip>')
#coordinator = player.group.coordinator
#coordinator.play_uri('<mp3>')