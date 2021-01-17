# Instagram data styled
A program to format your Instagram's "messages.json" into a beautiful and readable web
format.
> "messages.json" is a file containing all of your conversations and direct
> messages that you made with any account in instagram even if that account
> is no longer available.
You can get this file by [downloading your data from instagram](#How-to-download-your-data-from-Instagram).
## Getting Started
### Prerequisites
- python 3.9
(earlier versions might work, but they are not tested)
### Installing
You just have to `git clone` this repository:
`git clone https://github.com/adoliin/insta-data-styled`
## Usage
Just execute the "main.py" file like this:
`python src/main.py`
The program will then prompt for "messages.json" path.
After providing the path the program will then create a "conversations" folder
that contains 2 files and 2 folders:
- *messages-count.txt*:
A text file that tells how many messages you have with each Instagram user.

- *text-format*:
A folder containing all the conversations with each Instagram user in the form of text files.
These files are not really readable, but they are especially useful when
trying to use a tool like "ripgrep" to search for using a specific pattern in the messages.

- *web-format*:
Same as the "text-format" folder but instead of text files it contains HTML files.
Also the conversations are styled and formated so you can easily read the conversations
with each user.

- *style.css*:
The CSS file defining all the styles used by the HTML files inside "webformat".
You can change the different CSS classes to modify the styles of the conversations

## How to download your data from Instagram
Through the mobile app:
1. Open the Instagram app and go to your profile page by tapping your icon in the bottom-right corner.
2. In the upper-right hand corner of your profile page, tap the three horizontally stacked lines. Then, tap "Settings."
3. Select "Security."
5. Under "Data and History," tap "Download Data."
6. Enter your email address and then select "Request Download."
7. Enter your password and then tap "Next."

Through the website:
1. Visit the Instagram website and log in.
2. Click the profile icon in the upper-right hand corner of the screen, and then click "Settings."
3. Click "Privacy and Security" in the left sidebar.
4. Scroll down to find "Data Download." Then, click "Request Download."
5. Enter your email address and enter your Instagram password, then click "Request Download."

After that you'll receive an email with the data within 48 hours.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
