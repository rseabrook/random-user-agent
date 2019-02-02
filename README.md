# Random User Agent

It is easy to find a list of user agent strings online. It is much harder to find a list of user agent strings that meet the requirements to be useful for web scraping. My requirements for a good list of user agent strings are:

- Targeted to a specific platform
- Representative of real web traffic
- Easily updated

[Intoli](), a data consulting agency, publishes [a list of user agent strings]() along with many useful properties based on web traffic to their own website that is updated daily. I built a super simple command-line utility based on their dataset that generates lists of user agent strings that meet the three requirements above.

## Installation

## Usage

The default command returns the single most common user agent across all platforms to stdout.

```
$ python random-user-agent.py
Mozilla/5.0 (iPhone; CPU iPhone OS 12_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1
```

### Getting multiple user agent strings

Use the `--count` (`-n`) option to specify the number of user agents to return.

```
$ python random-user-agent.py --count 3
Mozilla/5.0 (iPhone; CPU iPhone OS 12_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
```

### Getting user agents for a specific platform

Use the `--device-type` (`-d`) option to specify `desktop`, `tablet`, or `mobile`.

```
$ python random-user-agent.py --device-type desktop
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
```

### Saving the output to a file

Use the `--output` (`-o`) option to specify a filename to save the output.

```
$ python random-user-agent.py --output user_agents.txt
```

### Combining options

Combining options works exactly how you would expect. If you want a list of ten user agents used by desktop browsers and saved to `user-agents.txt`, you can do that this way:

```
python random-user-agent.py --count 10 --device-type desktop --output user-agents.txt
```