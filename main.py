#!/usr/bin/env python3

import os
from flask import Flask, jsonify, render_template
from flask_caching import Cache
from util.metrics import *

# Flask-Caching related configs
config = {
    "CACHE_TYPE": "SimpleCache",  
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

@app.route('/', methods=['GET'])
def root():
  """
  A dummy route that returns {"Hello":"World"}
  """
  return jsonify({"Hello": "World"})


@app.route('/health', methods=['GET'])
def healthcheck():
  """
  A dummy route to check if the service is up or not!
  """
  return jsonify({"status": "OK"})


@app.route('/metrics', methods=['GET'])
@cache.cached(timeout=20) # Cache response for 20s 
def get_metrics():
  """ Retrieve metrics """
  metrics = get_app_metrics()
  return render_template('metrics.html.j2', metrics=metrics)
