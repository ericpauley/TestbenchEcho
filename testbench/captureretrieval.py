from __future__ import print_function

import json
import redis

def lambda_handler(event, context):
    r = redis.Redis("104.236.205.31")
    ps = r.pubsub()
    ps.subscribe(event['id'])
    next(ps.listen())
    m = next(ps.listen())
    return m['data']
