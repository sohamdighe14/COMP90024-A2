# COMP90024 - Assignment 2 - team 60
#
#  Junhong Liu         - Student ID: 1084997 - Melbourne
#  Justin Beaconsfield - Student ID: 761885  - Melbourne
#  Callum Dowling      - Student ID: 1009257 - Palmwoods
#  Soham Swapnil Dighe - Student ID: 1219439 - Melbourne
#  Samy Allouache      - Student ID: 1210426 - Melbourne

FROM python
COPY . /frontend
WORKDIR /frontend
RUN pip install -r /frontend/requirements.txt
CMD [ "python", "init.py"]