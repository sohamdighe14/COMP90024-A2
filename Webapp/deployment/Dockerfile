FROM python
RUN mkdir webapp
COPY . ./webapp
RUN pip install -r ./webapp/requirements.txt
WORKDIR ./webapp/ 
#ARG node_number
#CMD [ "python", "tweet_Harvester.py", "-n", "echo $node_number"]
CMD [ "python", "init.py"]