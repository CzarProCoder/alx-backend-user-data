<h1 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 36px;">0x01. Basic authentication</h1>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(219, 62, 62);font-size: 14px;">Back-end</span></strong><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(219, 62, 62);font-size: 14px;">Authentification</span></strong></div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <ul style="font-size: 11px;">
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">By: Guillaume, CTO at Holberton School</li>
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">Weight: 1</li>
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">Ongoing second chance project - started <span title=""><span style="border-bottom: 0.5px dashed currentcolor;">Nov 6, 2023 6:00 AM</span></span>, must end by <span title=""><span style="border-bottom: 0.5px dashed currentcolor;">Nov 11, 2023 6:00 AM</span></span></li>
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">An auto review will be launched at the deadline</li>
    </ul>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);font-size: 14px;border: 1px solid rgb(238, 238, 238);">
    <h4 style="color: inherit;font-size: 18px;">In a nutshell&hellip;</h4>
    <ul>
        <li><strong><strong>Auto QA review:</strong></strong> 12.0/169 mandatory &amp; 0.0/27 optional</li>
        <li><strong><strong>Altogether:</strong></strong>&nbsp; <strong><strong>7.1%</strong></strong>
            <ul>
                <li>Mandatory: 7.1%</li>
                <li>Optional: 0.0%</li>
                <li>Calculation: &nbsp;7.1% + (7.1% * 0.0%) &nbsp;== <strong><strong>7.1%</strong></strong></li>
            </ul>
        </li>
    </ul>
</div>
<div style="text-align: start;color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);font-size: 14px;border: 1px solid rgb(221, 221, 221);">
    <div>
        <h2 style="color: inherit;font-size: 30px;">Background Context</h2>
        <p>In this project, you will learn what the authentication process means and implement a <strong><strong>Basic Authentication</strong></strong> on a simple API.</p>
        <p>In the industry, you should <strong><strong>not</strong></strong> implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask: <a href="https://intranet.alxswe.com/rltoken/rpsPy0M3_FJuCLGNPUbmvg" title="Flask-HTTPAuth" target="_blank" style="color: transparent;">Flask-HTTPAuth</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.</p>
        <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/5/6ccb363443a8f301bc2bc38d7a08e9650117de7c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231109T092622Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d0428afe185273173fe887fea3ed192be6c52fc554d070770fe6271a77113ab9" alt="" style="border: 0px;"></p>
        <h2 style="color: inherit;font-size: 30px;">Resources</h2>
        <p><strong><strong>Read or watch</strong></strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/ssg5umgsMk5jKM8WRHk2Ug" title="REST API Authentication Mechanisms" target="_blank" style="color: transparent;">REST API Authentication Mechanisms</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/RpaPRyKx1rdHgRSUyuPfeg" title="Base64 in Python" target="_blank" style="color: transparent;">Base64 in Python</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/WlARq8tQPUGQq5VphLKM4w" title="HTTP header Authorization" target="_blank" style="color: transparent;">HTTP header Authorization</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/HG5WXgSja5kMa29fbMd9Aw" title="Flask" target="_blank" style="color: transparent;">Flask</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/br6Rp4iMaOce6EAC-JQnOw" title="Base64 - concept" target="_blank" style="color: transparent;">Base64 - concept</a></li>
        </ul>
        <h2 style="color: inherit;font-size: 30px;">Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to <a href="https://intranet.alxswe.com/rltoken/swiIZazfz7mspY1vjuy_Zg" title="explain to anyone" target="_blank" style="color: transparent;">explain to anyone</a>, <strong><strong>without the help of Google</strong></strong>:</p>
        <h3 style="color: inherit;font-size: 24px;">General</h3>
        <ul>
            <li>What authentication means</li>
            <li>What Base64 is</li>
            <li>How to encode a string in Base64</li>
            <li>What Basic authentication means</li>
            <li>How to send the Authorization header</li>
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
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">0. Simple-basic-API</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 100.0% (<em><span style="font-size: 12px;">Checks completed: 100.0%</span></em>)</div>
            </div>
            <p>Download and start your project from this <a href="https://intranet.alxswe.com/rltoken/2o4gAozNufil_KjoxKI5bA" title="archive.zip" target="_blank" style="color: transparent;">archive.zip</a></p>
            <p>In this archive, you will find a simple API with one model: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code>. Storage of these users is done via a serialization/deserialization in files.</p>
            <h4 style="color: inherit;font-size: 18px;">Setup and start server</h4>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ pip3 install -r requirements.txt
...
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Serving Flask app &quot;app&quot; (lazy loading)
...
bob@dylan:~$
</code></pre>
            <h4 style="color: inherit;font-size: 18px;">Use the API <em>(in another tab or in your browser)</em></h4>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/status&quot; -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; GET /api/v1/status HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; 
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Content-Length: 16
&lt; Access-Control-Allow-Origin: *
&lt; Server: Werkzeug/1.0.1 Python/3.7.5
&lt; Date: Mon, 18 May 2020 20:29:21 GMT
&lt; 
{&quot;status&quot;:&quot;OK&quot;}
* Closing connection 0
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-Basic_authentication</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(60, 118, 61);background-color: rgb(223, 240, 216);font-size: 12px;border: 1px solid rgb(214, 233, 198);">&nbsp;Done!</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">QA Review</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">1. Error handler: Unauthorized</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 25.0% (<em><span style="font-size: 12px;">Checks completed: 25.0%</span></em>)</div>
            </div>
            <p>What the HTTP status code for a request unauthorized? <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">401</code> of course!</p>
            <p>Edit <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/app.py</code>:</p>
            <ul>
                <li>Add a new error handler for this status code, the response must be:<ul>
                        <li>a JSON: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">{&quot;error&quot;: &quot;Unauthorized&quot;}</code></li>
                        <li>status code <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">401</code></li>
                        <li>you must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">jsonify</code> from Flask</li>
                    </ul>
                </li>
            </ul>
            <p>For testing this new error handler, add a new endpoint in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/views/index.py</code>:</p>
            <ul>
                <li>Route: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">GET /api/v1/unauthorized</code></li>
                <li>This endpoint must raise a 401 error by using <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">abort</code> - <a href="https://intranet.alxswe.com/rltoken/RH0gY_XQuSB75Q-JbI-fdg" title="Custom Error Pages" target="_blank" style="color: transparent;">Custom Error Pages</a></li>
            </ul>
            <p>By calling <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">abort(401)</code>, the error handler for 401 will be executed.</p>
            <p>In the first terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In a second terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/unauthorized&quot;
{
  &quot;error&quot;: &quot;Unauthorized&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/unauthorized&quot; -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; GET /api/v1/unauthorized HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; 
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 401 UNAUTHORIZED
&lt; Content-Type: application/json
&lt; Content-Length: 30
&lt; Server: Werkzeug/0.12.1 Python/3.4.3
&lt; Date: Sun, 24 Sep 2017 22:50:40 GMT
&lt; 
{
  &quot;error&quot;: &quot;Unauthorized&quot;
}
* Closing connection 0
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-Basic_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/app.py, api/v1/views/index.py</code></li>
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
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">2. Error handler: Forbidden</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 25.0% (<em><span style="font-size: 12px;">Checks completed: 25.0%</span></em>)</div>
            </div>
            <p>What the HTTP status code for a request where the user is authenticate but not allowed to access to a resource? <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">403</code> of course!</p>
            <p>Edit <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/app.py</code>:</p>
            <ul>
                <li>Add a new error handler for this status code, the response must be:<ul>
                        <li>a JSON: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">{&quot;error&quot;: &quot;Forbidden&quot;}</code></li>
                        <li>status code <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">403</code></li>
                        <li>you must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">jsonify</code> from Flask</li>
                    </ul>
                </li>
            </ul>
            <p>For testing this new error handler, add a new endpoint in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/views/index.py</code>:</p>
            <ul>
                <li>Route: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">GET /api/v1/forbidden</code></li>
                <li>This endpoint must raise a 403 error by using <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">abort</code> - <a href="https://intranet.alxswe.com/rltoken/RH0gY_XQuSB75Q-JbI-fdg" title="Custom Error Pages" target="_blank" style="color: transparent;">Custom Error Pages</a></li>
            </ul>
            <p>By calling <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">abort(403)</code>, the error handler for 403 will be executed.</p>
            <p>In the first terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In a second terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/forbidden&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/forbidden&quot; -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; GET /api/v1/forbidden HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; 
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 403 FORBIDDEN
&lt; Content-Type: application/json
&lt; Content-Length: 27
&lt; Server: Werkzeug/0.12.1 Python/3.4.3
&lt; Date: Sun, 24 Sep 2017 22:54:22 GMT
&lt; 
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
* Closing connection 0
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-Basic_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/app.py, api/v1/views/index.py</code></li>
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
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">3. Auth class</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Now you will create a class to manage the API authentication.</p>
            <ul>
                <li>Create a folder <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth</code></li>
                <li>Create an empty file <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/__init__.py</code></li>
                <li>Create the class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Auth</code>:<ul>
                        <li>in the file <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/auth.py</code></li>
                        <li>import <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">request</code> from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">flask</code></li>
                        <li>class name <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Auth</code></li>
                        <li>public method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def require_auth(self, path: str, excluded_paths: List[str]) -&gt; bool:</code> that returns <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">False</code> - <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">path</code> and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">excluded_paths</code> will be used later, now, you don&rsquo;t need to take care of them</li>
                        <li>public method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def authorization_header(self, request=None) -&gt; str:</code> that returns <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> - <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">request</code> will be the Flask request object</li>
                        <li>public method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def current_user(self, request=None) -&gt; TypeVar(&apos;User&apos;):</code> that returns <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> - <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">request</code> will be the Flask request object</li>
                    </ul>
                </li>
            </ul>
            <p>This class is the template for all authentication system you will implement.</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat main_0.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 0
&quot;&quot;&quot;
from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth(&quot;/api/v1/status/&quot;, [&quot;/api/v1/status/&quot;]))
print(a.authorization_header())
print(a.current_user())

bob@dylan:~$ 
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_0.py
False
None
None
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-Basic_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth, api/v1/auth/__init__.py, api/v1/auth/auth.py</code></li>
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
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">4. Define which routes don&apos;t need authentication</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Update the method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def require_auth(self, path: str, excluded_paths: List[str]) -&gt; bool:</code> in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Auth</code> that returns <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">True</code> if the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">path</code> is not in the list of strings <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">excluded_paths</code>:</p>
            <ul>
                <li>Returns <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">True</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">path</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code></li>
                <li>Returns <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">True</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">excluded_paths</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> or empty</li>
                <li>Returns <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">False</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">path</code> is in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">excluded_paths</code></li>
                <li>You can assume <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">excluded_paths</code> contains string path always ending by a <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">/</code></li>
                <li>This method must be slash tolerant: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">path=/api/v1/status</code> and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">path=/api/v1/status/</code> must be returned <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">False</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">excluded_paths</code> contains <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">/api/v1/status/</code></li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat main_1.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 1
&quot;&quot;&quot;
from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth(None, None))
print(a.require_auth(None, []))
print(a.require_auth(&quot;/api/v1/status/&quot;, []))
print(a.require_auth(&quot;/api/v1/status/&quot;, [&quot;/api/v1/status/&quot;]))
print(a.require_auth(&quot;/api/v1/status&quot;, [&quot;/api/v1/status/&quot;]))
print(a.require_auth(&quot;/api/v1/users&quot;, [&quot;/api/v1/status/&quot;]))
print(a.require_auth(&quot;/api/v1/users&quot;, [&quot;/api/v1/status/&quot;, &quot;/api/v1/stats&quot;]))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_1.py
True
True
True
False
False
True
True
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-Basic_authentication</code></li>
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
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">5. Request validation!</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Now you will validate all requests to secure the API:</p>
            <p>Update the method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def authorization_header(self, request=None) -&gt; str:</code> in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/auth.py</code>:</p>
            <ul>
                <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">request</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>, returns <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code></li>
                <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">request</code> doesn&rsquo;t contain the header key <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Authorization</code>, returns <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code></li>
                <li>Otherwise, return the value of the header request <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Authorization</code></li>
            </ul>
            <p>Update the file <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/app.py</code>:</p>
            <ul>
                <li>Create a variable <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth</code> initialized to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> after the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">CORS</code> definition</li>
                <li>Based on the environment variable <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">AUTH_TYPE</code>, load and assign the right instance of authentication to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth</code>
                    <ul>
                        <li>if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth</code>:<ul>
                                <li>import <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Auth</code> from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api.v1.auth.auth</code></li>
                                <li>create an instance of <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Auth</code> and assign it to the variable <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth</code></li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
            <p>Now the biggest piece is the filtering of each request. For that you will use the Flask method <a href="https://intranet.alxswe.com/rltoken/kzBrJT9aaokbD6aWYyQzXg" title="before_request" target="_blank" style="color: transparent;">before_request</a></p>
            <ul>
                <li>Add a method in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/app.py</code> to handler <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">before_request</code>
                    <ul>
                        <li>if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>, do nothing</li>
                        <li>if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">request.path</code> is not part of this list <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">[&apos;/api/v1/status/&apos;, &apos;/api/v1/unauthorized/&apos;, &apos;/api/v1/forbidden/&apos;]</code>, do nothing - you must use the method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">require_auth</code> from the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth</code> instance</li>
                        <li>if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth.authorization_header(request)</code> returns <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>, raise the error <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">401</code> - you must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">abort</code></li>
                        <li>if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth.current_user(request)</code> returns <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>, raise the error <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">403</code> - you must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">abort</code></li>
                    </ul>
                </li>
            </ul>
            <p>In the first terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=auth python3 -m api.v1.app
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
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-Basic_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/app.py, api/v1/auth/auth.py</code></li>
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
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">6. Basic auth</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Create a class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BasicAuth</code> that inherits from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Auth</code>. For the moment this class will be empty.</p>
            <p>Update <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/app.py</code> for using <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BasicAuth</code> class instead of <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Auth</code> depending of the value of the environment variable <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">AUTH_TYPE</code>, If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">AUTH_TYPE</code> is equal to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">basic_auth</code>:</p>
            <ul>
                <li>import <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BasicAuth</code> from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api.v1.auth.basic_auth</code></li>
                <li>create an instance of <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BasicAuth</code> and assign it to the variable <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth</code></li>
            </ul>
            <p>Otherwise, keep the previous mechanism with <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">auth</code> an instance of <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Auth</code>.</p>
            <p>In the first terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
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
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-Basic_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/app.py, api/v1/auth/basic_auth.py</code></li>
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
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">7. Basic - Base64 part</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Add the method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def extract_base64_authorization_header(self, authorization_header: str) -&gt; str:</code> in the class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BasicAuth</code> that returns the Base64 part of the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Authorization</code> header for a Basic Authentication:</p>
            <ul>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">authorization_header</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code></li>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">authorization_header</code> is not a string</li>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">authorization_header</code> doesn&rsquo;t start by <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Basic</code> (with a space at the end)</li>
                <li>Otherwise, return the value after <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Basic</code> (after the space)</li>
                <li>You can assume <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">authorization_header</code> contains only one <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Basic</code></li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat main_2.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 2
&quot;&quot;&quot;
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.extract_base64_authorization_header(None))
print(a.extract_base64_authorization_header(89))
print(a.extract_base64_authorization_header(&quot;Holberton School&quot;))
print(a.extract_base64_authorization_header(&quot;Basic Holberton&quot;))
print(a.extract_base64_authorization_header(&quot;Basic SG9sYmVydG9u&quot;))
print(a.extract_base64_authorization_header(&quot;Basic SG9sYmVydG9uIFNjaG9vbA==&quot;))
print(a.extract_base64_authorization_header(&quot;Basic1234&quot;))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_2.py
None
None
None
Holberton
SG9sYmVydG9u
SG9sYmVydG9uIFNjaG9vbA==
None
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-Basic_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/basic_auth.py</code></li>
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
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">8. Basic - Base64 decode</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Add the method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def decode_base64_authorization_header(self, base64_authorization_header: str) -&gt; str:</code> in the class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BasicAuth</code> that returns the decoded value of a Base64 string <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">base64_authorization_header</code>:</p>
            <ul>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">base64_authorization_header</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code></li>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">base64_authorization_header</code> is not a string</li>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">base64_authorization_header</code> is not a valid Base64 - you can use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">try/except</code></li>
                <li>Otherwise, return the decoded value as UTF8 string - you can use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">decode(&apos;utf-8&apos;)</code></li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat main_3.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 3
&quot;&quot;&quot;
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.decode_base64_authorization_header(None))
print(a.decode_base64_authorization_header(89))
print(a.decode_base64_authorization_header(&quot;Holberton School&quot;))
print(a.decode_base64_authorization_header(&quot;SG9sYmVydG9u&quot;))
print(a.decode_base64_authorization_header(&quot;SG9sYmVydG9uIFNjaG9vbA==&quot;))
print(a.decode_base64_authorization_header(a.extract_base64_authorization_header(&quot;Basic SG9sYmVydG9uIFNjaG9vbA==&quot;)))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_3.py
None
None
None
Holberton
Holberton School
Holberton School
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-Basic_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/basic_auth.py</code></li>
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
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">9. Basic - User credentials</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Add the method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def extract_user_credentials(self, decoded_base64_authorization_header: str) -&gt; (str, str)</code> in the class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BasicAuth</code> that returns the user email and password from the Base64 decoded value.</p>
            <ul>
                <li>This method must return 2 values</li>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None, None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">decoded_base64_authorization_header</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code></li>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None, None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">decoded_base64_authorization_header</code> is not a string</li>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None, None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">decoded_base64_authorization_header</code> doesn&rsquo;t contain <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">:</code></li>
                <li>Otherwise, return the user email and the user password - these 2 values must be separated by a <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">:</code></li>
                <li>You can assume <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">decoded_base64_authorization_header</code> will contain only one <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">:</code></li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat main_4.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 4
&quot;&quot;&quot;
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.extract_user_credentials(None))
print(a.extract_user_credentials(89))
print(a.extract_user_credentials(&quot;Holberton School&quot;))
print(a.extract_user_credentials(&quot;Holberton:School&quot;))
print(a.extract_user_credentials(&quot;bob@gmail.com:toto1234&quot;))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_4.py
(None, None)
(None, None)
(None, None)
(&apos;Holberton&apos;, &apos;School&apos;)
(&apos;bob@gmail.com&apos;, &apos;toto1234&apos;)
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-Basic_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/basic_auth.py</code></li>
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
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">10. Basic - User object</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Add the method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def user_object_from_credentials(self, user_email: str, user_pwd: str) -&gt; TypeVar(&apos;User&apos;):</code> in the class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BasicAuth</code> that returns the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> instance based on his email and password.</p>
            <ul>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_email</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> or not a string</li>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_pwd</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> or not a string</li>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if your database (file) doesn&rsquo;t contain any <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> instance with email equal to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_email</code> - you should use the class method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">search</code> of the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> to lookup the list of users based on their email. Don&rsquo;t forget to test all cases: &ldquo;what if there is no user in DB?&rdquo;, etc.</li>
                <li>Return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> if <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_pwd</code> is not the password of the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> instance found - you must use the method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">is_valid_password</code> of <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code></li>
                <li>Otherwise, return the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> instance</li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat main_5.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 5
&quot;&quot;&quot;
import uuid
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

&quot;&quot;&quot; Create a user test &quot;&quot;&quot;
user_email = str(uuid.uuid4())
user_clear_pwd = str(uuid.uuid4())
user = User()
user.email = user_email
user.first_name = &quot;Bob&quot;
user.last_name = &quot;Dylan&quot;
user.password = user_clear_pwd
print(&quot;New user: {}&quot;.format(user.display_name()))
user.save()

&quot;&quot;&quot; Retreive this user via the class BasicAuth &quot;&quot;&quot;

a = BasicAuth()

u = a.user_object_from_credentials(None, None)
print(u.display_name() if u is not None else &quot;None&quot;)

u = a.user_object_from_credentials(89, 98)
print(u.display_name() if u is not None else &quot;None&quot;)

u = a.user_object_from_credentials(&quot;email@notfound.com&quot;, &quot;pwd&quot;)
print(u.display_name() if u is not None else &quot;None&quot;)

u = a.user_object_from_credentials(user_email, &quot;pwd&quot;)
print(u.display_name() if u is not None else &quot;None&quot;)

u = a.user_object_from_credentials(user_email, user_clear_pwd)
print(u.display_name() if u is not None else &quot;None&quot;)

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_5.py 
New user: Bob Dylan
None
None
None
None
Bob Dylan
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-Basic_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/basic_auth.py</code></li>
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
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">11. Basic - Overload current_user - and BOOM!</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Now, you have all pieces for having a complete Basic authentication.</p>
            <p>Add the method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def current_user(self, request=None) -&gt; TypeVar(&apos;User&apos;)</code> in the class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BasicAuth</code> that overloads <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">Auth</code> and retrieves the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">User</code> instance for a request:</p>
            <ul>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">authorization_header</code></li>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">extract_base64_authorization_header</code></li>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">decode_base64_authorization_header</code></li>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">extract_user_credentials</code></li>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">user_object_from_credentials</code></li>
            </ul>
            <p>With this update, now your API is fully protected by a Basic Authentication. Enjoy!</p>
            <p>In the first terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat main_6.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 6
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
print(&quot;New user: {} / {}&quot;.format(user.id, user.display_name()))
user.save()

basic_clear = &quot;{}:{}&quot;.format(user_email, user_clear_pwd)
print(&quot;Basic Base64: {}&quot;.format(base64.b64encode(basic_clear.encode(&apos;utf-8&apos;)).decode(&quot;utf-8&quot;)))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_6.py 
New user: 9375973a-68c7-46aa-b135-29f79e837495 / bob@hbtn.io
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
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot; -H &quot;Authorization: Test&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$ 
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot; -H &quot;Authorization: Basic test&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
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
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-Basic_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/basic_auth.py</code></li>
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
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">12. Basic - Allow password with &quot;:&quot;</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">#advanced</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Improve the method <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def extract_user_credentials(self, decoded_base64_authorization_header)</code> to allow password with <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">:</code>.</p>
            <p>In the first terminal:</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat main_100.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 100
&quot;&quot;&quot;
import base64
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

&quot;&quot;&quot; Create a user test &quot;&quot;&quot;
user_email = &quot;bob100@hbtn.io&quot;
user_clear_pwd = &quot;H0lberton:School:98!&quot;

user = User()
user.email = user_email
user.password = user_clear_pwd
print(&quot;New user: {}&quot;.format(user.id))
user.save()

basic_clear = &quot;{}:{}&quot;.format(user_email, user_clear_pwd)
print(&quot;Basic Base64: {}&quot;.format(base64.b64encode(basic_clear.encode(&apos;utf-8&apos;)).decode(&quot;utf-8&quot;)))

bob@dylan:~$ 
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_100.py 
New user: 5891469b-d2d5-4d33-b05d-02617d665368
Basic Base64: Ym9iMTAwQGhidG4uaW86SDBsYmVydG9uOlNjaG9vbDo5OCE=
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
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot; -H &quot;Authorization: Test&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot; -H &quot;Authorization: Basic test&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot; -H &quot;Authorization: Basic Ym9iMTAwQGhidG4uaW86SDBsYmVydG9uOlNjaG9vbDo5OCE=&quot;
[
  {
    &quot;created_at&quot;: &quot;2017-09-25 01:55:17&quot;, 
    &quot;email&quot;: &quot;bob@hbtn.io&quot;, 
    &quot;first_name&quot;: null, 
    &quot;id&quot;: &quot;9375973a-68c7-46aa-b135-29f79e837495&quot;, 
    &quot;last_name&quot;: null, 
    &quot;updated_at&quot;: &quot;2017-09-25 01:55:17&quot;
  },
  {
    &quot;created_at&quot;: &quot;2017-09-25 01:59:42&quot;, 
    &quot;email&quot;: &quot;bob100@hbtn.io&quot;, 
    &quot;first_name&quot;: null, 
    &quot;id&quot;: &quot;5891469b-d2d5-4d33-b05d-02617d665368&quot;, 
    &quot;last_name&quot;: null, 
    &quot;updated_at&quot;: &quot;2017-09-25 01:59:42&quot;
  }
]
bob@dylan:~$
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-Basic_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/basic_auth.py</code></li>
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
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">13. Require auth with stars</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">#advanced</span></strong></div>
        </div>
        <div>
            <div style="color: rgb(152, 163, 174);border: 1px solid rgb(238, 238, 238);">
                <div>
                    <div><br></div>
                </div>
                <div>Score: 0.0% (<em><span style="font-size: 12px;">Checks completed: 0.0%</span></em>)</div>
            </div>
            <p>Improve <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def require_auth(self, path, excluded_paths)</code> by allowing <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">*</code> at the end of excluded paths.</p>
            <p>Example for <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">excluded_paths = [&quot;/api/v1/stat*&quot;]</code>:</p>
            <ul>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">/api/v1/users</code> will return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">True</code></li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">/api/v1/status</code> will return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">False</code></li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">/api/v1/stats</code> will return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">False</code></li>
            </ul>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-user-data</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-Basic_authentication</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">api/v1/auth/auth.py</code></li>
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
