def fromdicttolist(dict, keys):
    dictTOlist = []
    for e in dict:
        element = []
        for key in keys:
            if key in e: 
                element.append(e[key])
        dictTOlist.append(element)
    return dictTOlist