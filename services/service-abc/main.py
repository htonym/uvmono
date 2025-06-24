from lib_a.info import lib_name
from lib_a.req import send_request


def main():
    print("Hello from service-abc!")
    lib_name()

    result = send_request()
    for record in result:
        print(record)


if __name__ == "__main__":
    main()
