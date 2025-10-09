import supportfunctions as spf

class RecordsDB:
    def __init__(self, file):
        connections = spf.getRecords(file)