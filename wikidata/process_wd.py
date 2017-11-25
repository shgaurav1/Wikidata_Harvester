# coding=utf-8
import sys

class Process(object):
    """
    Procces class
    """
    def __init__(self,id):
        self.id=id

    def processItem(self,entry):
        """
        The method that will contains the process applied to items.
        :param entry: item data
        :return: 
        """
        pass
    def processProperty(self,entry):
        """
        The method that will contains the process applied to properties.
        :param entry: property data
        :return: 
        """
        pass

class WDController(object):
    """
    
    """
    def __init__(self,reader,*args):
        """
        Constructor
        :param reader: wikidata dump reader (see Reader class)
        :param args: contains all the process you want to apply during the dump reading
        """
        self.reader=reader
        self.process={}
        for arg in args:
            if isinstance(arg,Process):
                self.process[arg.id]=arg

    def process_all(self,v=True):
        """
        Read the dump and apply each process to each entry
        :param v: verbose
        :return: 
        """
        iterations = 0
        while self.reader.has_next():
            entry=self.reader.next()
            if entry:
                for id_,proc in self.process.items():
                    if entry["id"][0] == "Q":
                        proc.processItem(entry)
                    else:
                        proc.processProperty(entry)
            iterations+=1
            if iterations%100 == 0 and v:
            	sys.stdout.write("\rEntity Parsed: "+'{:,}'.format(iterations))
