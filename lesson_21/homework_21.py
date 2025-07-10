import datetime
import logging

with open("hblog.txt", "r") as file:
    lines = file.readlines()

filtered_lines = [line for line in lines if "Key TSTFEED0300|7E3E|0400" in line]

timestamps = []

for line in filtered_lines:
    if "Timestamp" in line:
        time_str = line.split("Timestamp")[1].strip().split()[0]
        try:
            time_obj = datetime.datetime.strptime(time_str, "%H:%M:%S")
            timestamps.append((time_obj, time_str, line.strip()))
        except ValueError:
            continue

with open("hb_test.log", "w") as log_file:
    for i in range(1, len(timestamps)):
        t1, ts1, line1 = timestamps[i - 1]
        t2, ts2, line2 = timestamps[i]

        delta = (t1 - t2).total_seconds()

        if 31 < delta < 33:
            log_file.write(f"WARNING! Delta time: {delta}\nTime: {ts2}\nFull info: {line2}\n\n")
        elif delta >= 33:
            log_file.write(f"ERROR! Delta time: {delta}\nTime: {ts2}\nFull info: {line2}\n\n")