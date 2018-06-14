# reactome_qa
# Aim
Generate a filt for visualizing of Reactome quality control measures.
# Background
Reactome (https://reactome.org or http://reactome.ncpsb.org) has developed a range of quality control measures. After each release, a set of scripts are run on the Reactome graph database to detect data problems or inconsistencies. These are then analysed and passed to curators and developers for correction, either immediately for critical errors, or over time for non-critical errors. The summary of the QA script results is provided in a QA summary file, one file per release.
The Reactome Scientific Advisory Board has requested information on the QA progress over time. We are also considering a publication describing the Reactome QA process. As one component in this, we’d like to summarise and visualise statistics on the Reactome QA process over multiple releases.
# Detailed Background
The release process in Reactome starts by taking a "slice database" from gk_central (curation database). The slice database contains exclusively curated data meant to be released (which is distinguished from the rest by using a boolean flag named "_toRelease". 
Using the content of the "slice database" as t he input for the graph-importer, a Neo4j graph database is created so the diagram-qa and the graph-qa projects can be run to assess the quality of the data. Once both types of QA are executed, a set of reports plus summary files are generated to help Reactome editorial and curators to address the different type of issues. 
After the QA tests are applied, the release process starts and the database is enrich with cross-references and orthologies to other species among other data. When the process finishes, the resulting database is used once more to generate more QA reports. In this case, the results of the tests will include curated data plus data added computationally. It means that it will detect problems in the content that have been introduced by different pieces of software executed during the release process. It is important to say that a greater number of inconsistencies are expected for this second set of results, although the aim for the mid-long term is for both sets to reach zero items reported.
# Minimum requirements
It should be possible to run the script on almost any computers where python 3 is installed. it also needs python dependencies,

**pandas**, [installation documentation](https://pandas.pydata.org/pandas-docs/stable/install.html), if you have pip installed, please run pip3 install pandas\
**re**, regular expression operation modules is bundled in the Python installation\
**glob**, glob is a standard module\
**functools**,

# Usage
Download the zip folder to your local,unzip the folder

reactome_qa is a directory to store all files, file structure as below:

* reactome_qa
  * report
    * input_01.csv
    * inpot_02.csv
    * ...
  * results
    * output.csv
  * reactome_qa.py

**report**-replace with your QA summary report files\
**results**- the output file will be stored in this folder\
**python script**- please change the path to your own

```python
file_path = "/your path to /reactome_qa/files/*.csv"
root = "/your path to /reactome_qa"
```


# Test

Run the script with provided QA files and visulize the outcome.csv file through Excel, You will get a similar chart as below,

![alt text](https://github.com/Chuqiaoo/reactome_qa/blob/master/reactome-qa.png)


# Contributors
Backgroud and Detailed Background are edited by Henning Hermjakob.
  
  





