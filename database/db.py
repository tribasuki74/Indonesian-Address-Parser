import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27017')
db=client.parser_ner # database
kodePos=db.kode_pos