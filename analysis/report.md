# eHealth Corp

#### Project 1 - SIO

___

## ![](https://cdn.discordapp.com/attachments/852109272262770710/1042518122550263848/logo-no-backgroundehealth.png)

---

## Index

1. Introduction

2. Overview

3. Vulnerabilites
   
   - CWE - 89
   
   - CWE - 79
   
   - CWE - 352
   
   - CWE - 488
   
   - CWE - 798
   
   - CWE - 620
   
   - CWE - 521 
   
   - CWE - 522
   
   - CWE - 434

4. Final Considerations

___

## 1. Introduction

The present report serves as documentation for Project 1 of SIO which intends to explore the possible vulnerabiilites, their consequences and their counters in a webapp for a ficitious clinic: eHealth Corp.

____

## 2. Overview

To implement and counteract our selected vulnerabilites we used Flask: HTML with Boostrap on the frontend, data renderization with templating using Jinja2 and a SQLite database for data persistency on the backend.

____

## 3. Vulnerabilites

### CWE - 89 - Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

#### Abstract

An example of SQL injection is when an attacker inserts Structured Query Language (SQL) code into a Web form input box to access resources or modify data.

An SQL query is a request for a database action to be taken.

Normally, when a user enters their name and password into the corresponding text boxes on a Web form for user authentication, those values are added to a SELECT query.

The user is given access if the values they submitted are found as expected; if they are not, access is refused.

However, except for names and passwords, most Web forms don't have any safeguards in place to prevent input.

In the absence of such security measures, a hacker may utilize the input boxes to give the database their own request, allowing them to download the entire database or engage with it in other illegal ways.

In this way, SQL injection can give an attacker unrestricted access to sensitive data, such as client information, personally identifiable information, trade secrets, intellectual property, and other sensitive data.

The ability to read, edit, and steal confidential data enables attackers to easily gain access to and take over a system.

#### Exploitation

In this case, SQL injection is possible in the password field of the login page, by entering an input that abuses the SQL quotation notation, for example '  or 1=1 -- as such:

![](https://cdn.discordapp.com/attachments/852109272262770710/1042661780205342750/injectionunsafe.gif)

#### Counteraction

Originally, the password is received and processed directly like so:

```python
result = db.session.execute("SELECT * FROM user WHERE email = '"+email+"' AND password = '"+password+"';").fetchall()
```

To correct this, the **werkzeug** library was employed to process the password through hashing. Furthermore, SQL Alchemy was used to make sure that the password matches that which is associated with the user. In pratical terms, this translates into a guard clause like the following:

```python
user = User.query.filter_by(email=email).first()
if not user or not check_password_hash(user.password, password):
    flash('Please check your login details and try again.')
    return redirect(url_for('auth.login'))
```

This results in the prevention of any type of SQL injection in this input field, as seen below:

### CWE - 79 - Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')

#### Abstract

Attacks called Cross-Site Scripting (XSS) include injecting malicious scripts into reliable websites.

Attackers can deliver malicious code, typically in the form of a browser side script, to a separate end user by using a web application. The attacker can engage in a number of malicious actions after injecting the malicious script. The victim's computer may be used to send private information to the attacker, such as cookies that may contain session information.

When the victim has administrator rights to control a website, the attacker can send malicious requests on the victim's behalf, which could be extremely damaging for the website.

XSS attacks are broadly classified into two types: non-persistent (reflected) and persistent 

- The most frequent type of cross-site scripting is non-persistent (reflected) XSS.
  The injected malicious script is "reflected" off the web server as a response that contains some or all of the input supplied to the server as part of the request in this type of attack.
  In such circumstances, the injected code travels to the susceptible website, "reflecting" the attack back to the victim's browser.
  Because it came from a trustworthy server, the code is then executed by the browser.

- The malicious script is stored on the victim web-server in a persistent (stored) XSS attack.
  The injected script is subsequently permanently saved on the web pages and returned to any user who accesses the script-containing web page. 
  
  This is the type of XSS that we will be implementing and combating in this project.

Weakness repercussions include the exposure or theft of information saved in the user's cookies, as well as the jeopardization of secrecy by the installation of Trojan horse programs or other malicious software.

#### Exploitation

#### Counteraction

### CWE - 352 - Cross-Site Request Forgery

#### Abstract

When a web server is constructed to receive a request from a client without any way for verifying that it was submitted intentionally, an attacker may be able to fool a client into sending an unintended request to the web server, which will be viewed as a genuine request.
This can be accomplished by a URL, image load, XMLHttpRequest, or other means, and can result in data exposure or inadvertent code execution. 

#### Exploitation

By producing a POST request externally from the application, one can easliy inject fake contacts, like so:

#### Counteraction

By using the **flask-wtf** library, it's possible to stop unintended POSTs from successfully submitting, by associating an authentication token to these requests, as such:

### CWE - 488 - Exposure of Data Element to Wrong Session

#### Abstract

The solution fails to adequately enforce the boundaries between the states of distinct sessions, resulting in data being provided to or used by the incorrect session.

#### Exploitation

#### Counteraction

### CWE - 798 - Use of Hard-coded Credentials

#### Abstract

Hard-coded credentials generally leave a big gap that allows an attacker to bypass the authentication that the software administrator has configured.
This vulnerability may be difficult to discover for the system administrator.
Even if it is detected, it can be impossible to repair, thus the administrator may be obliged to disable the product completely. 

In this project, the inbound variation of this vulnerability will be explored, this is where a default administrator account is generated and a basic password is hard-coded into the product and connected with that account.
This hard-coded password is the same for each installation of the product, and system administrators often cannot change or disable it without manually editing the application or otherwise updating the software.
If the password is ever found or publicized (which is often on the Internet), anyone with this password can access the product.
Lastly, because all installations of the program will use the same password, even across businesses, huge assaults such as worms are possible. 

#### Exploitation

#### Counteraction

### CWE - 620 - Unverified Password Change

#### Abstract

The product does not need knowledge of the original password or the usage of another type of authentication when creating a new password for a user.

An attacker might use this to change passwords for another account, acquiring the rights associated with that user. 

#### Exploitation

By not asking for the user's current password when editing their profile, this allows a rogue agent who has access to the user's current session to lock them out of their account:

![](https://media.discordapp.net/attachments/1031594520061689916/1042666766658191411/image.png?width=489&height=623)

#### Counteraction

Simply adding a field that requires the user to input their current password ensures their account isn't currently compromised:

![](https://media.discordapp.net/attachments/1031594520061689916/1042666547170254868/image.png?width=489&height=623)

### CWE - 521 - Weak Password Requirements

#### Abstract

To provide an assertion of identity for a system user, authentication systems frequently rely on a memorized secret (also known as a password).
As a result, it is critical that this password be sufficiently complex and difficult for an attacker to guess.
The particular criteria for how complicated a password must be vary according to the type of system being secured.
Choosing the right password requirements and enforcing them via implementation are important to the authentication mechanism's overall success. 

#### Exploitation

The exploitation of this 

#### Counteraction

### CWE - 522 - Insufficiently Protected Credentials

#### Abstract

The site sends or saves authentication credentials, but it does so in an unsafe manner that enables for unwanted monitoring and/or extraction. 

#### Exploitation

When editing the user profile, one can simply change the field in the URL corresponding to the user's ID to an ID of another user that exists, accessing, henceforth this user's profile editing page.

![](https://cdn.discordapp.com/attachments/852109272262770710/1042649066900832277/editotheruser.gif)

#### Counteraction

As previously referenced, the URL contains a field relative to the user's ID, this is because the current user's ID is passed as an argument in the routing system, as such:

```python
@prof.route('/edit_profile/<id>', methods=['Post'])
@login_required
def edit_profile(id): 
```

To counteract this, this page's URL has its ID field dropped and this argument is omitted, not being taken in consideration any longer, making it impossible for a given user to access any other editing page that would be able to alter third party data, like so:

```python
@prof.route('/edit_profile', methods=['POST'])
@login_required
def edit_profile():
```

### CWE-434 - Unrestricted Upload of File with Dangerous Type

#### Abstract

The software enables the upload or transfer of risky file types that can be automatically processed within the environment of the product. 

#### Exploitation

When editing the user's profile the site allows for the uploading of a file, intended only to be of the PNG or JPEG file type. This condition is left to the user's good will, which means a bad actor could upload a dangerous file type that could jeopardize the normal workflow of the application.

In the following example, the user inputs a JPG type file and the system, predictably, accepts it.

![](https://cdn.discordapp.com/attachments/852109272262770710/1042642931279990905/changeppic.gif)

#### Counteraction

To counter this, we used a simple guard clause to impede an upload of any other file type that isn't PNG/JPEG:

```python
if image and not image.filename.endswith('.png') and not image.filename.endswith('.jpeg'):
    flash('Please upload a png or jpeg image.')
    return redirect(url_for('profile.edit_profile'))
```

This is the system's behaviour after this change:

![](https://cdn.discordapp.com/attachments/852109272262770710/1042657675688808530/changeppicsafe.gif)

____ 

## 4. Final Considerations
