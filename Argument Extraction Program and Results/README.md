# IssueArgumentation

## List of files
### Before running the experiments (\*\_Pipeline_nestCV.ipynb), these following files need to run in the listed order to build feature sets

:page_facing_up: GetAssociation,ipynb - get author Association for the comment, needs to be ran before GetMetadata. 
<br/>:pencil: AuthorAssociation_data.csv

:page_facing_up: GetConversationalData.ipynb - get all other conversational data, need to run the one above first. 
<br/>:pencil: Conversational_data.csv

:page_facing_up: GetPOS.ipynb - get POS tag using Stanford CoreVLP. **Note:** in order to run this file, you need to follow the instructions at https://stanfordnlp.github.io/CoreNLP/corenlp-server.html (set up CoreNLP server to use the dependency parser). 
<br/>:pencil: Conversational_Pos_data.csv

:page_facing_up: GetPolitenessScore.ipynb - Get politeness score. **Note:** in order to run this file, you need to follow instructions at https://libraries.io/pypi/politeness (install politeness package) and https://stanfordnlp.github.io/CoreNLP/corenlp-server.html (set up CoreNLP server to use the dependency parser). 
<br/>:pencil: Conversational_Pos_Politeness_data.csv	

:wrench: LIWC tool - LIWC2015 tool to get LIWC features. 
<br/>:pencil: Conversational_Pos_Politeness_LIWC_data.csv

:page_facing_up: Preprocess.ipynb - rename column, output preprocess.csv for training and predicting.
<br/>:pencil: Preprocessed.csv

### Then the training and predicting can be performed using the following files

:page_facing_up: Argumentative_Pipeline_nestCV.ipynb - perform training and classification for task 1 (argumentative vs. non-argumentative). 
<br/>:pencil: results_argumentative/*

:page_facing_up: ArgumentPart_Pipeline_nestCV.ipynb - perform training and classification for task 2 (claim, warrant, and ground). 
<br/>:pencil: results_argu_part/*

:page_facing_up: Standpoint_Pipeline_nestCV.ipynb - perform training and classification for task 3 (support vs. against).
<br/>:pencil: results_standpoint/*

### For statistics in paper

:page_facing_up: CorpusStatistics.ipynb - get corpus statistics for paper

:page_facing_up: GetOpened.ipynb - get number of issues opened weekly.

:page_facing_up: DiscussionTrend.ipynb - get number of quotes for each argument ID (to draw the discussion trend graph)

:page_facing_up: ImportantToken.ipynb - get TFIDF weights for each of argumentative, non-argumentative, claim, warrant, ground, support and against to draw the top 20 TFIDF tokens for each category

### Others

:page_facing_up: FilterDFTool.py - little wrapper to filter by row and column 

:page_facing_up: DenseTfidfVectorizer.py - return in dataframe

:page_facing_up: ToulminArgumentationModel.csv - annotations exported from Atlas

:page_facing_up: TimeAuthor.xlsx - time and author information.
