def load_data(file):
    pattern_raw = open(file, "r").readlines()
    input_data = pattern_raw[0].rstrip('\n')
    pattern = pattern_raw[1].rstrip('\n')
    
    return [input_data, pattern]