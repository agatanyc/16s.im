This project defines an HTTP server that lets you collect stats of a given site.  It is still a working progress.
It works only on `local host`.

## Dependencies

graphite
statsd
Running the server

## For development (in seperate terminals) run

### carbon and graphite-web—parts of graphite
  
`python /opt/graphite/bin/carbon-cache.py start`

(__You can ignore the message: 'WHISPER_FALLOCATE_CREATE is enabled but linking failed.'__)
 
`python /opt/graphite/bin/run-graphite-devel-server.py /opt/graphite`
### statsd

`node /opt/statsd/stats.js /opt/statsd/config.js`

### application

`python ~/projects/analytics/main.py`


__To send multiple HTTP requests, run:__

`ab -n 10 -c 10 http://127.0.0.1:5000/page/49`

49 is the page ID in this case

__To view graphs locally in a browser run:__

`localhost80:80`

## Deployment

TBD
