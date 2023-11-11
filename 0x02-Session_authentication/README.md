<h1 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 36px;">0x02. Session authentication</h1>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(219, 62, 62);font-size: 14px;">Back-end</span></strong><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(219, 62, 62);font-size: 14px;">Authentification</span></strong></div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <ul style="font-size: 11px;">
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">By: Guillaume, CTO at Holberton School</li>
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">Weight: 1</li>
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">Ongoing second chance project - started <span title=""><span style="border-bottom: 0.5px dashed currentcolor;">Nov 8, 2023 6:00 AM</span></span>, must end by <span title=""><span style="border-bottom: 0.5px dashed currentcolor;">Nov 12, 2023 6:00 AM</span></span></li>
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">An auto review will be launched at the deadline</li>
    </ul>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);font-size: 14px;border: 1px solid rgb(238, 238, 238);">
    <h4 style="color: inherit;font-size: 18px;">In a nutshell&hellip;</h4>
    <ul>
        <li><strong><strong>Auto QA review:</strong></strong> 0.0/135 mandatory &amp; 0.0/46 optional</li>
        <li><strong><strong>Altogether:</strong></strong>&nbsp; <strong><strong>0.0%</strong></strong>
            <ul>
                <li>Mandatory: 0.0%</li>
                <li>Optional: 0.0%</li>
                <li>Calculation: &nbsp;0.0% + (0.0% * 0.0%) &nbsp;== <strong><strong>0.0%</strong></strong></li>
            </ul>
        </li>
    </ul>
</div>
<div style="text-align: start;color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);font-size: 14px;border: 1px solid rgb(221, 221, 221);">
    <div>
        <h2 style="color: inherit;font-size: 30px;">Background Context</h2>
        <p>In this project, you will implement a <strong><strong>Session Authentication</strong></strong>. You are not allowed to install any other module.</p>
        <p>In the industry, you should <strong><strong>not</strong></strong> implement your own Session authentication system and use a module or framework that doing it for you (like in Python-Flask: <a href="https://intranet.alxswe.com/rltoken/_ZTQTaMKjx1S_xATshexkA" title="Flask-HTTPAuth" target="_blank" style="color: transparent;">Flask-HTTPAuth</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.</p>
        <h2 style="color: inherit;font-size: 30px;">Resources</h2>
        <p><strong><strong>Read or watch</strong></strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/oofk0VhuS0ZFZTNTVrQeaQ" title="REST API Authentication Mechanisms - Only the session auth part" target="_blank" style="color: transparent;">REST API Authentication Mechanisms - Only the session auth part</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/peLV8xuJ4PDJMOVFqk-d2g" title="HTTP Cookie" target="_blank" style="color: transparent;">HTTP Cookie</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/AI1tFR5XriGfR8Tz7YTYQA" title="Flask" target="_blank" style="color: transparent;">Flask</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/QYfI5oW6OHUmHDzwKV1Qsw" title="Flask Cookie" target="_blank" style="color: transparent;">Flask Cookie</a></li>
        </ul>
        <h2 style="color: inherit;font-size: 30px;">Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to <a href="https://intranet.alxswe.com/rltoken/uWXp4VcY3Dd9UzTtc9N5_A" title="explain to anyone" target="_blank" style="color: transparent;">explain to anyone</a>, <strong><strong>without the help of Google</strong></strong>:</p>
        <h3 style="color: inherit;font-size: 24px;">General</h3>
        <ul>
            <li>What authentication means</li>
            <li>What session authentication means</li>
            <li>What Cookies are</li>
            <li>How to send Cookies</li>
            <li>How to parse Cookies</li>
        </ul>
        <h2 style="color: inherit;font-size: 30px;">Requirements</h2>
        <h3 style="color: inherit;font-size: 24px;">Python Scripts</h3>
        <ul>
            <li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">python3</code> (version 3.7)</li>
            <li>All your files should end with a new line</li>
            <li>The first line of all your files should be exactly <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">#!/usr/bin/env python3</code></li>
            <li>A <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>Your code should use the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">pycodestyle</code> style (version 2.5)</li>
            <li>All your files must be executable</li>
            <li>The length of your files will be tested using <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">wc</code></li>
            <li>All your modules should have a documentation (<code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;</code>)</li>
            <li>All your classes should have a documentation (<code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&apos;</code>)</li>
            <li>All your functions (inside and outside a class) should have a documentation (<code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">python3 -c &apos;print(__import__(&quot;my_module&quot;).my_function.__doc__)&apos;</code> and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&apos;</code>)</li>
            <li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
        </ul>
    </div>
</div>
<h2 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 30px;">Tasks</h2>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">0. Et moi et moi et moi!</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Copy all your work of the <strong><strong>0x06. Basic authentication</strong></strong> project in this new folder.</p>
            <p>In this version, you implemented a <strong><strong>Basic authentication</strong></strong> for giving you access to all User endpoints:</p>
            <ul>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">GET /api/v1/users</code></li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">POST /api/v1/users</code></li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">GET /api/v1/users/&lt;user_id&gt;</code></li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">PUT /api/v1/users/&lt;user_id&gt;</code></li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">DELETE /api/v1/users/&lt;user_id&gt;</code></li>
            </ul>
            <p>Now, you will add a new endpoint: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">GET /users/me</code> to retrieve the authenticated <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> object.</p>
            <ul>
                <li>Copy folders <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">models</code> and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api</code> from the previous project <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x06. Basic authentication</code></li>
                <li>Please make sure all mandatory tasks of this previous project are done at 100% because this project (and the rest of this track) will be based on it.</li>
                <li>Update <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">@app.before_request</code> in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/app.py</code>:<ul>
                        <li>Assign the result of <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth.current_user(request)</code> to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">request.current_user</code></li>
                    </ul>
                </li>
                <li>Update method for the route <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">GET /api/v1/users/&lt;user_id&gt;</code> in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/views/users.py</code>:<ul>
                        <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">&lt;user_id&gt;</code> is equal to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">me</code> and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">request.current_user</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">abort(404)</code></li>
                        <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">&lt;user_id&gt;</code> is equal to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">me</code> and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">request.current_user</code> is not <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>: return the authenticated <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> in a JSON response (like a normal case of <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">GET /api/v1/users/&lt;user_id&gt;</code> where <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">&lt;user_id&gt;</code> is a valid <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> ID)</li>
                        <li>Otherwise, keep the same behavior</li>
                    </ul>
                </li>
            </ul>
            <p>In the first terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat main_0.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 0
&quot;&quot;&quot;
import base64
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

&quot;&quot;&quot; Create a user test &quot;&quot;&quot;
user_email = &quot;bob@hbtn.io&quot;
user_clear_pwd = &quot;H0lbertonSchool98!&quot;

user = User()
user.email = user_email
user.password = user_clear_pwd
print(&quot;New user: {}&quot;.format(user.id))
user.save()

basic_clear = &quot;{}:{}&quot;.format(user_email, user_clear_pwd)
print(&quot;Basic Base64: {}&quot;.format(base64.b64encode(basic_clear.encode(&apos;utf-8&apos;)).decode(&quot;utf-8&quot;)))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth ./main_0.py 
New user: 9375973a-68c7-46aa-b135-29f79e837495
Basic Base64: Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In a second terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/status&quot;
{
  &quot;status&quot;: &quot;OK&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot;
{
  &quot;error&quot;: &quot;Unauthorized&quot;
}
bob@dylan:~$ 
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot; -H &quot;Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh&quot;
[
  {
    &quot;created_at&quot;: &quot;2017-09-25 01:55:17&quot;, 
    &quot;email&quot;: &quot;bob@hbtn.io&quot;, 
    &quot;first_name&quot;: null, 
    &quot;id&quot;: &quot;9375973a-68c7-46aa-b135-29f79e837495&quot;, 
    &quot;last_name&quot;: null, 
    &quot;updated_at&quot;: &quot;2017-09-25 01:55:17&quot;
  }
]
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; -H &quot;Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh&quot;
{
  &quot;created_at&quot;: &quot;2017-09-25 01:55:17&quot;, 
  &quot;email&quot;: &quot;bob@hbtn.io&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;9375973a-68c7-46aa-b135-29f79e837495&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-09-25 01:55:17&quot;
}
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x02-Session_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/app.py, api/v1/views/users.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">QA Review</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">1. Empty session</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Create a class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SessionAuth</code> that inherits from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Auth</code>. For the moment this class will be empty. It&rsquo;s the first step for creating a new authentication mechanism:</p>
            <ul>
                <li>validate if everything inherits correctly without any overloading</li>
                <li>validate the &ldquo;switch&rdquo; by using environment variables</li>
            </ul>
            <p>Update <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/app.py</code> for using <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SessionAuth</code> instance for the variable <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth</code> depending of the value of the environment variable <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">AUTH_TYPE</code>, If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">AUTH_TYPE</code> is equal to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">session_auth</code>:</p>
            <ul>
                <li>import <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SessionAuth</code> from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api.v1.auth.session_auth</code></li>
                <li>create an instance of <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SessionAuth</code> and assign it to the variable <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth</code></li>
            </ul>
            <p>Otherwise, keep the previous mechanism.</p>
            <p>In the first terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In a second terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/status&quot;
{
  &quot;status&quot;: &quot;OK&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/status/&quot;
{
  &quot;status&quot;: &quot;OK&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot;
{
  &quot;error&quot;: &quot;Unauthorized&quot;
}
bob@dylan:~$ 
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot; -H &quot;Authorization: Test&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x02-Session_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/session_auth.py, api/v1/app.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">QA Review</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">2. Create a session</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Update <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SessionAuth</code> class:</p>
            <ul>
                <li>Create a class attribute <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id_by_session_id</code> initialized by an empty dictionary</li>
                <li>Create an instance method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def create_session(self, user_id: str = None) -&gt; str:</code> that creates a Session ID for a <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id</code>:<ul>
                        <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code></li>
                        <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id</code> is not a string</li>
                        <li>Otherwise:<ul>
                                <li>Generate a Session ID using <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">uuid</code> module and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">uuid4()</code> like <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">id</code> in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Base</code></li>
                                <li>Use this Session ID as key of the dictionary <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id_by_session_id</code> - the value for this key must be <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id</code></li>
                                <li>Return the Session ID</li>
                            </ul>
                        </li>
                        <li>The same <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id</code> can have multiple Session ID - indeed, the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id</code> is the value in the dictionary <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id_by_session_id</code></li>
                    </ul>
                </li>
            </ul>
            <p>Now you an &ldquo;in-memory&rdquo; Session ID storing. You will be able to retrieve an <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> id based on a Session ID.</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat  main_1.py 
#!/usr/bin/env python3
&quot;&quot;&quot; Main 1
&quot;&quot;&quot;
from api.v1.auth.session_auth import SessionAuth

sa = SessionAuth()

print(&quot;{}: {}&quot;.format(type(sa.user_id_by_session_id), sa.user_id_by_session_id))

user_id = None
session = sa.create_session(user_id)
print(&quot;{} =&gt; {}: {}&quot;.format(user_id, session, sa.user_id_by_session_id))

user_id = 89
session = sa.create_session(user_id)
print(&quot;{} =&gt; {}: {}&quot;.format(user_id, session, sa.user_id_by_session_id))

user_id = &quot;abcde&quot;
session = sa.create_session(user_id)
print(&quot;{} =&gt; {}: {}&quot;.format(user_id, session, sa.user_id_by_session_id))

user_id = &quot;fghij&quot;
session = sa.create_session(user_id)
print(&quot;{} =&gt; {}: {}&quot;.format(user_id, session, sa.user_id_by_session_id))

user_id = &quot;abcde&quot;
session = sa.create_session(user_id)
print(&quot;{} =&gt; {}: {}&quot;.format(user_id, session, sa.user_id_by_session_id))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_1.py 
&lt;class &apos;dict&apos;&gt;: {}
None =&gt; None: {}
89 =&gt; None: {}
abcde =&gt; 61997a1b-3f8a-4b0f-87f6-19d5cafee63f: {&apos;61997a1b-3f8a-4b0f-87f6-19d5cafee63f&apos;: &apos;abcde&apos;}
fghij =&gt; 69e45c25-ec89-4563-86ab-bc192dcc3b4f: {&apos;61997a1b-3f8a-4b0f-87f6-19d5cafee63f&apos;: &apos;abcde&apos;, &apos;69e45c25-ec89-4563-86ab-bc192dcc3b4f&apos;: &apos;fghij&apos;}
abcde =&gt; 02079cb4-6847-48aa-924e-0514d82a43f4: {&apos;61997a1b-3f8a-4b0f-87f6-19d5cafee63f&apos;: &apos;abcde&apos;, &apos;02079cb4-6847-48aa-924e-0514d82a43f4&apos;: &apos;abcde&apos;, &apos;69e45c25-ec89-4563-86ab-bc192dcc3b4f&apos;: &apos;fghij&apos;}
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x02-Session_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/session_auth.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">QA Review</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">3. User ID for Session ID</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Update <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SessionAuth</code> class:</p>
            <p>Create an instance method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def user_id_for_session_id(self, session_id: str = None) -&gt; str:</code> that returns a <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> ID based on a Session ID:</p>
            <ul>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">session_id</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code></li>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">session_id</code> is not a string</li>
                <li>Return the value (the User ID) for the key <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">session_id</code> in the dictionary <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id_by_session_id</code>.</li>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">.get()</code> built-in for accessing in a dictionary a value based on key</li>
            </ul>
            <p>Now you have 2 methods (<code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">create_session</code> and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id_for_session_id</code>) for storing and retrieving a link between a <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> ID and a Session ID.</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat main_2.py 
#!/usr/bin/env python3
&quot;&quot;&quot; Main 2
&quot;&quot;&quot;
from api.v1.auth.session_auth import SessionAuth

sa = SessionAuth()

user_id_1 = &quot;abcde&quot;
session_1 = sa.create_session(user_id_1)
print(&quot;{} =&gt; {}: {}&quot;.format(user_id_1, session_1, sa.user_id_by_session_id))

user_id_2 = &quot;fghij&quot;
session_2 = sa.create_session(user_id_2)
print(&quot;{} =&gt; {}: {}&quot;.format(user_id_2, session_2, sa.user_id_by_session_id))

print(&quot;---&quot;)

tmp_session_id = None
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print(&quot;{} =&gt; {}&quot;.format(tmp_session_id, tmp_user_id))

tmp_session_id = 89
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print(&quot;{} =&gt; {}&quot;.format(tmp_session_id, tmp_user_id))

tmp_session_id = &quot;doesntexist&quot;
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print(&quot;{} =&gt; {}&quot;.format(tmp_session_id, tmp_user_id))

print(&quot;---&quot;)

tmp_session_id = session_1
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print(&quot;{} =&gt; {}&quot;.format(tmp_session_id, tmp_user_id))

tmp_session_id = session_2
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print(&quot;{} =&gt; {}&quot;.format(tmp_session_id, tmp_user_id))

print(&quot;---&quot;)

session_1_bis = sa.create_session(user_id_1)
print(&quot;{} =&gt; {}: {}&quot;.format(user_id_1, session_1_bis, sa.user_id_by_session_id))

tmp_user_id = sa.user_id_for_session_id(session_1_bis)
print(&quot;{} =&gt; {}&quot;.format(session_1_bis, tmp_user_id))

tmp_user_id = sa.user_id_for_session_id(session_1)
print(&quot;{} =&gt; {}&quot;.format(session_1, tmp_user_id))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_2.py 
abcde =&gt; 8647f981-f503-4638-af23-7bb4a9e4b53f: {&apos;8647f981-f503-4638-af23-7bb4a9e4b53f&apos;: &apos;abcde&apos;}
fghij =&gt; a159ee3f-214e-4e91-9546-ca3ce873e975: {&apos;a159ee3f-214e-4e91-9546-ca3ce873e975&apos;: &apos;fghij&apos;, &apos;8647f981-f503-4638-af23-7bb4a9e4b53f&apos;: &apos;abcde&apos;}
---
None =&gt; None
89 =&gt; None
doesntexist =&gt; None
---
8647f981-f503-4638-af23-7bb4a9e4b53f =&gt; abcde
a159ee3f-214e-4e91-9546-ca3ce873e975 =&gt; fghij
---
abcde =&gt; 5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee: {&apos;a159ee3f-214e-4e91-9546-ca3ce873e975&apos;: &apos;fghij&apos;, &apos;8647f981-f503-4638-af23-7bb4a9e4b53f&apos;: &apos;abcde&apos;, &apos;5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee&apos;: &apos;abcde&apos;}
5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee =&gt; abcde
8647f981-f503-4638-af23-7bb4a9e4b53f =&gt; abcde
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x02-Session_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/session_auth.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">QA Review</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">4. Session cookie</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Update <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/auth.py</code> by adding the method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def session_cookie(self, request=None):</code> that returns a cookie value from a request:</p>
            <ul>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">request</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code></li>
                <li>Return the value of the cookie named <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">_my_session_id</code> from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">request</code> - the name of the cookie must be defined by the environment variable <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SESSION_NAME</code></li>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">.get()</code> built-in for accessing the cookie in the request cookies dictionary</li>
                <li>You must use the environment variable <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SESSION_NAME</code> to define the name of the cookie used for the Session ID</li>
            </ul>
            <p>In the first terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat main_3.py
#!/usr/bin/env python3
&quot;&quot;&quot; Cookie server
&quot;&quot;&quot;
from flask import Flask, request
from api.v1.auth.auth import Auth

auth = Auth()

app = Flask(__name__)

@app.route(&apos;/&apos;, methods=[&apos;GET&apos;], strict_slashes=False)
def root_path():
    &quot;&quot;&quot; Root path
    &quot;&quot;&quot;
    return &quot;Cookie value: {}\n&quot;.format(auth.session_cookie(request))

if __name__ == &quot;__main__&quot;:
    app.run(host=&quot;0.0.0.0&quot;, port=&quot;5000&quot;)

bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_3.py 
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In a second terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ curl &quot;http://0.0.0.0:5000&quot;
Cookie value: None
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000&quot; --cookie &quot;_my_session_id=Hello&quot;
Cookie value: Hello
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000&quot; --cookie &quot;_my_session_id=C is fun&quot;
Cookie value: C is fun
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000&quot; --cookie &quot;_my_session_id_fake&quot;
Cookie value: None
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x02-Session_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/auth.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">QA Review</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">5. Before request</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Update the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">@app.before_request</code> method in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/app.py</code>:</p>
            <ul>
                <li>Add the URL path <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">/api/v1/auth_session/login/</code> in the list of excluded paths of the method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">require_auth</code> - this route doesn&rsquo;t exist yet but it should be accessible outside authentication</li>
                <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth.authorization_header(request)</code> and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth.session_cookie(request)</code> return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>, <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">abort(401)</code></li>
            </ul>
            <p>In the first terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In a second terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/status&quot;
{
  &quot;status&quot;: &quot;OK&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; # not found but not &quot;blocked&quot; by an authentication system
{
  &quot;error&quot;: &quot;Not found&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot;
{
  &quot;error&quot;: &quot;Unauthorized&quot;
}
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; -H &quot;Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh&quot; # Won&apos;t work because the environment variable AUTH_TYPE is equal to &quot;session_auth&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; --cookie &quot;_my_session_id=5535d4d7-3d77-4d06-8281-495dc3acfe76&quot; # Won&apos;t work because no user is linked to this Session ID
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x02-Session_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/app.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">QA Review</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">6. Use Session ID for identifying a User</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Update <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SessionAuth</code> class:</p>
            <p>Create an instance method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def current_user(self, request=None):</code> (overload) that returns a <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> instance based on a cookie value:</p>
            <ul>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.session_cookie(...)</code> and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.user_id_for_session_id(...)</code> to return the User ID based on the cookie <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">_my_session_id</code></li>
                <li>By using this User ID, you will be able to retrieve a <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> instance from the database - you can use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User.get(...)</code> for retrieving a <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> from the database.</li>
            </ul>
            <p>Now, you will be able to get a User based on his session ID.</p>
            <p>In the first terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat main_4.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 4
&quot;&quot;&quot;
from flask import Flask, request
from api.v1.auth.session_auth import SessionAuth
from models.user import User

&quot;&quot;&quot; Create a user test &quot;&quot;&quot;
user_email = &quot;bobsession@hbtn.io&quot;
user_clear_pwd = &quot;fake pwd&quot;

user = User()
user.email = user_email
user.password = user_clear_pwd
user.save()

&quot;&quot;&quot; Create a session ID &quot;&quot;&quot;
sa = SessionAuth()
session_id = sa.create_session(user.id)
print(&quot;User with ID: {} has a Session ID: {}&quot;.format(user.id, session_id))

&quot;&quot;&quot; Create a Flask app &quot;&quot;&quot;
app = Flask(__name__)

@app.route(&apos;/&apos;, methods=[&apos;GET&apos;], strict_slashes=False)
def root_path():
    &quot;&quot;&quot; Root path
    &quot;&quot;&quot;
    request_user = sa.current_user(request)
    if request_user is None:
        return &quot;No user found\n&quot;
    return &quot;User found: {}\n&quot;.format(request_user.id)

if __name__ == &quot;__main__&quot;:
    app.run(host=&quot;0.0.0.0&quot;, port=&quot;5000&quot;)

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_4.py
User with ID: cf3ddee1-ff24-49e4-a40b-2540333fe992 has a Session ID: 9d1648aa-da79-4692-8236-5f9d7f9e9485
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In a second terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ curl &quot;http://0.0.0.0:5000/&quot;
No user found
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/&quot; --cookie &quot;_my_session_id=Holberton&quot;
No user found
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/&quot; --cookie &quot;_my_session_id=9d1648aa-da79-4692-8236-5f9d7f9e9485&quot;
User found: cf3ddee1-ff24-49e4-a40b-2540333fe992
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x02-Session_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/session_auth.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">QA Review</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">7. New view for Session Authentication</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Create a new Flask view that handles all routes for the Session authentication.</p>
            <p>In the file <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/views/session_auth.py</code>, create a route <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">POST /auth_session/login</code> (= <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">POST /api/v1/auth_session/login</code>):</p>
            <ul>
                <li>Slash tolerant (<code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">/auth_session/login</code> == <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">/auth_session/login/</code>)</li>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">request.form.get()</code> to retrieve <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">email</code> and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">password</code> parameters</li>
                <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">email</code> is missing or empty, return the JSON <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">{ &quot;error&quot;: &quot;email missing&quot; }</code> with the status code <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">400</code></li>
                <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">password</code> is missing or empty, return the JSON <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">{ &quot;error&quot;: &quot;password missing&quot; }</code> with the status code <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">400</code></li>
                <li>Retrieve the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> instance based on the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">email</code> - you must use the class method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">search</code> of <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> (same as the one used for the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BasicAuth</code>)<ul>
                        <li>If no <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> found, return the JSON <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">{ &quot;error&quot;: &quot;no user found for this email&quot; }</code> with the status code <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">404</code></li>
                        <li>If the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">password</code> is not the one of the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> found, return the JSON <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">{ &quot;error&quot;: &quot;wrong password&quot; }</code> with the status code <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">401</code> - you must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">is_valid_password</code> from the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> instance</li>
                        <li>Otherwise, create a Session ID for the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code>ID:<ul>
                                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">from api.v1.app import auth</code> - <strong><strong>WARNING: please import it only where you need it</strong></strong> - not on top of the file (can generate circular import - and break first tasks of this project)</li>
                                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth.create_session(..)</code> for creating a Session ID</li>
                                <li>Return the dictionary representation of the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> - you must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">to_json()</code> method from User</li>
                                <li>You must set the cookie to the response - you must use the value of the environment variable <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SESSION_NAME</code> as cookie name - <a href="https://intranet.alxswe.com/rltoken/3WDlzYbVvdJJAf70IjWK6g" title="tip" target="_blank" style="color: transparent;">tip</a></li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
            <p>In the file <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/views/__init__.py</code>, you must add this new view at the end of the file.</p>
            <p>In the first terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In a second terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XGET
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;405 Method Not Allowed&lt;/title&gt;
&lt;h1&gt;Method Not Allowed&lt;/h1&gt;
&lt;p&gt;The method is not allowed for the requested URL.&lt;/p&gt;
bob@dylan:~$
bob@dylan:~$  curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XPOST
{
  &quot;error&quot;: &quot;email missing&quot;
}
bob@dylan:~$ 
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XPOST -d &quot;email=guillaume@hbtn.io&quot;
{
  &quot;error&quot;: &quot;password missing&quot;
}
bob@dylan:~$ 
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XPOST -d &quot;email=guillaume@hbtn.io&quot; -d &quot;password=test&quot;
{
  &quot;error&quot;: &quot;no user found for this email&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XPOST -d &quot;email=bobsession@hbtn.io&quot; -d &quot;password=test&quot;
{
  &quot;error&quot;: &quot;wrong password&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XPOST -d &quot;email=bobsession@hbtn.io&quot; -d &quot;password=fake pwd&quot;
{
  &quot;created_at&quot;: &quot;2017-10-16 04:23:04&quot;, 
  &quot;email&quot;: &quot;bobsession@hbtn.io&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;cf3ddee1-ff24-49e4-a40b-2540333fe992&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-10-16 04:23:04&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XPOST -d &quot;email=bobsession@hbtn.io&quot; -d &quot;password=fake pwd&quot; -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; POST /api/v1/auth_session/login HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; Content-Length: 42
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 42 out of 42 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Set-Cookie: _my_session_id=df05b4e1-d117-444c-a0cc-ba0d167889c4; Path=/
&lt; Access-Control-Allow-Origin: *
&lt; Content-Length: 210
&lt; Server: Werkzeug/0.12.1 Python/3.4.3
&lt; Date: Mon, 16 Oct 2017 04:57:08 GMT
&lt; 
{
  &quot;created_at&quot;: &quot;2017-10-16 04:23:04&quot;, 
  &quot;email&quot;: &quot;bobsession@hbtn.io&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;cf3ddee1-ff24-49e4-a40b-2540333fe992&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-10-16 04:23:04&quot;
}
* Closing connection 0
bob@dylan:~$ 
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; --cookie &quot;_my_session_id=df05b4e1-d117-444c-a0cc-ba0d167889c4&quot;
{
  &quot;created_at&quot;: &quot;2017-10-16 04:23:04&quot;, 
  &quot;email&quot;: &quot;bobsession@hbtn.io&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;cf3ddee1-ff24-49e4-a40b-2540333fe992&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-10-16 04:23:04&quot;
}
bob@dylan:~$
</code></pre>
            <p>Now you have an authentication based on a Session ID stored in cookie, perfect for a website (browsers love cookies).</p>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x02-Session_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/views/session_auth.py, api/v1/views/__init__.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">QA Review</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">8. Logout</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Update the class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SessionAuth</code> by adding a new method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def destroy_session(self, request=None):</code> that deletes the user session / logout:</p>
            <ul>
                <li>If the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">request</code> is equal to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>, return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">False</code></li>
                <li>If the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">request</code> doesn&rsquo;t contain the Session ID cookie, return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">False</code> - you must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.session_cookie(request)</code></li>
                <li>If the Session ID of the request is not linked to any User ID, return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">False</code> - you must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.user_id_for_session_id(...)</code></li>
                <li>Otherwise, delete in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.user_id_by_session_id</code> the Session ID (as key of this dictionary) and return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">True</code></li>
            </ul>
            <p>Update the file <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/views/session_auth.py</code>, by adding a new route <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">DELETE /api/v1/auth_session/logout</code>:</p>
            <ul>
                <li>Slash tolerant</li>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">from api.v1.app import auth</code></li>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth.destroy_session(request)</code>for deleting the Session ID contains in the request as cookie:<ul>
                        <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">destroy_session</code> returns <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">False</code>, <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">abort(404)</code></li>
                        <li>Otherwise, return an empty JSON dictionary with the status code 200</li>
                    </ul>
                </li>
            </ul>
            <p>In the first terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In a second terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XPOST -d &quot;email=bobsession@hbtn.io&quot; -d &quot;password=fake pwd&quot; -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; POST /api/v1/auth_session/login HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; Content-Length: 42
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 42 out of 42 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Set-Cookie: _my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721; Path=/
&lt; Access-Control-Allow-Origin: *
&lt; Content-Length: 210
&lt; Server: Werkzeug/0.12.1 Python/3.4.3
&lt; Date: Mon, 16 Oct 2017 04:57:08 GMT
&lt; 
{
  &quot;created_at&quot;: &quot;2017-10-16 04:23:04&quot;, 
  &quot;email&quot;: &quot;bobsession@hbtn.io&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;cf3ddee1-ff24-49e4-a40b-2540333fe992&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-10-16 04:23:04&quot;
}
* Closing connection 0
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; --cookie &quot;_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721&quot;
{
  &quot;created_at&quot;: &quot;2017-10-16 04:23:04&quot;, 
  &quot;email&quot;: &quot;bobsession@hbtn.io&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;cf3ddee1-ff24-49e4-a40b-2540333fe992&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-10-16 04:23:04&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/logout&quot; --cookie &quot;_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721&quot;
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;405 Method Not Allowed&lt;/title&gt;
&lt;h1&gt;Method Not Allowed&lt;/h1&gt;
&lt;p&gt;The method is not allowed for the requested URL.&lt;/p&gt;
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/logout&quot; --cookie &quot;_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721&quot; -XDELETE
{}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; --cookie &quot;_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$
</code></pre>
            <p>Login, logout&hellip; what&rsquo;s else?</p>
            <p>Now, after getting a Session ID, you can request all protected API routes by using this Session ID, no need anymore to send User email and password every time.</p>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x02-Session_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/session_auth.py, api/v1/views/session_auth.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">QA Review</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">9. Expiration?</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">#advanced</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Actually you have 2 authentication systems:</p>
            <ul>
                <li>Basic authentication</li>
                <li>Session authentication</li>
            </ul>
            <p>Now you will add an expiration date to a Session ID.</p>
            <p>Create a class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SessionExpAuth</code> that inherits from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SessionAuth</code> in the file <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/session_exp_auth.py</code>:</p>
            <ul>
                <li>Overload <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def __init__(self):</code>method:<ul>
                        <li>Assign an instance attribute <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">session_duration</code>:<ul>
                                <li>To the environment variable <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SESSION_DURATION</code> casts to an integer</li>
                                <li>If this environment variable doesn&rsquo;t exist or can&rsquo;t be parse to an integer, assign to 0</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li>Overload <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def create_session(self, user_id=None):</code>
                    <ul>
                        <li>Create a Session ID by calling <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">super()</code> - <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">super()</code> will call the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">create_session()</code> method of <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SessionAuth</code></li>
                        <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">super()</code> can&rsquo;t create a Session ID</li>
                        <li>Use this Session ID as key of the dictionary <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id_by_session_id</code>- the value for this key must be a dictionary (called &ldquo;session dictionary&rdquo;):<ul>
                                <li>The key <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id</code> must be set to the variable <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id</code></li>
                                <li>The key <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">created_at</code> must be set to the current datetime - you must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">datetime.now()</code></li>
                            </ul>
                        </li>
                        <li>Return the Session ID created</li>
                    </ul>
                </li>
                <li>Overload <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def user_id_for_session_id(self, session_id=None):</code>
                    <ul>
                        <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">session_id</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code></li>
                        <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id_by_session_id</code> doesn&rsquo;t contain any key equals to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">session_id</code></li>
                        <li>Return the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id</code> key from the session dictionary if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.session_duration</code> is equal or under 0</li>
                        <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if session dictionary doesn&rsquo;t contain a key <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">created_at</code></li>
                        <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">created_at</code> + <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">session_duration</code> seconds are before the current datetime. <a href="https://intranet.alxswe.com/rltoken/mwc3EnlWLNJ2rvzvgZT8eA" title="datetime - timedelta" target="_blank" style="color: transparent;">datetime - timedelta</a></li>
                        <li>Otherwise, return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id</code> from the session dictionary</li>
                    </ul>
                </li>
            </ul>
            <p>Update <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/app.py</code> to instantiate auth with <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SessionExpAuth</code> if the environment variable <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">AUTH_TYPE</code> is equal to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">session_exp_auth</code>.</p>
            <p>In the first terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_exp_auth SESSION_NAME=_my_session_id SESSION_DURATION=60 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In a second terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XPOST -d &quot;email=bobsession@hbtn.io&quot; -d &quot;password=fake pwd&quot; -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; POST /api/v1/auth_session/login HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; Content-Length: 42
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 42 out of 42 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Set-Cookie: _my_session_id=eea5d963-8dd2-46f0-9e43-fd05029ae63f; Path=/
&lt; Access-Control-Allow-Origin: *
&lt; Content-Length: 210
&lt; Server: Werkzeug/0.12.1 Python/3.4.3
&lt; Date: Mon, 16 Oct 2017 04:57:08 GMT
&lt; 
{
  &quot;created_at&quot;: &quot;2017-10-16 04:23:04&quot;, 
  &quot;email&quot;: &quot;bobsession@hbtn.io&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;cf3ddee1-ff24-49e4-a40b-2540333fe992&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-10-16 04:23:04&quot;
}
* Closing connection 0
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; --cookie &quot;_my_session_id=eea5d963-8dd2-46f0-9e43-fd05029ae63f&quot;
{
  &quot;created_at&quot;: &quot;2017-10-16 04:23:04&quot;, 
  &quot;email&quot;: &quot;bobsession@hbtn.io&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;cf3ddee1-ff24-49e4-a40b-2540333fe992&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-10-16 04:23:04&quot;
}
bob@dylan:~$
bob@dylan:~$ sleep 10
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; --cookie &quot;_my_session_id=eea5d963-8dd2-46f0-9e43-fd05029ae63f&quot;
{
  &quot;created_at&quot;: &quot;2017-10-16 04:23:04&quot;, 
  &quot;email&quot;: &quot;bobsession@hbtn.io&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;cf3ddee1-ff24-49e4-a40b-2540333fe992&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-10-16 04:23:04&quot;
}
bob@dylan:~$ 
bob@dylan:~$ sleep 51 # 10 + 51 &gt; 60
bob@dylan:~$ 
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; --cookie &quot;_my_session_id=eea5d963-8dd2-46f0-9e43-fd05029ae63f&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x02-Session_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/session_exp_auth.py, api/v1/app.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">QA Review</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">10. Sessions in database</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">#advanced</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Since the beginning, all Session IDs are stored in memory. It means, if your application stops, all Session IDs are lost.</p>
            <p>For avoid that, you will create a new authentication system, based on Session ID stored in database (for us, it will be in a file, like <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code>).</p>
            <p>Create a new model <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">UserSession</code> in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">models/user_session.py</code> that inherits from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Base</code>:</p>
            <ul>
                <li>Implement the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def __init__(self, *args: list, **kwargs: dict):</code> like in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code>but for these 2 attributes:<ul>
                        <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_id</code>: string</li>
                        <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">session_id</code>: string</li>
                    </ul>
                </li>
            </ul>
            <p>Create a new authentication class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SessionDBAuth</code> in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/session_db_auth.py</code> that inherits from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SessionExpAuth</code>:</p>
            <ul>
                <li>Overload <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def create_session(self, user_id=None):</code> that creates and stores new instance of <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">UserSession</code> and returns the Session ID</li>
                <li>Overload <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def user_id_for_session_id(self, session_id=None):</code> that returns the User ID by requesting <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">UserSession</code> in the database based on <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">session_id</code></li>
                <li>Overload <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def destroy_session(self, request=None):</code> that destroys the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">UserSession</code> based on the Session ID from the request cookie</li>
            </ul>
            <p>Update <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/app.py</code> to instantiate <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth</code> with <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">SessionDBAuth</code> if the environment variable <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">AUTH_TYPE</code> is equal to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">session_db_auth</code>.</p>
            <p>In the first terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_db_auth SESSION_NAME=_my_session_id SESSION_DURATION=60 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In a second terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XPOST -d &quot;email=bobsession@hbtn.io&quot; -d &quot;password=fake pwd&quot; -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; POST /api/v1/auth_session/login HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; Content-Length: 42
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 42 out of 42 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Set-Cookie: _my_session_id=bacadfad-3c3b-4830-b1b2-3d77dfb9ad13; Path=/
&lt; Access-Control-Allow-Origin: *
&lt; Content-Length: 210
&lt; Server: Werkzeug/0.12.1 Python/3.4.3
&lt; Date: Mon, 16 Oct 2017 04:57:08 GMT
&lt; 
{
  &quot;created_at&quot;: &quot;2017-10-16 04:23:04&quot;, 
  &quot;email&quot;: &quot;bobsession@hbtn.io&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;cf3ddee1-ff24-49e4-a40b-2540333fe992&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-10-16 04:23:04&quot;
}
* Closing connection 0
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; --cookie &quot;_my_session_id=bacadfad-3c3b-4830-b1b2-3d77dfb9ad13&quot;
{
  &quot;created_at&quot;: &quot;2017-10-16 04:23:04&quot;, 
  &quot;email&quot;: &quot;bobsession@hbtn.io&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;cf3ddee1-ff24-49e4-a40b-2540333fe992&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-10-16 04:23:04&quot;
}
bob@dylan:~$
bob@dylan:~$ sleep 10
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; --cookie &quot;_my_session_id=bacadfad-3c3b-4830-b1b2-3d77dfb9ad13&quot;
{
  &quot;created_at&quot;: &quot;2017-10-16 04:23:04&quot;, 
  &quot;email&quot;: &quot;bobsession@hbtn.io&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;cf3ddee1-ff24-49e4-a40b-2540333fe992&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-10-16 04:23:04&quot;
}
bob@dylan:~$
bob@dylan:~$ sleep 60
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; --cookie &quot;_my_session_id=bacadfad-3c3b-4830-b1b2-3d77dfb9ad13&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x02-Session_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/session_db_auth.py, api/v1/app.py, models/user_session.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button>&nbsp;</div>
            </div>
        </div>
    </div>
</div>
