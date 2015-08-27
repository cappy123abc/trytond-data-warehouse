from trytond.model import ModelView, ModelSQL, fields

# list of all classes in the file
__all__ = ['DateDimension', 'DateDimensionLine']


class DateDimension(ModelSQL, ModelView):
    'DateDimension'

    __name__ = 'dw.date'

    year = fields.Integer('Year')
    month = fields.Integer('Month')
    day_of_year = fields.Integer('Day of Year')
    day_of_month = fields.Integer('Day of Month')
    day_of_week = fields.Integer('Day of Week')
    week_of_year = fields.Integer('Week of Year')
    quarter = fields.Integer('Quarter')




