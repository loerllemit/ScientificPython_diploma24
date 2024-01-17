import time
import sample_mod as spmod

if __name__ == '__main__':
    start_time = time.time()
    spmod.recaman(30)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")

    start_time = time.time()
    spmod.recaman2(30)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")


