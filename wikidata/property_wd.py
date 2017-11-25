# coding=utf-8

class Property(object):
    """
    Property class
    """
    def __init__(self, id,isMultiple,type_):
        """
        Constructor
        :param id: id of the property
        :param isMultiple: if the property can be associated to multiple values
        :param type_: type of the value associated
        """
        self.id=id
        self.isMultiple=isMultiple
        self.type=type_

    def exists(self,data):
        """
        Method that verify if the property exist in an entry
        :param data: 
        :return: 
        """
        if 'claims' in data:
            if self.id in data["claims"] and self.type.check_conformity(self.id,data):
                return True
        return False

    def extractData(self,data):
        """
        Return the data associated to the property in an entry
        :param data: entry data
        :return: data associated to the property
        """
        return self.type.extractData(self.id,self.isMultiple,data)
