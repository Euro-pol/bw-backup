# bw-backup
simple bitwarden backup script, intended for personal use on my raspberry pi (in case my VPS hosting bitwarden goes BOOM)
## how to use?
you need the bitwarden cli client installed. login to your account, and get the session key. then put it in config.json, and run the main.py! it will run the backup script every 24 hours, and save the backups in the `backups` folder.

*if you're on a raspberry pi, you need to use the NPM client as there's no binaries for ARM/ARM64 (`npm install -g @bitwarden/cli`)*
