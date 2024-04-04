# Import Statements
# ----------------------------------------------------------------
import requests  # First party
from bs4 import BeautifulSoup  # Third party
from fpdf import FPDF  # Third party
# ----------------------------------------------------------------

# File Docstring
"""
Web scraper that downloads news articles and outputs them into a PDF.
"""

# Class Definitions
class ArticleToPDF:
    @staticmethod
    def fetch_article(url):
        """Fetches and parses the article content from the URL."""
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('h1').text
            paragraphs = soup.find_all('p')
            content = "\n".join([para.text for para in paragraphs])
            return title, content
        except requests.RequestException as e:
            print(f"Error fetching article: {e}")
            return "", ""

    @staticmethod
    def save_pdf(title, content, filename="article.pdf"):
        """Saves the article content to a PDF file."""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, title, ln=True)
        pdf.multi_cell(0, 10, content)
        pdf.output(filename)

# Example Usage
if __name__ == "__main__":
    url = "https://example.com/news-article"
    title, content = ArticleToPDF.fetch_article(url)
    ArticleToPDF.save_pdf(title, content, "news_article.pdf")
