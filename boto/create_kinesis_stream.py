from boto import kinesis
kinesis = kinesis.connect_to_region("eu-west-1")
stream = kinesis.create_stream("BotoDemo", 1)
kinesis.describe_stream("BotoDemo")
kinesis.list_streams()
