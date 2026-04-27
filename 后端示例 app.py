from flask import Flask, request, jsonify, render_template
from scrapers.pinterest_scraper import scrape_pinterest
from scrapers.behance_scraper import scrape_behance

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if not query:
        return jsonify([])

    # 调用两个爬虫
    pinterest_results = scrape_pinterest(query)
    behance_results = scrape_behance(query)

    # 合并结果
    results = pinterest_results + behance_results
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
