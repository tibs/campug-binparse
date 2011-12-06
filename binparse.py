import pprint

class Field(object):
    fields = []
    order = {}
    names = {}
    def __init__(self):
        Field.order[self] = len(Field.order)
        Field.fields.append(self)

    def __repr__(self):
        return '<{0} {1}>'.format(Field.names[self],
                                           self.__class__.__name__)

class UInt32(Field):
    pass

class UInt8(Field):
    pass

class MetaStructure(type):

    def __new__(metaclass, class_name, bases, attributes):
        for k in attributes:
            Field.names[attributes[k]] = k
            print
            print 'add %s:%s'%(k, attributes[k])
            pprint.pprint(Field.names)
        return type.__new__(metaclass, class_name, bases, attributes)

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
print
print 'Field.fields', Field.fields
print 'Field.order'
pprint.pprint(Field.order)
print 'Field.names'
pprint.pprint(Field.names)



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

