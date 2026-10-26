### Cache

A temporary storage that keeps recently used data for fetching it faster.

### Caching strategies:

- Cache Aside: Checks in cache. If doesn't find the data, CLIENT FETCHES the data from the db.
- Write through: Writes in the cache first then caches synchs with the db.
- Read through: Checks in cache. If doesn't find the data, CACHE FETCHES the data from the db, writes in the cache and forwards the data to the client.

### Cache eviction policies:

- Least Recently used
- Least Frequently used
- Last In First Out
- Time To Live (TTL)

### Commmon issues in caching

1. Cache Stampede: It occurs when thousands of requests are being made for a certain cache data. When the data gets evicted there will be thousands of call being made to the database causing a stampede scenario. Fix involves:
   - Accepting only the first request made to the db while making the other requests wait for the data to be available on the cache itself
   - **Cache warming**: Keeping the frequently requested cache data updated before the data is evicted from the cache. Hence, never allowing the condition for stampede
