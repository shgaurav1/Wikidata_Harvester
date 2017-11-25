# coding=utf-8
from wikidata.process_wd import Process, WDController
from wikidata.property_wd import Property
from wikidata.reader import Reader
from wikidata.types_wd import EntityID


class ExtractActorProcess(Process):
    def __init__(self,id):
        Process.__init__(self,id)
        self.occupation_prop=Property("P106",True,EntityID())
        self.actor_value_id="Q33999"
        self.data_saved=[]

    def processItem(self,entry):
        if self.occupation_prop.exists(entry):
            try:
                occ_data=self.occupation_prop.extractData(entry)
                if occ_data:
                    if self.actor_value_id in occ_data:
                        self.data_saved.append(entry)
            except Exception as E: # Sometimes data are not well formated :/
                pass


if __name__ =="__main__":
    wikidata_dump="/Users/jacquesfize/LOD_DATASETS/Wikidata/latest-all.json.gz"
    dump = Reader(wikidata_dump, 'utf-8')
    proc1=ExtractActorProcess(1)
    controller = WDController(dump, proc1)
    controller.process_all()

