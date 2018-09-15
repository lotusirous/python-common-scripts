- [Convert datetime to string](#convert-datetime-to-string)

### Convert datetime to string

```py
import datetime


def time2str(format):
    # datetime to string
    format = format or "%Y-%m-%d %H:%M:%S" # set default format
    return datetime.datetime.now().strftime(format)

```