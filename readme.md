# Bitwarden Backup Tool (R-Pi)
Backup Bitwarden tool for passwords and etc. Incase my VPS with Bitwarden goes boom (Back-up tool for R-Pi)
## How to use?
Before you start, ensure you have the Bitwarden command-line interface (CLI) client installed. Log in to your Bitwarden account using the CLI and retrieve the session key. Next, open the config.json file and paste the session key into it. Then, simply run the main.py script! It automatically initiates a backup process every 24 hours and stores the backups in a folder named backups.

*IF you are using R-PI you need to use the NPM client as there's no binaries for ARM/ARM64 (`npm install -g @bitwarden/cli`)*
