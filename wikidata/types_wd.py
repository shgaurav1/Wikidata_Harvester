# coding=utf-8
from urllib.parse import urlparse
from dateutil.parser import parse


def parseDate(date):
    """
    Parse Wikidata date
    :param date: wikidata formated date
    :return: 
    """
    AD_BC_identifier = date[0]
    date.lstrip('+-')
    return AD_BC_identifier, parse(date, fuzzy=True)


class Type(object):
    """
    Class for managing data type in value
    """

    def __init__(self, typeName):
        """
        Constructor
        :param typeName: type name
        """
        self.type_name = typeName

    def extractData(self, propId, isMultiple, data):
        """
        
        :param propId: property id of the data to extract
        :param isMultiple: if single or multiple values
        :param data: entry data
        :return: 
        """
        if isMultiple:
            return self.extract_multiple(propId, data)
        return self.extract_single(propId, data)

    def extract_multiple(self, propID, data):
        """
        Methods use to extract data that contains multiple values associated to a property
        :param propID: property id
        :param data: entry data
        :return: data
        """
        return []

    def extract_single(self, propID, data):
        """
        Methods use to extract data that contains single values associated to a property
        :param propID: property id
        :param data: entry data
        :return: data
        """
        return []

    def check_conformity(self, propID, data):
        """
        Check if the data are in a good format
        :param propID: 
        :param data: 
        :return: 
        """
        return True


class EntityID(Type):
    """
    EntityID class
    """
    def __init__(self):
        """
        Constructor
        """
        super(EntityID, Type.__init__(self, "EntityID"))

    def extract_multiple(self, propID, data):
        result = []
        for i in range(len(data['claims'][propID])):
            result.append(data['claims'][propID][i]['mainsnak']['datavalue']['value']['id'])
        return result

    def extract_single(self, propID, data):
        return data['claims'][propID][0]['mainsnak']['datavalue']['value']['id']

    def check_conformity(self, propID, data):
        try:
            data['claims'][propID][0]['mainsnak']['datavalue']['value']['id']
            return True
        except Exception as e:
            return False


class String(Type):
    """
    String Type
    """
    def __init__(self):
        """
        Constructor
        """
        super(String, Type.__init__(self, "String"))

    def extract_multiple(self, propID, data):
        result = []
        for i in range(len(data['claims'][propID])):
            result.append(data['claims'][propID][i]['mainsnak']['datavalue']['value'])
        return result

    def extract_single(self, propID, data):
        return data['claims'][propID][0]['mainsnak']['datavalue']['value']

    def check_conformity(self, propID, data):
        try:
            data['claims'][propID][0]['mainsnak']['datavalue']['value']
            return True
        except Exception as e:
            return False


class Coordinates(Type):
    """
    Coordinates type
    """
    def __init__(self):
        """
        Constructor
        """
        super(Coordinates, Type.__init__(self, "Coordinates"))

    def extract_multiple(self, propID, data):
        result = []
        for i in range(len(data['claims'][propID])):
            result.append(self.parse_coord(data['claims'][propID][i]['mainsnak']['datavalue']['value']))
        return result

    def extract_single(self, propID, data):
        return self.parse_coord(data['claims'][propID][0]['mainsnak']['datavalue']['value'])

    def parse_coord(self, data):
        return {"lat": data["latitude"], "lon": data["longitude"]}

    def check_conformity(self, propID, data):
        try:
            self.parse_coord(data['claims'][propID][0]['mainsnak']['datavalue']['value'])
            return True
        except Exception as e:
            return False


class URL(Type):
    """
    Url type
    """
    def __init__(self):
        """
        Constructor
        """
        super(URL, Type.__init__(self, "URL"))

    def extract_multiple(self, propID, data):
        result = []
        for i in range(len(data['claims'][propID])):
            result.append(urlparse(data['claims'][propID][i]['mainsnak']['datavalue']['value']))
        return result

    def extract_single(self, propID, data):
        return urlparse(data['claims'][propID][0]['mainsnak']['datavalue']['value'])

    def check_conformity(self, propID, data):
        try:
            urlparse(data['claims'][propID][0]['mainsnak']['datavalue']['value'])
            return True
        except Exception as e:
            return False



class Time(Type):
    """
    Time Type
    """
    def __init__(self):
        """
        Constructor
        """
        super(Time, Type.__init__(self, "Time"))

    def extract_multiple(self, propID, data):
        result = []
        for i in range(len(data['claims'][propID])):
            result.append(parsedate(data['claims'][propID][i]['mainsnak']['datavalue']['value']))
        return result

    def extract_single(self, propID, data):
        return parsedate(data['claims'][propID][0]['mainsnak']['datavalue']['value'])

    def check_conformity(self, propID, data):
        try:
            parsedate(data['claims'][propID][0]['mainsnak']['datavalue']['value'])
            return True
        except Exception as e:
            return False


class Quantity(Type):
    """
    Quantity type
    """
    def __init__(self):
        """
        Constructor
        """
        super(Quantity, Type.__init__(self, "int"))

    def extract_multiple(self, propID, data):
        result = []
        for i in range(len(data['claims'][propID])):
            result.append(int(data['claims'][propID][i]['mainsnak']['datavalue']['value']))
        return result

    def extract_single(self, propID, data):
        return int(data['claims'][propID][0]['mainsnak']['datavalue']['value'])

    def check_conformity(self, propID, data):
        try:
            int(data['claims'][propID][0]['mainsnak']['datavalue']['value'])
            return True
        except Exception as e:
            return False


class ExternalIdentifier(Type):
    """
    External Identifier type
    """
    def __init__(self):
        """
        Constructor
        """
        super(ExternalIdentifier, Type.__init__(self, "ExternalIdentifier"))

    def extract_multiple(self, propID, data):
        result = []
        for i in range(len(data['claims'][propID])):
            result.append(data['claims'][propID][i]['mainsnak']['datavalue']['value'])
        return result

    def extract_single(self, propID, data):
        return data['claims'][propID][0]['mainsnak']['datavalue']['value']

    def check_conformity(self, propID, data):
        try:
            data['claims'][propID][0]['mainsnak']['datavalue']['value']
            return True
        except Exception as e:
            return False
