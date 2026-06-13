# Mining Company Tracker

A Python-based web application to search public mining companies by ticker symbol and retrieve detailed information about their mining projects, reserves, grades, and production metrics.

## Features

✨ **Interactive Dashboard**
- Search mining companies by ticker symbol
- View company overview and metrics
- Browse mining projects with detailed specifications
- Real-time data display with beautiful UI

📊 **Comprehensive Mining Data**
- Project status (Producing, Development, Exploration)
- Ore types and composition
- Proven and probable reserves
- Grade percentages
- Strip ratios
- Production rates
- Project locations

🏢 **Supported Companies**
- BHP Group
- Rio Tinto
- Vale S.A.
- Freeport-McMoRan
- Newmont Corporation
- And more...

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/AnthonyH1507/Mining-Company-Tracker.git
cd Mining-Company-Tracker
```

### Step 2: Create a Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment File

```bash
cp .env.example .env
```

The `.env` file contains:
- `FLASK_ENV=development`
- `FLASK_DEBUG=True`
- `PORT=5000`

(Default values are fine for local development)

### Step 5: Run the Application

```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Step 6: Open in Your Browser

Go to: **http://localhost:5000**

You'll see the Mining Company Tracker dashboard!

## How to Use

### Search for a Company

1. **Enter a ticker symbol** in the search box (e.g., BHP, RIO, VALE, FCX, NEM)
2. **Click Search** or press Enter
3. View company information and mining projects

### Quick Access

Click any company tile under "Major Mining Companies" to instantly search that company.

### View Metrics

The **Metrics** tab shows aggregated data:
- Total projects (Producing vs Development)
- Total proven and probable reserves
- Average grade
- Ore types

### Browse Projects

The **Projects** tab displays each mining project with:
- Project name and location
- Development stage
- Ore types
- Reserve estimates (Proven/Probable in Mt)
- Grade percentage
- Strip ratio
- Production rate

## Project Structure

```
Mining-Company-Tracker/
├── app.py                          # Main Flask application
├── config.py                       # Configuration settings
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── templates/
│   ├── base.html                   # Base HTML template with styling
│   └── index.html                  # Dashboard page
├── static/
│   └── styles.css                  # Additional CSS styles
├── src/
│   ├── services/
│   │   ├── ticker_service.py       # Company ticker lookups
│   │   └── mining_data_service.py  # Mining project data retrieval
│   ├── models/
│   │   └── mining_project.py       # Mining project data model
│   ├── data/
│   │   └── mining_data.py          # Sample mining company data
│   └── utils/
│       └── error_handler.py        # Error handling utilities
```

## API Endpoints

### GET `/`
Opens the web dashboard

### POST `/api/company/search`
Search for a company by ticker
```bash
curl -X POST http://localhost:5000/api/company/search \
  -H "Content-Type: application/json" \
  -d '{"ticker": "BHP"}'
```

### GET `/api/company/<ticker>/projects`
Get all mining projects for a company
```bash
curl http://localhost:5000/api/company/BHP/projects
```

### GET `/api/company/<ticker>/metrics`
Get aggregated metrics for a company
```bash
curl http://localhost:5000/api/company/BHP/metrics
```

### GET `/api/tickers/major-mining-companies`
Get list of all major mining companies
```bash
curl http://localhost:5000/api/tickers/major-mining-companies
```

## Supported Tickers

| Ticker | Company | Country |
|--------|---------|---------|
| BHP | BHP Group | Australia |
| RIO | Rio Tinto | UK/Australia |
| VALE | Vale S.A. | Brazil |
| FCX | Freeport-McMoRan | USA |
| NEM | Newmont | USA |
| GLD | Barrick Gold | Canada |
| AEM | Agnico Eagle Mines | Canada |
| TECK | Teck Resources | Canada |
| AA | Alcoa | USA |
| CLF | Cleveland-Cliffs | USA |
| MOS | Mosaic | USA |

## Future Enhancements

- [ ] Integration with SEC EDGAR for real mining project data
- [ ] Real-time stock price data
- [ ] Interactive charts and graphs
- [ ] Project timeline comparisons
- [ ] Reserve trend analysis
- [ ] Export to PDF/CSV
- [ ] Multi-year historical data
- [ ] Advanced filtering and sorting

## Development

### Running Tests
```bash
pytest tests/
```

### Adding New Companies

Edit `src/data/mining_data.py` and add company data following the existing format.

### Customizing Styles

Edit `templates/base.html` for major styles or `static/styles.css` for additional styles.

## Troubleshooting

### "Port 5000 already in use"
```bash
# Change the port in .env
PORT=5001
```

### "ModuleNotFoundError"
Make sure virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

### "Company not found"
Check that the ticker is in the supported list and spelled correctly (case-insensitive).

## Technologies Used

- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing
- **Python** - Backend language
- **HTML5/CSS3/JavaScript** - Frontend
- **Bootstrap 5** - UI framework
- **Font Awesome** - Icons

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or support, please open an issue on GitHub.

---

**Happy mining data exploring!** ⛏️
