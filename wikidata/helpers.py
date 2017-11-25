# -*- coding: utf-8 -*-

def extract_label(entry, lang):
    """
    Extract the label associated to an entry in a specific language
    :param entry: 
    :param lang: 
    :return: 
    """
    if "labels" in entry:
        if lang in entry['labels'].keys():
            return entry['labels'][lang]
    return None


def extract_wiki_link(entry, lang):
    """
    Extract the associated wikipedia link to an entry in a specific language
    :param entry: entry data
    :param lang: lang of wikipedia link, you want to extract
    :return: 
    """
    if "sitelinks" in entry:
        siteLinks = entry['sitelinks']
        key = '{0}wiki'.format(lang)
        if key in siteLinks:
            return siteLinks[key]["url"]
    return None


def extract_all_wiki_links(entry):
    """
    Extract all wikipedia links associated to an entry
    :param entry: entry data
    :return: 
    """
    if "sitelinks" in entry:
        return entry['sitelinks']

