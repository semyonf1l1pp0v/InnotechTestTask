from typing import Optional

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import bcrypt

users_db = {"admin":
                {"username": "admin",
                 "hashed_password": bcrypt.hashpw(password="admin".encode(), salt=bcrypt.gensalt())
                 }
            }

app = FastAPI()


def open_html(filename):
    with open(filename) as file:
        html_response = file.read()
    return HTMLResponse(content=html_response)


@app.get("/", response_class=HTMLResponse)
def homepage():
    return open_html("homepage.html")


@app.get("/login", response_class=HTMLResponse)
def authpage():
    return open_html("authform.html")


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username == users_db["admin"]["username"] and bcrypt.checkpw(password.encode(),
                                                                    users_db["admin"]["hashed_password"]):
        return open_html("correct_cred.html")
    else:
        return open_html("incorrect_cred.html")


appsec_practices = {
    "SAST": "SAST helps detect code flaws by analyzing the application source files for root causes. It enables "
            "comparing static analysis scan results with real-time solutions to quickly detect security problems, "
            "decrease the mean time to repair (MTTR), and troubleshoot collaboratively.",
    "DAST": "DAST is a proactive testing approach that simulates security breaches on a running web application to "
            "identify exploitable flaws. These tools evaluate applications in production to help detect runtime or "
            "environment-related errors.",
    "IAST": "IAST utilizes SAST and DAST elements, performing analysis in real-time or at any SDLC phase from within "
            "the application. IAST tools get access to the application's code and components, which means the tools "
            "achieve the in-depth access needed to produce accurate results.",
    "RASP": "RASP tools work within the application to provide continuous security checks and automatically respond "
            "to possible breaches. Common responses include alerting IT teams and terminating a suspicious session.",
    "MAST": "MAST tools test the security of mobile applications using various techniques, such as performing static "
            "and dynamic analysis and investigating forensic data gathered by mobile applications. MAST tools help "
            "identify mobile-specific issues and security vulnerabilities, such as malicious WiFi networks, "
            "jailbreaking, and data leakage from mobile devices.",
    "WAF": "A WAF solution monitors and filters all HTTP traffic passing between the Internet and a web application. "
           "These solutions do not cover all threats. Rather, WAFs work as part of a security stack that provides a "
           "holistic defense against the relevant attack vectors. WAF works as a protocol layer seven defense when "
           "applied as part of the open systems interconnection (OSI) model. It helps protect web applications "
           "against various attacks, including cross-site-scripting (XSS), SQL injection (SQLi), file inclusion, "
           "and cross-site forgery (CSRF).",
    "CNAPP": "A cloud native application protection platform (CNAPP) centralizes the control of all tools used to "
             "protect cloud native applications. It unifies various technologies, such as cloud security posture "
             "management (CSPM) and cloud workload protection platform (CWPP), identity entitlement management, "
             "automation and orchestration security for container orchestration platforms like Kubernetes, "
             "and API discovery and protection."
}


@app.get("/appsec")
def get_practice(key: Optional[str] = None):
    if not key or key == "practice_main":
        return open_html("appsec.html")
    for el in appsec_practices.items():
        if el[0].lower() == key.lower().replace("practice_", ""):
            return {el[0]: el[1]}
    return {"error": "key not found"}
