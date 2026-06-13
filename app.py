import os
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from config import config
from src.services.ticker_service import TickerService
from src.services.mining_data_service import MiningDataService
from src.utils.error_handler import handle_error

app = Flask(__name__, 
            template_folder='templates',
            static_folder='static',
            static_url_path='/static')
app.config.from_object(config[os.getenv('FLASK_ENV', 'development')])
CORS(app)

# Initialize services
ticker_service = TickerService()
mining_data_service = MiningDataService()

# ==================== WEB ROUTES ====================

@app.route('/')
def index():
    """Home page - main dashboard"""
    return render_template('index.html')

@app.route('/companies')
def companies():
    """Companies listing page"""
    return render_template('index.html')

# ==================== API ROUTES ====================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Mining Company Tracker API is running'
    }), 200

@app.route('/api/company/search', methods=['POST'])
def search_company():
    """Search for a mining company by ticker"""
    try:
        data = request.get_json()
        ticker = data.get('ticker', '').upper()
        
        if not ticker:
            return jsonify({'error': 'Ticker symbol required'}), 400
        
        company_info = ticker_service.search_ticker(ticker)
        
        if not company_info:
            return jsonify({'error': f'Company with ticker {ticker} not found'}), 404
        
        return jsonify(company_info), 200
    except Exception as e:
        return handle_error(e)

@app.route('/api/company/<ticker>/projects', methods=['GET'])
def get_mining_projects(ticker):
    """Get all mining projects for a company"""
    try:
        ticker = ticker.upper()
        projects = mining_data_service.fetch_mining_projects(ticker)
        
        if not projects:
            return jsonify({
                'message': f'No mining projects found for {ticker}',
                'data': []
            }), 200
        
        return jsonify({
            'ticker': ticker,
            'project_count': len(projects),
            'projects': projects
        }), 200
    except Exception as e:
        return handle_error(e)

@app.route('/api/company/<ticker>/projects/<project_name>', methods=['GET'])
def get_project_details(ticker, project_name):
    """Get detailed information for a specific mining project"""
    try:
        ticker = ticker.upper()
        project = mining_data_service.fetch_project_details(ticker, project_name)
        
        if not project:
            return jsonify({'error': f'Project {project_name} not found for {ticker}'}), 404
        
        return jsonify(project), 200
    except Exception as e:
        return handle_error(e)

@app.route('/api/company/<ticker>/metrics', methods=['GET'])
def get_mining_metrics(ticker):
    """Get aggregated mining metrics for a company"""
    try:
        ticker = ticker.upper()
        metrics = mining_data_service.calculate_company_metrics(ticker)
        
        if not metrics:
            return jsonify({'error': f'No metrics found for {ticker}'}), 404
        
        return jsonify(metrics), 200
    except Exception as e:
        return handle_error(e)

@app.route('/api/tickers/major-mining-companies', methods=['GET'])
def get_major_mining_companies():
    """Get a list of major publicly traded mining companies"""
    try:
        companies = ticker_service.get_major_mining_companies()
        return jsonify({
            'count': len(companies),
            'companies': companies
        }), 200
    except Exception as e:
        return handle_error(e)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
