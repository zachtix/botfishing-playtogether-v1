# How to call Function
# from printts import tsprint
# tsprint("test time stamp")

import pytz
from datetime import datetime

def tsprint(pmessage):
    tz_TH = pytz.timezone('Asia/Bangkok')
    datetime_TH = datetime.now(tz_TH)
    CTime = datetime_TH.strftime("[%d-%m-%Y|%H:%M:%S]")
    print(CTime, pmessage)