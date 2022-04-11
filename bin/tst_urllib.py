#!/usr/bin/env python3

from urllib.parse import urlparse, parse_qs

url = urlparse('/api/v1/some-request?a=bad&d=fast#xxx')

print(url)

print(f"       Query path: {url.path}")
print(f"  Query component: {url.query}")
print(f"       Query args: {parse_qs(url.query)}")
print(f"   Query fragment: {url.fragment}")


