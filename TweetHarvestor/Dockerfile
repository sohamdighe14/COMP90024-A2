FROM python
RUN mkdir harvest
COPY . ./harvest
RUN pip install -r ./Harvestor/requirements.txt
WORKDIR ./harvest/ 
CMD [ "python", "tweet_Harvester.py"]