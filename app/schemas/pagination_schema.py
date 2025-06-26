from marshmallow import Schema, fields


def PaginationSchemaFactory(item_schema, items_key='items'):
    fields_dict = {
        items_key: fields.Nested(item_schema(), many=True),
        'total': fields.Int(),
        'page': fields.Int(),
        'pages': fields.Int(),
        'per_page': fields.Int(),
        'has_next': fields.Bool(),
        'has_prev': fields.Bool()
    }

    return type(f'{item_schema.__name__}Pagination', (Schema,), fields_dict)()
