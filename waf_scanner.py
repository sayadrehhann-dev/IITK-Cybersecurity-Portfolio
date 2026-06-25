import re

# 1. Simulate a list of incoming web requests hitting a website
web_traffic_logs = [
    "GET /index.html HTTP/1.1 (Normal User access)",
    "GET /login.php?user=admin' OR 1=1-- HTTP/1.1 (SQL Injection Attempt)",
    "GET /about.html HTTP/1.1 (Normal User access)",
    "GET /profile.php?name=<script>alert('Hacked')</script> HTTP/1.1 (XSS Attack Attempt)"
]

# 2. Define standard security signatures to spot hacker patterns
sql_injection_pattern = r"['\"]|OR|UNION|SELECT"
xss_pattern = r"<script>|alert\(|<\/script>"

print("[*] Launching Web Application Firewall (WAF) Simulation...\n")

# 3. Scan the traffic line by line
for log in web_traffic_logs:
    print(f"Analyzing Log Line: {log}")
    
    # Check for SQL Injection
    if re.search(sql_injection_pattern, log, re.IGNORECASE) and "Normal" not in log:
        print("  ❌ [BLOCK] High Risk: SQL Injection attack pattern detected! Malicious database query blocked.")
    # Check for Cross-Site Scripting (XSS)
    elif re.search(xss_pattern, log, re.IGNORECASE):
        print("  ❌ [BLOCK] High Risk: Cross-Site Scripting (XSS) detected! Malicious script execution blocked.")
    else:
        print("  ✅ [PASS] Request is clean and safe.")
    print("-" * 50)
