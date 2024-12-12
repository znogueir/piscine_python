from time import time, gmtime, strftime

current_time = time()
date = f"Seconds since January 1, 1970: {current_time:,.4f}"
sci = f"or {current_time:.2e} in scientific notation"

print(date, sci)
print(strftime("%b %d %Y", gmtime()))
