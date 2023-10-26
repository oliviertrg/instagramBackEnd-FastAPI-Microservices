import time 
# import asyncio


# def x():
#     time.sleep(5)
#     print("done")


# def y():
#     time.sleep(5)
#     print("done")
#     # a = [i for i in range(100000000)]    
# async def d():
#    x()
#    await y()    
#    print("done")

# start_time = time.time()
# asyncio.run(d())
# end_time = time.time()
# print(end_time - start_time  )

# import asyncio

# async def x():
#     time.sleep(5)
#     a = [i for i in range(100000000)] 
#     print("done")

# async def y():
#     # time.sleep(5)
#     a = [i for i in range(100000000)] 
#     print("done")

# async def main():
#     task1 = asyncio.create_task(x())
#     task2 = asyncio.create_task(y())

#     await task1
#     await task2

import asyncio

async def x(x):
    # a = [i for i in range(10)]
    print("done",x)
    return await x
    # return await a

async def y():
    # a = [i for i in range(10)]
    print("done")
    # return await a
async def main():

    task1 = asyncio.run(x(10))
    task2 = asyncio.create_task(y())
    print(task1)
    # await task1
    # await task2

# def x():
#     a = [i for i in range(100000000)]
#     print("done")

# def y():
#     a = [i for i in range(100000000)]
#     print("done")
# def main():
#     x()
#     y()

   


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    # main()
    end_time = time.time()
    print(end_time - start_time  )

# # Import the time module
# import time

# # Sleep for 5 seconds
# time.sleep(5)

# # Sleep for 1 second and then print a message
# time.sleep(1)
# print("Hello, world!")
# # import uuid
# a = uuid.uuid4()
# print(a)
# import time 
# import asyncio


# def x():
#     a = [i for i in range(100000000)]

# def y():
    
#     a = [i for i in range(100000000)]    
# def d():
#    x()
#    y()    
#    print("done")

# start_time = time.time()
# d()
# end_time = time.time()
# print(end_time - start_time  )



