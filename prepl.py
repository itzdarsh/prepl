import pymongo
from bson.objectid import ObjectId
from prepl_config import *

conn_source = pymongo.MongoClient(source)
conn_target = pymongo.MongoClient(target)


if conn_target['csTrack'].csToken.count_documents({}) == 0:
    stream = conn_source.watch()
else:
    tokens = conn_target['csTrack'].csToken.find().sort([('$natural', -1)]).limit(1)
    conn_target['csTrack'].csToken.drop()
    conn_target['csTrack'].create_collection('csToken',capped=True, size=1000)
    for token in tokens:
        resumeToken = token['_id']
        stream = conn_source.watch(resume_after=resumeToken)

for change in stream:
    db = change['ns']['db']
    if db in doDB or db not in  ignoreDB:
        coll = change['ns']['coll']
        tdb = conn_target[db]
        conn_target['csTrack'].csToken.insert_one({'_id':change['_id']})
        if(change['operationType'] == 'insert'):
            tdb[coll].insert_many([change['fullDocument']])
            print(change)
        elif(change['operationType'] == 'update'):
            tdb[coll].update_one(change['documentKey'],{"$set":change['updateDescription']['updatedFields']})
        elif(change['operationType'] == 'delete'):
            tdb[coll].delete_one(change['documentKey'])
        elif(change['operationType'] == 'drop'):
            tdb[coll].drop()



        
        



  


