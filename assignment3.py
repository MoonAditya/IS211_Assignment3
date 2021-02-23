import urllib.request
import csv
import argparse
import re
import logging


downloadUrl = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
def downloadData(url=downloadUrl):
    g = urllib.request.urlopen(url)
    name = g.url[url.rfind('/') + 1:]
    with open(name, 'wb') as f:
       return f.write(g.read())

def processData(file='weblog.csv'):
    with open(file) as csvFile:
        reader = csv.reader(csvFile, delimiter= ",")
        imgCount = 0
        total_rows = 0
        for eachRow in reader:
            fileName = eachRow[0]
            if(re.search("(.(?i)(jpe?g|png|gif|bmp))$", fileName,)):
                imgCount+=1
            
            dateTime = eachRow[1]
            browserInfo = eachRow[2]

            status = eachRow[3]
            fileSize = eachRow[4]
            total_rows+=1 
        print("Total image hit found".format(imgCount))
        image_hit_percentage = round((imgCount / total_rows) * 100)
        print("Image requests account for {}% of all requests".format(image_hit_percentage))

def main(url):
     print(f"Running main with URL = {url}...")
     parseUrl = downloadData()
     processData(parseUrl)

if __name__ == "__main__":
     """Main entry point"""
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="URL to the datafile", type=str, required=False)
args = parser.parse_args()
logger = logging.getLogger("Assignment3 ")
logging.basicConfig(filename='errors.log', level=logging.ERROR)
main(args.url)