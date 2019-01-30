import json

import click

@click.command()
@click.option('-n', '--count', type=int, default=1, help='Number of user-agents')
@click.option('-d', '--device-type', type=click.Choice(['desktop', 'tablet', 'mobile']))
@click.option('-o', '--output', type=click.File('w'), default='-')
def main(count, device_type, output):
    # TODO: download and unzip user-agents.json if it doesn't exist
    with open('user-agents.json', 'r') as f:
        user_agents = json.load(f)
    
    returned = 0
    for user_agent in user_agents:
        if not device_type or user_agent['deviceCategory'] == device_type:
            output.write(user_agent['userAgent'] + '\n')
            returned += 1
        if returned >= count: break

if __name__ == '__main__':
    main()