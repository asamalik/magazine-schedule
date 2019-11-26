FROM fedora:31

COPY schedule.py /app/schedule.py

CMD /usr/bin/python3 /app/schedule.py