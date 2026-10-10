# Status Finder

A lightweight Python script that checks whether hostnames listed in `subs.txt` respond over HTTP or HTTPS and records the results.

## What it does

For each non-empty line in `subs.txt`, `check_domains.py`:

1. Tries `http://<hostname>` first, then `https://<hostname>` if the first request raises a request exception.
2. Follows redirects and uses a 5-second request timeout.
3. Prints the first HTTP response status it receives.
4. Appends responsive URLs to `responses/<status-code>.txt`. Hostnames for which both requests fail are appended to `responses/dead.txt`.

The script creates the `responses/` directory automatically.

## Requirements

- Python 3
- `requests`

Install the dependency:

```bash
python3 -m pip install requests
```

## Usage

Create `subs.txt` in the project directory with one hostname per line:

```text
example.com
www.example.org
```

Run the script from that directory:

```bash
python3 check_domains.py
```

Example output:

```text
[200] http://example.com
[301] http://www.example.org
[Dead] unreachable.example
```

The exact status codes and results depend on the target hosts and network conditions.

## Output

| Path | Meaning |
| --- | --- |
| `responses/200.txt` | URLs that returned HTTP status 200 |
| `responses/<status-code>.txt` | URLs that returned the corresponding HTTP status |
| `responses/dead.txt` | Hostnames for which both HTTP and HTTPS requests raised request exceptions |

Results are appended, so repeated runs can add duplicate entries. Review or clear prior output files before starting a fresh collection.

## Limitations

- An HTTP response only indicates that a web endpoint responded; it does **not** establish domain-registration availability, DNS health, or overall application health.
- A non-2xx status such as 403 or 404 is still recorded as a response.
- The script does not perform WHOIS lookups or query DNS record types. Those capabilities are not implemented in the current code.
- A hostname is marked `Dead` when both requests fail; transient network errors, TLS problems, and timeouts can produce the same result.
- Use this tool only for hostnames you own or are authorized to assess.

## Scope

This is a basic HTTP/HTTPS responsiveness checker for domain-reconnaissance workflows, not a full domain availability or vulnerability scanner.
