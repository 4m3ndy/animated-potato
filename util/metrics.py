import os

def get_app_metrics() -> str:
  metrics = {}
  try:
    with open(os.getenv('METRICS_FILE_PATH', "./data/metrics_from_special_app.txt"), "r") as metrics_file:
      for metric_line in metrics_file.readlines():
        metric = metric_line.rstrip().split("=")
        metrics[str(metric[0])] = str(metric[1])
  except IOError as x:
      print("Couldn't Read metrics file, for more details: ", x )
  return metrics