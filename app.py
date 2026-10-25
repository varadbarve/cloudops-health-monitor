import time
import urllib.error
import urllib.request

URLS = [
    "https://www.google.com",
    "https://github.com",
    "https://aws.amazon.com",
]


def check_website(url):
    start_time = time.perf_counter()

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "CloudOpsHealthMonitor/1.0"},
        )

        with urllib.request.urlopen(request, timeout=5) as response:
            latency = (time.perf_counter() - start_time) * 1000

            return {
                "url": url,
                "status": response.status,
                "latency_ms": round(latency, 2),
                "healthy": 200 <= response.status < 400,
            }

    except (urllib.error.URLError, TimeoutError, OSError) as error:
        latency = (time.perf_counter() - start_time) * 1000

        return {
            "url": url,
            "status": "ERROR",
            "latency_ms": round(latency, 2),
            "healthy": False,
            "error": str(error),
        }


def main():
    print("CloudOps Health Monitor")
    print("=" * 50)

    for url in URLS:
        result = check_website(url)

        status = "UP" if result["healthy"] else "DOWN"

        print(
            f'{status} | {result["url"]} | '
            f'Status: {result["status"]} | '
            f'Latency: {result["latency_ms"]} ms'
        )

        if "error" in result:
            print(f'  Error: {result["error"]}')


if __name__ == "__main__":
    main()