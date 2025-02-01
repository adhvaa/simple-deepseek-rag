# simple-deepseek-rag
Simple "getting started" python script to build a simple RAG with deepseekR1:7b and ollama. 

## Description
This Python script utilizes AI models and document processing techniques to provide answers based on specific documents. It uses the OllamaEmbeddings library for embedding generation and retrieval, and it processes text files to extract information relevant to user queries.

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/adhvaa/simple-deepseek-rag.git
    cd your-repo
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Ensure you have Python installed on your machine.
2. Run the script using:
    ```bash
    python main.py
    ```
3. Follow the prompts or input queries as directed in the script.

## Dependencies
- langchain_community
- langchain_ollama
- langchain
- tiktoken
- sklearn
- numpy

## Input: 
File: diet_plan1.txt
Question: can you suggest a new vegetarian dish for dinner basaed on diet plan?

## Output:
Answer: <think>
Okay, so I need to suggest a new vegetarian dish for dinner based on the given diet plan.....~.....So I think steamed broccoli would be a suitable vegetarian dinner choice that supports the overall recovery plan.
</think>

Steamed Broccoli is an excellent vegetarian option for dinner, offering high vitamin C and calcium content to support bone health during recovery.


## License
[MIT](https://choosealicense.com/licenses/mit/)
