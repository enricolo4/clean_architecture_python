user = {
    '$schema': 'http://json-schema.org/schema#',
    'type': 'object',
    'properties': {
        'name': {'$ref': '#/definitions/non-empty-string'},
        'surname': {'$ref': '#/definitions/non-empty-string'},
        'birthday': {'$ref': '#/definitions/date-string-pattern'},
        'age': {'$ref': '#/definitions/non-negative-number'},
        'cpf': {'$ref': '#/definitions/cpf-string-pattern'},
        'email': {'$red': '#/definitions/email-string-pattern'},
        'cellphone': {}
    },
    'definitions': {
        'cpf-string-pattern': {
            'type': 'string',
            'pattern': '[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}'
        },
        'date-string-pattern': {
            'type': 'string',
            'pattern': '^([0-2][0-9]|(3)[0-1])(/)(((0)[0-9])|((1)[0-2]))(/)\d{4}$'
        },
        'email-string-pattern': {
            'type': 'string',
            'pattern': '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
        },
        'non-empty-string': {
            'type': 'string',
            'minLength': 1
        },
        'non-negative-number': {
            'type': 'integer',
            'minimum': 0,
        }

    },
    'required': ['name', 'surname', 'birthday', 'age', 'cpf', 'email', 'cellphone']
}
