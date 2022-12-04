#!/usr/bin/env python3

from main import app
import os

if __name__ == "__main__":
  # Running on http://0.0.0.0:12345/ by default
  app.run(
    debug=False,
    port=os.getenv('PORT', "12345"),
    host=os.getenv('HOST', "0.0.0.0")
  )