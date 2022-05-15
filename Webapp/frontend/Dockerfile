FROM python
COPY . /script
WORKDIR /script
RUN pip install -r /script/requirements.txt
#ARG node_number
#CMD [ "python", "tweet_Harvester.py", "-n", "echo $node_number"]
CMD [ "python", "init.py"]