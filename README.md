# anki-web-server

!!! Warning. The software is in a early stage, backup your data before use !!!

[anki](https://apps.ankiweb.net/) is a great website. It's supposed to be a life saver for people want to learn with flash cards. However, their sever is too slow and often fail to sync data from my iPhone.

This project is a personal web server replacement for the official ankiweb with limited functions. Inspired by [anki-sync-server](https://github.com/ankicommunity/anki-sync-server).

# Requirement
anki-web-server runs on Python 3. It needs the [anki-sync-server](https://github.com/ankicommunity/anki-sync-server) from ankicommunity for data server.

# Install
1. Build up a [anki-sync-server](https://github.com/tsudoko/anki-sync-server). Make sure you have already enabled user authentication and add some cards to the sync server.

2. Install requirements for anki-web-server.

```
pip install -r requirements.txt
```

3. Rename ankiweb.conf.sample to ankiweb.conf. You need to modify `anki_sync_server_path` to the location where you put the anki-sync-server while the program will look for `collections` folder in the path.

4. Run anki-web-server. 

```
python app.py
```

5. Open [http://127.0.0.1:27702/ankiweb/](http://127.0.0.1:27702/ankiweb/) in your browser. Enjoy!