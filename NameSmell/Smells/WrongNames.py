

def wrong_names(input):
    return any([True if w.lower().startswith('get') or  w.lower().startswith('set') else False  for w in input ])