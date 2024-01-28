tok = WordPunctTokenizer()
stop_words = set(stopwords.words('english'))
url_pattern = r'https?://[^\s]+'
html_pattern = r'&[^;\s]+;'
punct_pattern = r'[' + re.escape(string.punctuation) + ']'

def preprocess_text(text):
    text = str(text) if not pd.isna(text) else ''
    text = BeautifulSoup(text, 'html.parser').get_text()
    text = re.sub(url_pattern, '', text)
    text = re.sub(html_pattern, '', text)
    text = re.sub(punct_pattern, '', text)
    words = [word.lower() for word in tok.tokenize(text) if word.lower() not in stop_words]
    return ' '.join(words)
