from colander import (
    Boolean,
    Integer,
    Length,
    MappingSchema,
    OneOf,
    SchemaNode,
    SequenceSchema,
    String
)

from deform import widget

colors = (('red', 'Red'), ('green', 'Green'), ('blue', 'Blue'))


class DateSchema(MappingSchema):
    month = SchemaNode(Integer())
    year = SchemaNode(Integer())
    day = SchemaNode(Integer())


class DatesSchema(SequenceSchema):
    date = DateSchema()


class MySchema(MappingSchema):
    name = SchemaNode(String(),
                      description='The name of this thing')
    title = SchemaNode(String(),
                       widget=widget.TextInputWidget(size=40),
                       validator=Length(max=20),
                       description='A very short title')
    password = SchemaNode(String(),
                          widget=widget.CheckedPasswordWidget(),
                          validator=Length(min=5))
    is_cool = SchemaNode(Boolean(),
                         default=True)
    dates = DatesSchema()
    color = SchemaNode(String(),
                       widget=widget.RadioChoiceWidget(values=colors),
                       validator=OneOf(('red', 'blue')))
