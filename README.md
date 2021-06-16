# anki-web-server

!!! Warning. The software is in a early stage, backup your data before use !!!

[anki](https://apps.ankiweb.net/) is a great website. It's supposed to be a life saver for people want to learn with flash cards. However, their sever is too slow and often fail to sync data from my iPhone.

This project is a personal web server replacement for the official ankiweb with limited functions. Inspired by [anki-sync-server](https://github.com/ankicommunity/anki-sync-server).

# Docker install
For a quick start, you can use docker. Please check [anki-web-server-docker](https://github.com/Nriver/anki-web-server-docker), it will start both snyc server and web server for you.


# Manual install Requirements
anki-web-server runs on Python 3(3.8 is preferred). It needs the [anki-sync-server](https://github.com/ankicommunity/anki-sync-server) from ankicommunity for data server.

# Manual Install

Use anki 2.1.40 for better compatibility.

1. Build up a [anki-sync-server](https://github.com/ankicommunity/anki-sync-server). Make sure you have already enabled user authentication and add some cards to the sync server.

2. Install requirements for anki-web-server.

```
pip install -r requirements.txt
```

3. Rename ankiweb.conf.sample to ankiweb.conf. You need to modify `anki_sync_server_path` to the location where you put the anki-sync-server while the program will look for `collections` folder in the path.

4. Run anki-web-server. 

```
python app.py
```

5. Open [http://127.0.0.1:27702/](http://127.0.0.1:27702/) in your browser. Enjoy!

(If you have set `context_path=ankiweb` in ankiweb.conf, the url would be [http://127.0.0.1:27702/ankiweb/](http://127.0.0.1:27702/ankiweb/).)

# vue api
[http://127.0.0.1:27702/api/](http://127.0.0.1:27702/api/)