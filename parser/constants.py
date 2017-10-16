# STREAM_ID = 'feed%2Fhttp%3A%2F%2Ffeeds.feedburner.com%2Ftrdnews' Test feed
STREAM_ID='feed/http://www.cnbc.com/id/10000115/device/rss/rss.html'
FEEDLY_API_URL = 'http://cloud.feedly.com/v3/streams/contents?streamId=feed%2Fhttp%3A%2F%2Ffeeds.feedburner.com%2Ftrdnews'
FEEDLY_API_URL_CELERY = 'http://cloud.feedly.com/v3/streams/contents?streamId=%s' % STREAM_ID
FEEDLY_GET_CATEGORIES_URL = 'http://sandbox7.feedly.com/v3/categories/Finance'
DEV_TOKEN = 'AzZVWr0jpfS3DDqq1NgCHgYRnmpzuHDsYPC-3Y6wZj6KBIhaD3f9njOuQ6cqSLMnl_p4FBS96tqggIn5JXgvzszQzKlnOsPkpKgDqYezfYWRa2yd9Itm_sM0Vwkp-bQ17bqZ6r0bMOQGwpPnV7k6WY5ebCl2_wZwgcxADiyBwr_KWQJ7equhbsOlU3dSClej-lK-5AJ5fddURsG7zBnYr2bt93lftw:feedlydev'
CLIENT_ID = '3306a8e8-2885-4750-829b-30d15549ecdb.'
FEEDLY_PROFILE = "http://cloud.feedly.com/v3/profile"

# Getting stream ids
FEEDLY_API_URL_IDS = 'http://sandbox7.feedly.com/v3/streams/ids?streamId=feed%2Fhttp%3A%2F%2Ffeeds.feedburner.com%2Ftrdnews'

# get specific strem entry

STREAM_ENTRY = 'https://sandbox7.feedly.com/v3/entries/%s'  # replace %s with stream id got from FEEDLY_API_URL_IDS and don't forget to do url encode on id

FEEDLY_PRODUCTION_URL='cloud.feedly.com'
FEEDLY_ACCOUNT_TOKEN = 'Azz5rr9MzYSNveu1WsYTjyPI3xe7GV2bbciCoU5_uTE8hcb1e6yBHgRvrGRJJypWigZMq2-9eyUczGwOBUNjFn9vUqfJaA49O2BuaU9ObWCQZdjzL216h4diE9-1bGFxMOZvwesZvDLCt80w9II4vaFimM7rXpppQZJHOz0RbNAuQ21OwFeMOvMjkjggdOXp31SOGnCn-WNcIg8Si375KkE:feedlydev'
FEEDLY_REFRESH_ACCOUNT_TOKEN = 'Azz5rr9MzYyNvevKDcUSgmPdrV-oHgmRMJmV5VBwvXY11979f_mBTwQ7-WxMLj9WzgYXvWOtBXROnTBEFz81Uyw6DO-fIgAzcDR2cVQMeWqVKY6xa2d2nc5tT5jpc3ggYeI03OIV7TGWvp1h-I81sLBimN3rXppqXYgBLzYAJZtzFi8BlkrBbuAjkjogdOWojgncXCPFsixFaVkemGP7KhBlEOCqBRIfo-hojqH54uqtXeXU_u4ve_hhH_G8FCs'
