###########################################
# Message Generator for Fast Langugage    #
###########################################
# Coding By José Alexsandro               #
# Github: https://github.com/jsalexsandro #
###########################################


from variables import langName,langVersion
from datetime import datetime

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

generated_code_for_insert = f"""/*
 * [file]
 * Code Generated by {langName} lang
 * Version language: ({langVersion})
 * {days[datetime.weekday(datetime.now())]} {datetime.now()}
*/\n\n"""