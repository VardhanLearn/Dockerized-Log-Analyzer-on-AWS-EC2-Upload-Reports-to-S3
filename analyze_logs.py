import boto3
from collections import Counter

LOG_FILE = "sample.log"
OUTPUT_FILE = "log_summary.txt"
BUCKET_NAME = "your-s3-bucket-name"

counter = Counter()

with open(LOG_FILE, "r") as f:
    for line in f:
        if "ERROR" in line:
            counter["ERROR"] += 1
        elif "WARNING" in line:
            counter["WARNING"] += 1
        elif "INFO" in line:
            counter["INFO"] += 1

with open(OUTPUT_FILE, "w") as f:
    for level, count in counter.items():
        f.write(f"{level}: {count}\n")

s3 = boto3.client("s3")
s3.upload_file(OUTPUT_FILE, BUCKET_NAME, OUTPUT_FILE)

print("Log analysis complete. File uploaded to S3.")

