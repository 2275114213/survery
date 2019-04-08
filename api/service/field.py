
from rest_framework import fields

class CustomCharField(fields.Field):

    '''
    针对prefix
    应用场景: 比如图片地址很多个,降低单台服务器的压力,前面可以自定义传
    def __init__(self,prefix,*args,**kwargs):
        self.prefix = prefix
        super(CustomCharField,self).__init__(*args,**kwargs)
    def to_representation(self, value):

        return f"{self.prefix}第{value.semester}期"
    '''
    def to_internal_value(self, data):
        return data


    # 这里面的value 是by_class  相关联的外键字段 的实例对象
    def to_representation(self, value):
        # 如此format  甚是简单
        return f"{value.course}第{value.semester}期"
    '''
    >>> value
    <ClassList: ClassList object (1)>
    '''


# 如果图片的域名变了,就直接在这改就可以
class ImgCharField(fields.Field):
    def to_internal_value(self, data):
        return data


    # 这里面的value 是by_class  相关联的外键字段 的实例对象
    def to_representation(self, value):
        # 如此format  甚是简单
        return f"{'http://www.cdjh'}"