# Telegram_Auto_Views

This is a Telegram bot designed to increase the views on a specific Telegram post using proxies. The bot scrapes proxies from given sources and uses them to send view requests to the specified Telegram post.

## Features
- Scrapes HTTP, SOCKS4, and SOCKS5 proxies from specified sources.
- Validates the scraped proxies.
- Sends view requests to a specified Telegram post using the valid proxies.
- Provides real-time status updates on the number of views, proxy errors, and token errors.

## Requirements
- Python 3.6+
- Required Python packages (specified in `requirements.txt`)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Aadarsh-Mourya/Telegram_Auto_Views.git
    cd Telegram_Auto_Views
    ```

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    - Create a `.env` file in the root directory of your project.
    - Add the following line to the `.env` file with your specific Telegram post URL:
      ```env
      POST_URL=https://t.me/yourchannel/yourpost
      ```

## Usage

1. **Run the bot:**
    ```bash
    python main.py
    ```

2. **Monitor the bot:**
    - The bot will start scraping proxies, validate them, and send view requests to the specified Telegram post.
    - The bot will provide real-time updates in the console, including the number of live views, token errors, proxy errors, and active threads.

## File Structure

- `main.py`: Main script to run the bot. Initializes and starts the view update and command line interface threads.
- `sources.py`: Contains functions for loading configurations and user input, and a function for displaying real-time updates.
- `proxyScrapper.py`: Contains the `Proxy` class for scraping proxies from given sources.
- `sendView.py`: Contains the `Api` class for sending view requests to the specified Telegram post and validating proxies.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add some feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) for the Telegram bot API.
- [requests](https://github.com/psf/requests) for HTTP requests.
- [fake_useragent](https://github.com/hellysmile/fake-useragent) for generating random User-Agent headers.
