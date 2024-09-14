# SampleSet

The SampleSetAssginemnt1.ipynb contains the solution for the problem statement:
Develop a Retrieval-Augmented Generation (RAG) model for a Question Answering (QA) bot for a business. Use a vector database like Pinecone DB and a generative model like Cohere API (or any other available alternative). The QA bot should be able to retrieve relevant information from a dataset and generate coherent answers.

To run this file u will need to install few packages before running the code
the packages required are:
  pinecone-client
  cohere
  transformers
  torch
  sentence_transformers

command used to download these packages in colab notebook:
!pip install pinecone-client cohere transformers torch sentence_transformers

You will be required to aquire the API key of pinecone and cohere for this project and replace it in the fields in the given file

After this setup u will be able to run the file and see the results of the chatbot with sample documentation and questions asked

####################################################################################################

The SampleSetAssignment2 contains the solution for the problem statement:
Develop an interactive interface for the QA bot from Part 1, allowing users to input queries and retrieve answers in real time. The interface should enable users to upload documents and ask questions based on the content of the uploaded document.

To run this file the requirements are:
1. You will need a code editor and then open the folder in the code editor
2. make sure you use python 3.12.5 version to run this code without any erroes or u will have to change the version of the python and its dependencies in the requirement file to the python version u are using
3. start your dockers desktop version
4. open the terminal in your code editor and follow the commands
    1. docker build -t my-python-app 
    2. docker run -p 8501:8501 my-python-app
5. Now your Stremlit app will be up and running using docker
6. Open a web browser and navigate to http://localhost:8501. You should see your Streamlit application running.



