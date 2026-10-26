### **Cache**

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

###
