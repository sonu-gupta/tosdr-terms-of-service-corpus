<h1 align="center">TOSDR Terms of Service Corpus</h1>

<p align="center">
  <a href="#usage">Usage</a> •
  <a href="#contributors">Contributors</a> •
   <a href="#acknowledgment">Acknowledgment</a> •
  <a href="#license">License</a>
</p>

## Description

This repository contains a corpus of 12,215 terms of service (TOS) documents, which were scraped from the [TOSDR website](https://edit.tosdr.org/documents) using the Beautiful Soup and Requests libraries in Python. The dataset includes both HTML and text versions of the documents.

The data collection process involved retrieving the document text from TOSDR, saving it in an HTML file, removing non-English files detected through the LangDetect library, removing files less than 2B in size and less than 6 words, and converting the remaining files to a text format.

## Usage

This corpus can be used by legal, privacy, and natural language processing (NLP) researchers to study terms of service agreements and their implications for user privacy and rights. It can be used to develop models and tools for analyzing terms of service agreements, identifying patterns and trends in the language used, and predicting the impact of certain clauses on users.

To use the dataset, simply download the files from this repository and import them into your preferred analysis tool or programming language.

## Contributors

This corpus was created by Sonu Gupta. Contributions to the corpus and repository are welcome and encouraged. To contribute, please fork this repository, make your changes, and submit a pull request.

## Acknowledgment

I would like to acknowledge the TOSDR team for their good work and the valuable resource they have created in the form of the TOSDR website. Their efforts in creating a platform that summarizes and rates the terms of service of various online services has been invaluable in raising awareness about online privacy and user rights.

## License

This corpus is based on data from the Terms of Service; Didn't Read (TOS; DR) project, licensed under the GNU Affero General Public License version 3 (AGPLv3). As such, this work is also licensed under GNU AGPLv3. For more information about the GPLv3 license, please visit https://www.gnu.org/licenses/licenses.html#AGPL.

## Things in Progress
I am continuously updating and improving this corpus. Currently, I am working on removing the non-TOS documents from the corpus. I am also exploring the use of machine learning and natural language processing techniques to further analyze and extract insights from this corpus. 

I am working on a new corpus that would contain TOS documents that are not included in this corpus.

If you are interested in contributing to this project, please feel free to submit a pull request or reach out to us directly. I welcome any and all contributions and feedback.
