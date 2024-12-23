import subprocess
import argparse
from pathlib import Path
import venv
import os

# Configuration information and API
class Config:
    client_bind: str = "0.0.0.0"
    client_port: str = "8791"
    client_name: str = "byod--client"
    client_dir:  str = "src/client"

    server_bind: str = "0.0.0.0"
    server_port: str = "4971"
    server_name: str = "byod--server"
    server_dir:  str = "src/server"

    @classmethod
    def create_parser(cls):
        parser = argparse.ArgumentParser(description='Helper script for the project')
        parser.add_argument(
            '--run-client',
            action='store_true',
            help='run the web client',
        )
        
        # parser.add_argument(
        #     '--port',
        #     type=str,
        #     default=None,
        #     help='specify the port you wish to run this on'
        # )
        
        parser.add_argument(
            '--server-env',
            action='store_true',
            help='setup the environment for the server',
        )
        
        parser.add_argument(
            '--run-server',
            action='store_true',
            help='run the backend service',
        )

        return parser

    @classmethod
    def source(cls, script_path):
        # Use Bash to source the script and print the environment
        command = f"source {script_path} && env"
        proc = subprocess.Popen(
            command, shell=True, executable="/bin/bash", stdout=subprocess.PIPE
        )
        env_output, _ = proc.communicate()

        # Parse the environment variables
        env = {}
        for line in env_output.decode().splitlines():
            key, _, value = line.partition("=")
            env[key] = value

        return env

class TmuxSession:
    name: str = ''

    def __init__(self, name:str):
        self.name = name
        command = ['tmux', 'new-session', '-A', '-d', '-t', name]
        subprocess.run(command)

    def send_command(self, command:str):
        subprocess.run(['tmux', 'send-keys', '-t', self.name, command, 'C-m'])

    def kill(self):
        subprocess.run(['tmux', 'kill-session', '-t', self.name])

class Tmux:
    sessions = {}

    @classmethod
    def new_session(cls, name:str) -> TmuxSession:
        session = TmuxSession(name)
        cls.sessions[name] = session
        return session

    @classmethod
    def send_command(cls, session_name: str, command: str):
        cls.sessions[session_name].send_command(command)

    @classmethod
    def kill_session(cls, name:str):
        cls.sessions[session_name]

# API For interacting with the web client
class Client:
    port: str = Config.client_port
    name: str = Config.client_name
   
    @classmethod
    def __new__(cls, port:str=Config.client_port, name:str=Config.client_name):
        cls.port = port
        cls.name = name

    @classmethod
    def run(cls):
        print(f'Running client on port {cls.port}')
        Tmux.new_session(Config.client_name)
        
        cls.initialize_env()
        cls.start()

    @classmethod
    def setup_env(cls):
        print('Setting up client environment')
        command = f'cd {Config.client_dir}'
        Tmux.send_command(Config.client_name, command)
        Tmux.send_command(Config.client_name, 'npm install')

    @classmethod
    def initialize_env(cls):
        print('Initializing client environment')
        Tmux.send_command(Config.client_name, f'cd {Config.client_dir}')

    @classmethod
    def start(cls):
        print('Starting client...')
        Tmux.send_command(Config.client_name, f'gatsby develop --host {Config.client_bind} --port {Config.client_port}')

class Server:
    port: str = Config.server_port
    name: str = Config.server_name

    @classmethod
    def __new__(cls, port:str=Config.client_port, name:str=Config.client_name):
        cls.port = port
        cls.name = name
    
    @classmethod
    def run(cls):
        print(f'Running server on port {cls.port}')
        cls.initialize_env()
        Tmux.new_session(Config.server_name)
        
        cls.start()

    @classmethod
    def initialize_env(cls):
        path = Path('src/server/venv')
        if path.exists():
            print('Virtual Env already exists. Aborting.')
            return
        print('Initializing server environment')
        
        # Venv
        venv_dir = f'{Config.server_dir}/venv'
        venv.create(venv_dir, with_pip=True)
        if os.name == "nt":  # Windows
            activate_script = os.path.join(venv_dir, "Scripts", "activate_this.py")
        else:  # Unix or MacOS
            activate_script = os.path.join(venv_dir, "bin", "activate")
        Config.source(activate_script)

        pip_executable = os.path.join(venv_dir, "bin", "pip") if os.name != "nt" else os.path.join(venv_dir, "Scripts", "pip.exe")
        subprocess.run([pip_executable, "install", '-r', f'{Config.server_dir}/requirements.txt'])

        # Install deps
        # command = ['python', '-m', 'pip', 'install', '-r', f'{Config.server_dir}/requirements.txt']
        # subprocess.run(command)

    @classmethod
    def start(cls):
        print('Starting server...')
        Tmux.send_command(Config.server_name, f'BYOD_SERVER_PORT={Config.server_port}')
        Tmux.send_command(Config.server_name, f'BYOD_SERVER_BIND={Config.server_bind}')
        Tmux.send_command(Config.server_name, f'cd src/server')
        Tmux.send_command(Config.server_name, f'python -m server')


if __name__ == "__main__":
    parser = Config.create_parser()
    args = parser.parse_args()

    if args.run_client:
        Client.run()
    elif args.run_server:
        Server.run()
    

    pass
