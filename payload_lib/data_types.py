Int32 = 'int32'
String = 'string'
Float = 'float'
Binary = 'binary'
Int8 = 'int8'

_map = {
    1 : Int32,
    4 : String,
    5 : Float,
    6 : Binary,
    8 : Int8
}

def get_data_type(v):
    return _map[v]