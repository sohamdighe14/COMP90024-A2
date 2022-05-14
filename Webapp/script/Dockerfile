FROM python
RUN mkdir webapp \
&& cp . /webapp \
&& pip install -r ./webapp/requirements.txt

#ARG node_number
#CMD [ "python", "tweet_Harvester.py", "-n", "echo $node_number"]
CMD [ "python", "init.py"]