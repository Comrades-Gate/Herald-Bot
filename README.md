# Herald-Bot

Created by Xxscorchxx5#4815. 
Contact me on Discord! (https://discord.gg/964zKCgkdx)

# Bot Prefix
The prefix `/hb` is hard-coded into main.py to invoke any of the bot features.

# Bot Features
`/hbsuggest <your_message>` - Posts an embed to the Herald Bot feature suggestion channel at Comrade's Gate that contains (1) the name of the user who made the suggestion and (2) a string of text provided by the user. Herald will automatically delete the invocation.

`/hbquote` - Herald bot replies with a random quote.

`/hbisad` - Feeling down? Herald will cheer you up!

# Selected Examples
- `/hbsuggest Add this cool new feature.`

# Scripts
- main.py - Where the magic happens.
- plot_weekdays.py - Analyzes the github CSV data and returns memberflow, voice, and message statistics for the Comrade's Gate Discord server.
- keep_alive.py - Prevents Herald Bot from going offline in Discord.

# Upcoming Patches
- Working on adding a feature that will return server information in .png format using a variation of the command: /hbserverstats
- Constructing a /hbhelp command for server-side bot documentation.
- Will be adding an error-management function that will return the proper usage of a command if an argument is missing.
