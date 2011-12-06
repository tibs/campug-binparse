class Field(object):
    order = {}
    names = {}
    def __init__(self):
        Field.order[self] = len(Field.order)

class UInt32(Field):
    pass

class UInt8(Field):
    pass

class MetaStructure(type):
    def __new__(metaclass, klass, bases, attributes, *args, **kwargs):
        print 'm.__new__'
        print 'metaclass ', metaclass
        print 'class     ', klass
        print 'bases     ', bases
        print 'attributes', attributes
        print 'args     ', args
        print 'kwargs   ',kwargs
        for k in attributes:
            Field.names[attributes[k]] = k
        return type(klass, bases, attributes)
    def __init__(self, *args, **kwargs):
        print 'm.__init__', args, kwargs

class Structure(object):
    __metaclass__ = MetaStructure

    def __init__(self, *args, **kwargs):
        print '__init__', args, kwargs

class Spam(Structure):
    file_length = UInt32()
    x = UInt8()
    y = UInt8()

spam = Spam(3, spam='beans')
print 'Field.order', Field.order
print 'Field.names', Field.names

# How to specify arrays?
#    array_no1 = Array(UInt32, 4)  # simple and explicit
#    array_no2 = [UInt32() for _ in range(4)]  # hard to make it do what we want
#    array_no3 = Uint32[4]()       # Tom's suggestion
#    array_no4 = Uint32()*4        # compare with numpy
#    array_no5 = Uint32(repeat=4)
#    name = NullTerminatedString()
#    str_len = SByte()
#    manifest = CountedString(size=str_len)
# vim: set tabstop=8 softtabstop=4 shiftwidth=4 expandtab:

