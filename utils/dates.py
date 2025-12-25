from dateutil import parser


def parse_date(date_str):
    """
    Convert various date formats into datetime object
    """
    return parser.parse(date_str)
