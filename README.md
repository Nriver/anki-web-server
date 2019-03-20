# anki-web-server

!!! Warning. The software is in a early stage, backup your data before use !!!

[anki](https://apps.ankiweb.net/) is a great website. It's supposed to be a life saver for people want to learn with flash cards. However, their sever is too slow and often fail to sync data from my iPhone.

This project is a personal web server replacement for the official ankiweb with limited functions. Inspired by [anki-sync-server](https://github.com/tsudoko/anki-sync-server).

# Requirement
anki-web-server requires the [anki-sync-server](https://github.com/tsudoko/anki-sync-server) from tsudoko.

# Install
1. Build up a [anki-sync-server](https://github.com/tsudoko/anki-sync-server).

2. Modify anki-sync-server code. Open anki-sync-server/ankisyncd/thread.py. Change the value of monitor_frequency and monitor_inactivity in  to a small value(say 1 and 3).

3. Install anki.

        $ git submodule update --init
        $ cd anki-bundled
        $ pip install -r requirements.txt

4. Install requirements for anki-web-server.(different from anki)

        $ pip install -r requirements.txt

5. Rename ankiweb/ankiweb.conf.sample to ankiweb/ankiweb.conf and modity the content with your setup.

6. Run anki-web-server.

        $ pip install -r requirements.txt

7. Open [http://127.0.0.1:27702/ankiweb/](http://127.0.0.1:27702/ankiweb/) in your browser.