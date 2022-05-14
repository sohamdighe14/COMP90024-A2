FROM python

COPY . /deployment
WORKDIR /deployment
RUN pip install -r /deployment/requirements.txt
 
#ARG node_number
#CMD [ "python", "tweet_Harvester.py", "-n", "echo $node_number"]
CMD [ "python", "init.py"]