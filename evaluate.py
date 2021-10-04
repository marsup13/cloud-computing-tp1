import time
import requests

# The DNS address and path of the load balancer, like
url = "http://tp1-408593023.us-east-1.elb.amazonaws.com/cluster1"

def consumeGETRequestSync():
    r = requests.get(url)
    print(r.json(), end=' status ')
    print(r.status_code)

if __name__ == '__main__':
    start = time.time()
    for i in range(500):
        print(str(i) + ': ', end='')
        consumeGETRequestSync()
    print('time: ' + str(time.time()-start))
