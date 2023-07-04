def apply(data, fn):

    if isinstance(data, list):

        return [apply(_data, fn) for _data in data]
    
    if isinstance(data, tuple):

        return tuple([apply(_data, fn) for _data in data])
    
    if isinstance(data, dict):

        return {key: apply(value, fn) for key, value in data.items()}
    
    return fn(data)