from . import licenses


def format_text(license_text, info):
    """
    Takes license template body and returns the text after filling in name and year
    :return: Formatted license text
    """
    final_text = license_text.format(year=info['year'],
                                     copyright_holders=','.join(info['people']))
    return final_text
