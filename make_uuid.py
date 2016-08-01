import uuid

class UUIDGenerator(object):

    def get_uuid(self):
        return bytes(uuid.uuid4())

if __name__ == '__main__':

    u = UUIDGenerator()

