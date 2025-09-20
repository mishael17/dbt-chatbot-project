1. Clone the repo
git clone https://github.com/your-username/dbt-chatbot.git
cd dbt-chatbot

2. Set up virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Add dbt metadata files

Copy these files from your dbt project into data/target/:

manifest.json

catalog.json



-Environment Variables

Create a .env file in the root:

GEMINI_API_KEY=your_api_key_here

- Usage
Step 1 – Parse dbt metadata
python src/parse_dbt.py

Step 2 – Format metadata into chunks
python src/format_metadata.py

Step 3 – Generate embeddings
python src/embed_data.py

Step 4 – Ask a question (basic FAISS retrieval)
python src/user_query.py

Step 5 – Query with Gemini API
python src/query_gemini.py



- Example Queries

“What does the fct_orders model represent?”

“Which models reference dim_customers?”

“List the columns of dim_products with descriptions.”

“How is fct_orders related to dim_customers?”



- Roadmap

 Add support for multi-turn conversations

 Visualize model relationships (ERD style)

 Streamlit UI for chatbot interaction

 Support for other LLMs (OpenAI, Anthropic, Local LLMs)