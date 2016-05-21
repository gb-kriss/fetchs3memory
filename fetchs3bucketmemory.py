from boto.s3.connection import S3Connection
from boto.s3.connection import OrdinaryCallingFormat
def sizeof_fmt(num):
   for x in ['bytes','KB','MB','GB','TB']:
       if num < 1024.0:
           return "%3.1f %s" % (num, x)
       num /= 1024.0

conn = S3Connection('s3key', 's3secretkey',calling_format=OrdinaryCallingFormat())
print conn
total_bytes=0
buckets = conn.get_all_buckets()
for key in buckets:
     print key.name
       try:
        bucket=conn.get_bucket(key.name)
       except :
         print "s3 exception"
       bucket_size=0
       for key1 in bucket:
        #bucket_size=0
        bucket_size +=key1.size
        total_bytes +=key1.size
        sebucket= sizeof_fmt(bucket_size)
        print key.name
        print  sebucket       
print "total bucket size " % sizeof_fmt(total_bytes)
  #  get_bucket_size(key.name)
 
