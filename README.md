# Readme File

This Python script extracts images from a WordPress single post page and saves them to disk. The script requires a text file named 'pages.txt' which contains a list of URLs, with each URL on a new line.

## Prerequisites

The script requires the following libraries:

- requests
- BeautifulSoup
- os

These can be installed via pip or another package manager.

## Usage

1. Create a text file named 'pages.txt' containing a list of URLs, with each URL on a new line.
2. Run the script in a Python environment.
3. The script will loop through each URL in the 'pages.txt' file and extract all images from the post.
4. The images will be saved to a folder named after the last part of the URL, located in the same directory as the script.

Note: If you need to access private/draft posts, you can replace the cookie in the script. The user-agent is also required so that the server thinks the request is coming from Chrome and not a Python bot.

## Author

This script was written by Prabhat Giri. If you have any questions or concerns, you can reach the author at viaprabhat@gmail.com.

## License

This script is licensed under the [GNU GPL3.0 License](https://www.gnu.org/licenses/gpl-3.0.en.html).
