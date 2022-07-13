from time import time, sleep
import requests
import numpy as np


def send_image(image: np.ndarray, url: str) -> None:
    """
    Send an image to the server.
    """
    image_msg = image.tobytes()
    url += "image"
    data = {"message": image_msg, "array": image_msg}
    r = requests.post(url, data=data)
    print(r.content)
    print(np.frombuffer(bytes(r.content), dtype=np.uint8))


def main():
    """
    Main function.
    """
    url = "http://127.0.0.1:5000/"
    image = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)
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
