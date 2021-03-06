from time import time, sleep
import requests
import numpy as np
import pickle


def send_image(image: np.ndarray, url: str) -> None:
    """
    Send an image to the server.
    """
    image_msg = image.tobytes()
    url += "image"
    data = {"array": image_msg, "dims": pickle.dumps(image.shape, 0)} # 0 encodes it in ascii, ensuring we can decode with just utf-8
    data = pickle.dumps({"array": image, "dims": image.shape}, 0) # 0 encodes it in ascii, ensuring we can decode with just utf-8
    r = requests.post(url, data=data)

    response = pickle.loads(r.content)
    print(response)
    # print(np.frombuffer(bytes(r.content["array"]), dtype=np.uint8))

def check_hello(url: str):
    """
    Check if the server is running.
    """
    r = requests.get(url)
    print(r.content)
    return r.content == b"/ -> /hello -> /goodbye"

def main():
    """
    Main function.
    """
    url = "http://127.0.0.1:5000/" # DON'T use 'localhost', adds a 1.5 second delay 
    # check_hello(url)

    image = np.ones((100, 100, 3), dtype=np.uint8)

    time_start = time()
    send_image(image, url)
    time_end = time()
    print("Time: {}".format(time_end - time_start))

    return time_end - time_start


if __name__ == "__main__":
    diffs = []
    main()
    # for i in range(50):
    #     diffs.append(main())
    #     sleep(0.1)
    # print("Average time: {}".format(sum(diffs) / len(diffs)))
