<h1 align="center">TOSDR Terms of Service Corpus</h1>

<p align="center">
  <a href="#usage">Usage</a> •
  <a href="#contributors">Contributors</a> •
  <a href="#license">License</a>
</p>

## Description

This repository contains a corpus of 10,000 terms of service (TOS) documents, which were scraped from the [TOSDR website](https://edit.tosdr.org/documents) using the Beautiful Soup and Requests libraries in Python. The dataset includes both HTML and text versions of the documents.

The data collection process involved retrieving the document text from TOSDR, saving it in an HTML file, removing non-English files detected through the LangDetect library, removing files less than 2KB in size, and converting the remaining files to a text format.

## Usage

This dataset can be used by legal, privacy, and natural language processing (NLP) researchers to study terms of service agreements and their implications for user privacy and rights. The dataset can be used to develop models and tools for analyzing terms of service agreements, identifying patterns and trends in the language used, and predicting the impact of certain clauses on users.

To use the dataset, simply download the files from this repository and import them into your preferred analysis tool or programming language.

## Contributors

This dataset was created by Sonu Gupta. Contributions to the dataset and repository are welcome and encouraged. To contribute, please fork this repository, make your changes, and submit a pull request.

## License

This dataset is released under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). By downloading and using this dataset, you agree to give attribution to the original source and to share any modifications under the same license.
