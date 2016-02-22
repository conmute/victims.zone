# Victims.zone - the place where we remember.

## Logotype example

Crash test dummy sign:

`http://www.vecteezy.com/vector-art/89361-crash-test-dummy-symbol-icons`

## Technology base

backend: python(flask)
frontend: javascript(jquery)+css(less)+html(jade)

## User behaviour and results, or in other words "The Flow of application"

> Watch (as anonymous user)
> > The map with area or markers of victims locations
> > Date filter slider above the map
> > On clicking of location/area show information about it
> Add (as registered user)
> > Add victim(-s) information group information, and single instance information
> > Add memories about victim(-s)
> Update (as registered user)
> > Fix the information give by other user about victim(-s)
> > Answer to a memory given by someone else

## Development steps

* Facebook login/authorisation: email, id, socialservice, name, photo_url
* Add record one of these types
    - Person type: name, date, description, photos, location, tags, category, author_id
    - Event type: name, date, description, photos, map_area, tags, category, author_id
    - Memory: photos, description, date, link_url, obj_id, obj_type
* Visualise on map: date range, areas and markers are clickable with sidebar info details
* Update someones record:
    - Object update: obj_id, obj_type, name, date, description, photos, location, tags, category, author_id


## Tech specs

Runs on python3.4

To make it work:

```bash
source venv/bin/activate

# Start app
python app.py runserver --port {port} --host {host.IP}

# And on work done ust do:
deactivate
```

*During development*

```bash
npm install -g bower
```

*Watch and compile less during development*

```bash
cd assets/
while true;do N=`find -name "*.less" `;inotifywait -qe modify $N ;for f in $N; do lessc -x less/app.less --source-map ../victims/static/css/app.css;done;done
```


## Some resources for later

https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
http://flask-sqlalchemy.pocoo.org/2.1/models/