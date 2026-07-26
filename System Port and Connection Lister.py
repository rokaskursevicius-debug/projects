import socket
import psutil

def get_process_name(pid):
    try:
        process = psutil.Process(pid)
        return process.name()
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        return "Unknown"

def scan_network_connections():
    print("Scanning network connections...")
    print(f"{'Local Address':<30} | {'Remote Address':<30} | {'Status':<15} | {'Process Name':<20} | {'PID'}")
    connections = psutil.net_connections(kind='inet')
    count = 0 
    for conn in connections:
        if conn.pid:
            process_name = get_process_name(conn.pid)
            process_info = f"{process_name} (PID: {conn.pid})"
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "Listening"
            status = conn.status
            print(f"{laddr:<30} | {raddr:<30} | {status:<15} | {process_info}")
            count += 1
    print("-" * 85)
    print(f"Total connections found: {count}")
if __name__ == "__main__":
    scan_network_connections()