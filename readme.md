### KANBAN BOARD

https://kanbanflow.com/board/yj8ydSr

### Wiki

The wiki contains the project plan, wireframe, diagarms, tasks, etc.
To download the wiki, run the following:
```
git clone https://github.com/StvnLm/NotStockWatcher.wiki.git
```

To instantiate the SQLITE database, delete any pycache files, and migration cache files. Delete the sqlite3 file to start anew.
Doing this will nuke your database. Only do these steps for DEV environments.
<app> parameter is optional. You can leave this out or plug in the stockwatcher app name.
```
python manage.py makemigrations <app>
python manage.py migrate <app>
```

To import the data from the Stock Watcher API:
```
python.exe .\manage.py getapi
```
