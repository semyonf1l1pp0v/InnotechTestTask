import sqlite3

connection = sqlite3.connect("app/databases/AppSec.db")
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS APPSEC')
connection.commit()

# Создаем таблицу

cursor.execute('''
CREATE TABLE IF NOT EXISTS APPSEC (
acronym text,
description text
)
''')
connection.commit()

cursor.execute('''
INSERT INTO APPSEC VALUES (?, ?)
''', ["SAST", "SAST helps detect code flaws by analyzing the application source files for root causes. It enables "
              "comparing static analysis scan results with real-time solutions to quickly detect security problems, "
              "decrease the mean time to repair (MTTR), and troubleshoot collaboratively."])
connection.commit()
cursor.execute('''
INSERT INTO APPSEC VALUES (?, ?)
''', ["DAST", "DAST is a proactive testing approach that simulates security breaches on a running web application to "
              "identify exploitable flaws. These tools evaluate applications in production to help detect runtime or "
              "environment-related errors."])
connection.commit()
cursor.execute('''
INSERT INTO APPSEC VALUES (?, ?)
''', ["IAST", "IAST utilizes SAST and DAST elements, performing analysis in real-time or at any SDLC phase from within "
              "the application. IAST tools get access to the application's code and components, which means the tools "
              "achieve the in-depth access needed to produce accurate results."])
connection.commit()
cursor.execute('''
INSERT INTO APPSEC VALUES (?, ?)
''', ["RASP", "RASP tools work within the application to provide continuous security checks and automatically respond "
              "to possible breaches. Common responses include alerting IT teams and terminating a suspicious session."])
connection.commit()
cursor.execute('''
INSERT INTO APPSEC VALUES (?, ?)
''', ["MAST", "MAST tools test the security of mobile applications using various techniques, such as performing static "
              "and dynamic analysis and investigating forensic data gathered by mobile applications. MAST tools help "
              "identify mobile-specific issues and security vulnerabilities, such as malicious WiFi networks, "
              "jailbreaking, and data leakage from mobile devices."])
connection.commit()
cursor.execute('''
INSERT INTO APPSEC VALUES (?, ?)
''', ["WAF", "A WAF solution monitors and filters all HTTP traffic passing between the Internet and a web application. "
             "These solutions do not cover all threats. Rather, WAFs work as part of a security stack that provides a "
             "holistic defense against the relevant attack vectors. WAF works as a protocol layer seven defense when "
             "applied as part of the open systems interconnection (OSI) model. It helps protect web applications "
             "against various attacks, including cross-site-scripting (XSS), SQL injection (SQLi), file inclusion, "
             "and cross-site forgery (CSRF)."])
cursor.execute('''
INSERT INTO APPSEC VALUES (?, ?)
''', ["CNAPP", "A cloud native application protection platform (CNAPP) centralizes the control of all tools used to "
               "protect cloud native applications. It unifies various technologies, such as cloud security posture "
               "management (CSPM) and cloud workload protection platform (CWPP), identity entitlement management, "
               "automation and orchestration security for container orchestration platforms like Kubernetes, "
               "and API discovery and protection."])

connection.commit()

connection.close()
