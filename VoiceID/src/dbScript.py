from voiceid.sr import Voiceid
from voiceid.db import GMMVoiceDB
import os
#
#   create voice db
# print "starting"
# path = "E:\\WorkSpace\\SleepGuard\\training_1\\AdoraSvitak.wav"
# dirs = os.listdir( path )
# 
# # This would print all the files and directories
# for file in dirs:
#    print file
# print "done"  
db = GMMVoiceDB('E:\\WorkSpace\\workspace\\VoiceID\\src\\voiceid')
 
# add models to db: params the basename of 'giov_wave.wav' and the speaker,
#  Giovanni
print "Start Training"
db.add_model('E:\\WorkSpace\\workspace\\VoiceID\\src\\tests\mr_akadin.wav', 'akadin')
print "End Training"
#db.add_model('fran_wave', 'Francesco')
#db.add_model('luca_wave', 'Luca')
 
 
#
#   extract speakers from a file
#
 
# process a video/audio file containing various speakers
print "Start Testing"
v = Voiceid(db, 'E:\\WorkSpace\\workspace\\VoiceID\\src\\tests\mr_akadin.wav')
print "End Testing"
# extract the speakers from file and search into db
print "Start Extracting"
v.extract_speakers()
print "End Extracting" 
# print the clusters (one for every speaker) and relative speakers' names
for c in v.get_clusters():
    cluster = v.get_cluster(c)
    print cluster
    cluster.print_segments()
    print
print "Complete"