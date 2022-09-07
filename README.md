# prepl
MongoDB partial replication with selective database/collection with the help of change stream.

Edit the `prepl_config.py` file and mention `source` URI from which you want to replicate the data. `target` in which you want to specify URI of the instance where the data to be replicated. An array of database names in `doDb` for those database you want to replicate. And `ignoreDB` array holds the name of databases which you want to ignore in replication.

Once done, install the dependencies using pip
```
pip install -r /path/to/requirements.txt
```

Now you are all set to run main script of the show `prepl.py`
```
python3 prepl.py
```

Sit back and relax the script replicates the data. As of now, this script is performing Insert, Update, and delete operation and no other operation like createIndex/dropIndex or any of the administration level task. For which you may have to code accordingly.
