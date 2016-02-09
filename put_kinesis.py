import testdata
import json
from boto import kinesis

kinesis = kinesis.connect_to_region("eu-west-1")

class Users(testdata.DictFactory):
     firstname = testdata.FakeDataFactory('firstName')
     lastname = testdata.FakeDataFactory('lastName')
     age = testdata.RandomInteger(10, 30)
     gender = testdata.RandomSelection(['female', 'male'])

for user in Users().generate(5000):
     print(user)
     kinesis.put_record("BotoDemo", json.dumps(user), "partitionkey")
