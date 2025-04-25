## CrimeDashboard

This repository is built to download and process data related to crime and create a dashboard. We are going to look at crime data from specific cities and see how crime relates to demographic information such as income, population density, household size and other factors. We plan on collecting some of this demographic information using zip codes and joining this to the datasets that we have already found. 

## How to use commands
Under the execution folder there is a file command.yml; This file is what will be used to determine what functions to execute based on the command input. You can see the name of the command and the functions it will execute with the parameters passed into each function. This will be described in more detail under the how to create commands sections.

To execute a specifc command just run the main file and type the name of the command
Example: To run the download_files function type 'python main.py download_files' into you terminal and hit enter

## How to create commands
There are a few core components that are needed to create a command.

# Name 
First is the name. This is what you will type in the terminal to call the command. It should be all lower case, have no spaces, and no special characters except for underscores '_'. It should not start with a number. Directly underneath the name you can include other entries like a description or message. Then the final entry should be functions and should be blank. The blank entry allows you to create lists of objects underneath of it with an indent and a '-' as seen in the existing commands.

# Functions
Wherever you see a '-' underneath functions is the start of a new function. You can then list anything needed for that function to execute. This includes the function name, module, and parameters to pass to the function. In python a module simply tells the program what directory to go to. For example there is a functions.py in the transformation folder. The module needed to access functions from that folder is 'transformation.functions'. Note that it doesn't include the file extension. The last command in the yml is an example that demonstrates this.

Here the file is passed into the function so what is actually executed is table_from_csv('example_file.csv')

And in order to call this you would type 'python main.py example_command'
          
# Using the api
This project uses dynaconf to store secrets. A settings.toml file can be used for public configuration settings, while a settings.local.toml can be used for secrets such as api keys. For readability, anything needed in settings.local.toml should have a blank entry in settings.toml.

## Team Members

Josh Morningstar
    - Joshua134512

Niraj Amgai
    - amgaio

Macy Schanbacher
    - Macy-Schanbacher
    
Kat Amundson
    - katamundson

## Folders

Execution: This can be used for creating sequences of functions to execute in order\
Extraction: This accesses data and writes to files\
Transformation: Will be used for cleaning and transforming data\
Data: Location where raw data will be written to when extracting (automatically created when downloading data, not kept in repository)\
Rawdata: Holds data files and metadata for our datasets\

## Dataset URLS

https://www.statsamerica.org/sip/rank_list.aspx?rank_label=pop1 
https://worldpopulationreview.com/state-rankings/quality-of-life-by-state 
https://www.datapandas.org/ranking/recidivism-rates-by-state#table 
https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/docApi 


