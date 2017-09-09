# Topic-Mining
Topic Mining on BigFoot sighting reports. Unsupervised learning on the most relevant events and topics related to Bigfoot sighting reports. Bigfoot sightings have been reported since last 40 years and many of the reports shared some similar descriptions and location information. What is the most relevant events to those sightings?

## Data
The Bigfoot sighting reports was collected from the [Geographic Database of Bigfoot / Sasquatch Sightings & Reports](http://www.bfro.net/gdb/). There are 4800+ sighting reports from 1960 to 2010 stored in this site. The raw dataset are html pages in a single json file. The reports information are parsed using BeautifulSoup library in python.

## Approach
Implemented tf-idf and non-negative matrix factorization on Bigfoot sighting reports to extract the most relevant latent features and consistent pattern from the sighting descriptions.
