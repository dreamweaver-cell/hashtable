def new(number_of_buckets = 128):
    """Initializes a Map with the a specified number of buckets."""
    hmap = []
    for i in range(number_of_buckets):
        hmap.append([])
    return hmap


def hash_key(hmap, key):
    """Takes a key, create a hash number from it and then convert it to an index for the hashmap's bucket."""
    return hash(key) % len(hmap)


def get_bucket(hmap, key):
    """Given a key, get the bucket index."""
    bucket_id = hash_key(hmap, key)
    return hmap[bucket_id]


def get_slot(hmap, key, default=None):
    """Returns the index, key, and value of a slot found in a bucket. Returns -1, key, and none when not found."""
    bucket = get_bucket(hmap, key)

    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v

    return -1, key, default


def set(hmap, key, value):
    """Set the key to the value or replacing any existing value."""
    bucket = get_bucket(hmap, key)
    i, k, v = get_slot(hmap, key)

    if i >= 0:
        """If the key exists, replace it"""
        bucket[i] = (key, value)
    else:
        """the key does not, append to create it"""
        bucket.append((key, value))


def get(hmap, key, default=None):
    """Gets the value in a bucket for the given key if it exist"""
    i, k, v = get_slot(hmap, key, default=default)
    return v


def delete(hmap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(hmap, key)

    for i in enumerate(bucket):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break


def list(hmap):
    """ Print bucket content"""
    for bucket in hmap:
        if bucket:
            for k, v in bucket:
                print(k, v)
