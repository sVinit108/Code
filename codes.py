#RPC
'''
from xmlrpc.server import SimpleXMLRPCServer

# Define functions to be exposed
def add(x, y):
  """Adds two numbers together."""
  return x + y

def subtract(x, y):
  """Subtracts two numbers."""
  return x - y

# Create a server object
server = SimpleXMLRPCServer( ("localhost", 8000) )

# Register functions as methods
server.register_function(add, "add")
server.register_function(subtract, "subtract")

# Print a server started message
print("Server listening on port 8000...")

# Start the server
server.serve_forever()

#server side
import xmlrpc.client

proxy= xmlrpc.client.ServerProxy("http://localhost:8000")
x=1
y=2
result=proxy.add(x,y)
print(result)
'''

#Interprocess COMM
'''
import multiprocessing
def send_msgs(conn, msgs):
    for msg in msgs:
        conn.send(msg)
    conn.close()
    
def recv_msg(conn):
    while 1:
        msg = conn.recv()
        if msg == "END":
            break
        print(msg)

msgs = ["Hey", "Hello", "Hru?", "END"]

parent_conn, child_conn = multiprocessing.Pipe()
p1 = multiprocessing.Process(target=send_msgs, args=(parent_conn, msgs))
p2 = multiprocessing.Process(target=recv_msg, args=(child_conn,))


if __name__ == '__main__':
  p1.start()
  p2.start()

  p1.join()
  p2.join()
'''

# election algo - gfg code

# clock syn - gfg
import time

class ClockSynchronizer:
    def __init__(self, master_node):
        self.master_node = master_node
        self.offset = 0

    def synchronize(self):
        # Get the time from the master node
        master_time = self.master_node.get_time()

        # Calculate the offset between the local clock and the master clock
        self.offset = master_time - time.time()

    def get_synchronized_time(self):
        # Return the current time, adjusted for the offset
        return time.time() + self.offset

# Create a clock synchronizer object
synchronizer = ClockSynchronizer("master_node")

# Synchronize the local clock
synchronizer.synchronize()

# Get the synchronized time
synchronized_time = synchronizer.get_synchronized_time()

# Print the synchronized time
print(synchronized_time)

#Token algo
'''
class TokenBasedAlgorithm:
    def __init__(self, num_processes):
        self.token = 0
        self.processes = [i for i in range(num_processes)]

    def acquire_token(self, process_id):
        while self.token != process_id:
            pass

    def release_token(self):
        self.token = (self.token + 1) % len(self.processes)

# Example usage:

algorithm = TokenBasedAlgorithm(5)

# Process 0 acquires the token
algorithm.acquire_token(0)

# Process 0 releases the token
algorithm.release_token()

# Process 1 acquires the token
algorithm.acquire_token(1)

# ...
'''