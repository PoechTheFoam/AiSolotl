# 🦎 AiSolotl 🦎 #
An inbox summarization tool.
The current version of AiSolotl is a prototype made only for the web version of Messenger, which requires its designated message scraper web extension to work (https://github.com/PoechTheFoam/AiSolotl-Web-Messenger-Scraper)
## Using AiSolotl ##
###  1. Features  ###
- Gives a structured summary on the main content of messages:
    + An overall summary of all chosen conversations
    + Summary cards categorized by urgency and topic
    + Includes deadlines and small suggested actions for important events

### 2. Installation ###
## A> The extension
Installing the scraper extension:
For Windows machines using Chrome, or an equivalent Chromium-based browser:
1. Download the latest release ZIP 
(https://github.com/PoechTheFoam/AiSolotl-Web-Messenger-Scraper/releases/tag/v.1.0)
2. Extract it
3. Open the extensions page
4. Enable Developer mode
5. Choose Load unpacked
6. Make sure you see the "src" folder
7. Click Select

## B> AiSolotl (the backend)
1. Download the latest release ZIP
2. Get your Gemini API key, create a ".env" file and write in it:
'GEMINI_API_KEY="[your Gemini API key here]"'
3. Before running AiSolotl's Web Messenger messages scraper, run "fastapi dev main.py" in your powershell, the location should be wherever you are storing the AiSolotl folder
(For example, I store AiSolotl in the D drive, so it would look like "D:\AiSolotl> fastapi dev main.py")

For MacOS/Linux, or other browsers:
(Not available, any contribution would be appreciated!)

## Why it was created ##
### 1. Keeping up with conversations ###
- Multiple messages in 1 conversation can talk about various topics
- Each conversation may talk about a different topic
- All conversations may talk about a single topic
- Distinguish work, casual/friend messages, actionable items, and urgent replies.

### 2. Why Web Messenger as the prototype?  ###
- There has yet to be a Meta AI summary feature for Web Messenger/PC Messenger at the time of the tool's creation.
=> This aimed to be a way for users to summarize messages on PC as well.

## Workflow ##
1. Users open the AiSolotl panel by clicking on the scraper extension icon, a panel like this should pop up:
![panel](docs\assets\images\Scraper_UI.png)
2. Users need to wait initially for the tool to finish initialization ->  After it finishes, the "Browse" and input field for amount of scrolls will be clickable.
3. Users next either input how many scrolls they expect the tool to scroll up inside conversations, or browse conversations they wish to summarize first.
4. After both fields are satisfied (selected conversations and specified amount of scrolls), hit "Summarize" to start the summary.
5. Wait for the summary!

## Limitations ##
1. Currently, the tool is not accessible to average users yet, as the setup and installation process introduces a lot of friction (requiring both user's Gemini API key, setting up a local http server via running "fastapi dev main.py", and downloading a separate scraper function)
2. The summarization process requires heavy optimization so as to increase its speed, as it currently requires about 10-15 seconds to settle first before extracting messages for the summary.
3. The scraper relies heavily on Messenger's DOM structure, meaning any future changes to it may ofuscate AiSolotl.