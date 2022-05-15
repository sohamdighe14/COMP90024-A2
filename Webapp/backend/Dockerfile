# COMP90024 - Assignment 2 - team 60
#
#  Junhong Liu         - Student ID: 1084997 - Melbourne
#  Justin Beaconsfield - Student ID: 761885  - Melbourne
#  Callum Dowling      - Student ID: 1009257 - Palmwoods
#  Soham Swapnil Dighe - Student ID: 1219439 - Melbourne
#  Samy Allouache      - Student ID: 1210426 - Melbourne

FROM nginx
ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV http_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV no_proxy localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.o>
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf