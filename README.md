# Wikidata Python API

As a matter of fact, few tools exist fir working on Wikidata dump are using Python and the most
accomplished one is written in Java. 

To fill this void, we propose a simple API that allows python programmers to work on Wikidata dump.
And for those, who are using the Java API, you'll find a lot of similarities, particularly 
 by the use of `Process`

## Requirements

 * Python 3.x
 * python-dateutil
 * setuptools
 
## Installation

    python setup.py install

## How-To

The Wikidata Python API is working using `Process`. A `Process` is basically a object that define
what do you want to process at each entries in Wikidata Dump.

For example, we want to extract all the actors stored in Wikidata, so we define a class that 
inherit from `Process` and look like this:

    class ExtractActorProcess(Process):
        def __init__(self,id):
            Process.__init__(self,id)
    
        def processItem(self,entry):
            pass
        def processProperty(self,entry):
            pass

A `Process` is associated to 3 things:
  * an **ID**
  * a method to process properties (see Wikidata Wiki)
  * a method to process items (see Wikidata Wiki)

In our example, we want to extract all the actors in Wikidata. One way of doing that is extracting
all the entries where the value "Q33999"(actor) is associated to the property "P106"(occupation).

In order to do that, we declare a `Property` instance for the occupation property:

    self.occupation_prop = Property("P106",True,EntityID())
    
N.B: a `Property` instance is defined by 3 parameters:
 * Id of the property *e.g P106, P31, ...*
 * If there is multiple values associated to the property
 * Type of data associated to the property
    * EntityID
    * ExternalIdentifier
    * Coordinates
    * ...
    
Then, knowing that actor are "items", we define the extraction process in the method `processItem()`.

    def processItem(self,entry):
        if self.occupation_prop.exists(entry):
            try:
                occ_data=self.occupation_prop.extractData(entry)
                if occ_data:
                    if self.actor_value_id in occ_data:
                        self.data_saved.append(entry)
            except Exception as E: # Sometimes data are not well formated :/
                pass

Finally, to apply this process to our corpus, we create a `WDController` associated to dump reader
using the `Reader` class

    wikidata_dump="/path/to/your/wikidata/dump"
    dump = Reader(wikidata_dump, 'utf-8')
    proc1=ExtractActorProcess(1)
    controller = WDController(dump, proc1)
    controller.process_all()


## TODO

  * Create a quantity object (store more information)
  * Better documentation for the different data types
    
