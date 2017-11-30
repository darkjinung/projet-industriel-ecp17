# coding: utf-8
import get_this_one_Feature_extract_optimized
import timeit
import os
import psutil


for i in range(0, 7):
    start_time = timeit.default_timer()
    get_this_one_Feature_extract_optimized.main(i)
    elapsed = timeit.default_timer() - start_time
    print(elapsed)
    process = psutil.Process(os.getpid())
    print((process.memory_info().rss) / 1073741824.0)
    print("##########################")


# ###########get memory of the program ( python process )####################

# ##########################
