# coding=utf-8
from gzip import GzipFile
import json
class Reader(object):
    """Reader class"""
    def __init__(self, wikidata_dump_fn, decoding="utf-8"):
        """
        
        :param wikidata_dump_fn: wikidata dump filename
        :param decoding: encoding used
        """
        self.wikidata_dump_fn = wikidata_dump_fn
        self.decoding = decoding
        self.dump = GzipFile(wikidata_dump_fn,'r')
        self.line = self.dump.readline()

    def has_next(self):
        """
        Check if there is still entries to be read
        :return: true if other entries available
        """
        self.line = self.dump.readline().decode(self.decoding)
        if self.line is '': return False
        else:return True

    def next(self):
        """
        Return the next entry
        :return: next entry
        """
        try:
            return json.loads(self.line.strip('\n,'))
        except json.decoder.JSONDecodeError as e:
            return None
