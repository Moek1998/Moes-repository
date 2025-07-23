#!/bin/bash

# Context7 MCP Server Control Script
# This script helps manage Context7 servers for all coding agents

AGENTS_DIR="/workspace/mcp-agents"

function start_agent() {
    local agent_num=$1
    local agent_dir="${AGENTS_DIR}/coding-agent-${agent_num}"
    
    if [ -d "$agent_dir" ]; then
        echo "Starting Context7 for Coding Agent ${agent_num}..."
        cd "$agent_dir/context7"
        
        # Start in background with HTTP transport on different ports
        case $agent_num in
            1) node dist/index.js --transport http --port 3001 > "${agent_dir}/context7.log" 2>&1 & ;;
            2) node dist/index.js --transport http --port 3002 > "${agent_dir}/context7.log" 2>&1 & ;;
            3) node dist/index.js --transport http --port 3003 > "${agent_dir}/context7.log" 2>&1 & ;;
        esac
        
        echo $! > "${agent_dir}/context7.pid"
        echo "Started Context7 for Agent ${agent_num} (PID: $!)"
    else
        echo "Agent directory not found: $agent_dir"
    fi
}

function stop_agent() {
    local agent_num=$1
    local agent_dir="${AGENTS_DIR}/coding-agent-${agent_num}"
    local pid_file="${agent_dir}/context7.pid"
    
    if [ -f "$pid_file" ]; then
        local pid=$(cat "$pid_file")
        if kill -0 $pid 2>/dev/null; then
            kill $pid
            rm "$pid_file"
            echo "Stopped Context7 for Agent ${agent_num}"
        else
            echo "Process not running for Agent ${agent_num}"
            rm "$pid_file"
        fi
    else
        echo "No PID file found for Agent ${agent_num}"
    fi
}

function status_agent() {
    local agent_num=$1
    local agent_dir="${AGENTS_DIR}/coding-agent-${agent_num}"
    local pid_file="${agent_dir}/context7.pid"
    
    if [ -f "$pid_file" ]; then
        local pid=$(cat "$pid_file")
        if kill -0 $pid 2>/dev/null; then
            echo "Context7 for Agent ${agent_num}: RUNNING (PID: $pid, Port: 300${agent_num})"
        else
            echo "Context7 for Agent ${agent_num}: NOT RUNNING (stale PID file)"
        fi
    else
        echo "Context7 for Agent ${agent_num}: NOT RUNNING"
    fi
}

case "$1" in
    start)
        if [ "$2" = "all" ]; then
            for i in 1 2 3; do
                start_agent $i
            done
        elif [[ "$2" =~ ^[1-3]$ ]]; then
            start_agent $2
        else
            echo "Usage: $0 start {all|1|2|3}"
        fi
        ;;
    stop)
        if [ "$2" = "all" ]; then
            for i in 1 2 3; do
                stop_agent $i
            done
        elif [[ "$2" =~ ^[1-3]$ ]]; then
            stop_agent $2
        else
            echo "Usage: $0 stop {all|1|2|3}"
        fi
        ;;
    status)
        echo "Context7 MCP Servers Status:"
        echo "============================"
        for i in 1 2 3; do
            status_agent $i
        done
        ;;
    restart)
        $0 stop ${2:-all}
        sleep 2
        $0 start ${2:-all}
        ;;
    test)
        # Test if servers are responsive
        echo "Testing Context7 servers..."
        for port in 3001 3002 3003; do
            echo -n "Testing port $port: "
            if curl -s -f http://localhost:$port/health >/dev/null 2>&1; then
                echo "OK"
            else
                echo "Not responding"
            fi
        done
        ;;
    *)
        echo "Context7 MCP Server Control"
        echo "Usage: $0 {start|stop|restart|status|test} [all|1|2|3]"
        echo ""
        echo "Examples:"
        echo "  $0 start all     - Start all Context7 servers"
        echo "  $0 start 1       - Start only Agent 1's server"
        echo "  $0 stop all      - Stop all servers"
        echo "  $0 status        - Show status of all servers"
        echo "  $0 test          - Test server connectivity"
        exit 1
        ;;
esac