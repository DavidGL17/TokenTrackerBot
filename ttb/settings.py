import yaml

# Settings

with open("settings.yaml", "r") as f:
    config = yaml.safe_load(f)

client_id = config["client_id"]
client_secret = config["client_secret"]
region = config["region"]
log_file = config["log_file"]
