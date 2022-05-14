FROM python
RUN mkdir webapp

COPY . /webapp
WORKDIR /webapp 
RUN pip install -r requirements.txt

#ARG node_number
#CMD [ "python", "tweet_Harvester.py", "-n", "echo $node_number"]
CMD [ "python", "init.py"]