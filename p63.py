# # A simple Python function to check
# # whether x is even or odd

def evenOdd(x):
    """Function to check if the number is even or odd"""
    
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


# Driver code to call the function
print(evenOdd.__doc__)

# asynchronous
import asyncio

async def fnn():
    print("this is asynchronous")
    await asyncio.sleep(5)
    print("this is not threading")
    await asyncio.sleep(5)
asyncio.run(fnn())
