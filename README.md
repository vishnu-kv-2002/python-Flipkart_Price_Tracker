# 🛒 Flipkart Price Tracker

A Python web scraping project that monitors the price of an iPhone 15 on Flipkart and sends an email notification when the price drops below a specified target price.

## 🚀 Features

- Scrapes product prices from Flipkart using BeautifulSoup.
- Extracts the product title and current price.
- Converts the price into a numeric value for comparison.
- Checks whether the current price is below the target price.
- Sends an email alert when the product reaches the desired price.
- Uses environment variables to protect email credentials.

## 🛠️ Technologies Used

- Python
- Requests
- BeautifulSoup
- SMTP
- Python-dotenv

## 📦 Installation

1. Clone this repository.
2. Install the required libraries:

   ```bash
   pip install requests beautifulsoup4 python-dotenv
   ```

## 🔐 Environment Variables

Create a `.env` file in the project directory:

```env
SMTP_EMAIL=your_email@gmail.com
SMTP_PASS=your_app_password
```

Replace the example values with your email address and Gmail App Password.

**Security:** Never upload your `.env` file or email credentials to GitHub. Add `.env` to your `.gitignore` file.

## ⚙️ How It Works

1. Sends an HTTP request to the Flipkart product page.
2. Parses the webpage using BeautifulSoup.
3. Extracts the product title and current price.
4. Removes the rupee symbol and commas from the price.
5. Converts the price into a floating-point number.
6. Compares the current price with the target price of ₹70,000.
7. Sends an email notification if the current price is below the target.

## ▶️ How to Run

Run the Python script:

```bash
python main.py
```

If the product price is below ₹70,000, an email alert will be sent to the configured email address.

## 🧠 Concepts Learned

- Web scraping with Python
- HTTP requests and headers
- HTML parsing with BeautifulSoup
- String manipulation and type conversion
- Conditional statements
- Sending emails using SMTP
- Managing credentials with environment variables

## 🔮 Future Improvements

- Allow users to configure the target price.
- Check the product price automatically at regular intervals.
- Track multiple products.
- Store historical prices in a database.
- Handle missing product details and request errors.

## 👨‍💻 Author

**Vishnu K V**