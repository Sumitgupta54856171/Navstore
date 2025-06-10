import mongoengine

mongoengine.connect(
        db="sessionDB",
        host="localhost",
        port=27017, # or your port number
     )