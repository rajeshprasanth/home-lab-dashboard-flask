#!/bin/bash

# Function to start the dashboard

ip_address=10.0.0.90
port=5000
engine=gunicorn

start() {
    echo "Starting dashboard..."
    python3 dashboard.py --ip $ip_address --port $port $engine &
    pid_num=$!
    echo $pid_num > pid_file
    echo "pid written to pid_file"
}

# Function to stop the dashboard
stop() {
    echo "Stopping dashboard..."
    pid_to_kill=$(cat pid_file)
    kill -9 $pid_to_kill
    rm -rf pid_file
}

# Function to restart the dashboard
restart() {
    stop
    start
}

# Parse command line arguments
case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
        ;;
esac

exit 0
