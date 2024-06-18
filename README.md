BART (Bidirectional and Auto-Regressive Transformers): is a denoising autoencoder for pre-training sequence-to-sequence models, combining bidirectional and autoregressive transformers. 
T5 (Text-To-Text Transfer Transformer): transforms all NLP tasks into a unified text-to-text format, where both input and output are consistent text strings. This model has proposed promising results on a variety of NLP benchmarks, demonstrating its generality and effectiveness.
GPT-2 (Generative Pretrained Transformer 2): is a large-scale, transformer-based language model that is trained to predict the next word in a sentence and excels at generating coherent and contextually relevant text.  
Pegasus (Pre-training with Extracted Gap-sentences for Abstractive Summarization): is specifically designed for abstractive text summarisation by pre-training on a gap-sentence generation target. 

Usage Of Summy

Settings page where the user can make choices regarding the use of the relevant summarization system. 
This page allows the user to select one or many sources, title selection and subtitle selection. 
As the title is selected, subheadings related to that title are dynamically retrieved from the database via AJAX and dynamically displayed according to the sub-title selection.
Essentially, this is the part where the system works and allows us to get the desired basic summarisation output for the summarisation process to take place. 
This section sets up the mechanism of the summarization. 
Depending on the selections made here, the process of receiving data and the length of messages from news sources will be adjusted.
For instance, if a long and detailed content is selected, it enables access more detailed and longer summaries of this content. 
On the contrary, a summary selection works by extracting data from fewer and fewer sources and making shorter summaries based on this extracted data. 
The news items selected according to the selections made are grouped together with their URLs according to the relevant title selection.  
After extracting the text of the relevant news from the extracted URLs, the news text is accessed by scraping. 
The accessed news texts are summarised using the Bart summarisation model according to the summary length request and the selection made on the summarisation page, and stored in the database. 
