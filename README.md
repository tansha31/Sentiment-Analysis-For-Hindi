<h1 align="center">
Sentiment Analysis for Hindi
</h1>

Accurate sentiment analysis for your documents and text in Hindi.

## 💻 Running Locally

1. Clone the repository 📂

```bash
git clone https://github.com/tansha31/Sentiment-Analysis-For-Hindi.git
cd Sentiment-Analysis-For-Hindi
```

2. [Download](https://drive.google.com/file/d/1Tqx3tX5pcBHFpy-04OsYODepjiRV2MMy/view?usp=share_link) and copy pytorch_model.bin to distilBert folder.

```bash
mv pytorch_model.bin Sentiment-Analysis-For-Hindi/distilBert
```

3. Install dependencies with [Pip](https://pypi.org/project/pip) and activate virtual environment 🔨

```bash
pip install -r requirements.txt
```

4. Run the Model server.

```bash
cd Sentiment-Analysis-For-Hindi
python server.py
```

5. Run the Streamlit server 🚀

```bash
cd Sentiment-Analysis-For-Hindi
streamlit run app.py
```
