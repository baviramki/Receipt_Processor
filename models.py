from marshmallow import Schema, fields, validate


class Items(Schema):
	shortDescription = fields.Str(required = True)
	price = fields.Str(required = True, validate = validate.Regexp('^[0-9]*\.[0-9][0-9]$'))

class CreateReceiptSchema(Schema):
	retailer = fields.Str(required = True)
	purchaseDate = fields.Str(required = True, validate = validate.Regexp('^\\d{4}-\\d{2}-\\d{2}$'))
	purchaseTime = fields.Str(required = True, validate = validate.Regexp('^\\d{2}:\\d{2}$'))
	items = fields.List(fields.Nested(Items),required = True)
	total = fields.Str(required = True, validate = validate.Regexp('^[0-9]*\.[0-9][0-9]$'))

	










