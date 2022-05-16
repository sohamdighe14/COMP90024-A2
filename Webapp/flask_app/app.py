import plotly
from flask import Flask, render_template, send_file, request, url_for, redirect
from matplotlib import pyplot as plt
from io import BytesIO
import plotly.express as px
import json
import plotly.graph_objects as go
from scenario1 import city_tweets, income_sentiment, generate_pie_chart, generate_word_cloud_hashtags
from scenario2 import generate_word_cloud, generate_scores, city_comparison, covid_save_data
from scenario3 import subjectivity_unemployment,education_unemployment,unemployment_polarity,generate_wordcloud_work_education, emp_save_data
from plotly.subplots import make_subplots
from fetch_data import save_data,refresh_map_pt,convert_geojson

app = Flask(__name__)