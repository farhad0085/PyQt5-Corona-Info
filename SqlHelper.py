import sqlite3 as sql
import hashlib, binascii, os

class SqlHelper:
    def __init__(self):
        self.con = sql.connect("userdb.db")
        self.con.execute('''CREATE TABLE IF NOT EXISTS userinfo
                 (USERNAME           TEXT  PRIMARY KEY  NOT NULL,
                 PASSWORD			TEXT NOT NULL,
                 EMAIL           TEXT    NOT NULL,
                 FULLNAME           TEXT    NOT NULL,
                 AGE				TEXT NOT NULL);''')

    def userExist(self, uname):
        cursor = self.con.execute("SELECT username from userinfo")
        prevUnames = []
        for row in cursor:
            prevUnames.append(row[0])
        if uname in prevUnames:
            return True
        else:
            return False

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(self, stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def registerUser(self, username, password, email, fullName, age):
        password = self.hash_password(password)
        if self.userExist(username) == 0:
            self.con.execute("INSERT INTO userinfo VALUES (?, ?, ?, ?, ?)",
                        (username, password, email, fullName, age))
            self.con.commit()
            return True
        else:
            return False

    def checkPassword(self, username, password):
        command = "SELECT password FROM userinfo where USERNAME = '" + username + "'"
        passfromdb = self.con.execute(command)
        pwdActual = ""
        for row in passfromdb:
            pwdActual = row[0]

        if self.verify_password(pwdActual, password):
            return True
        else:
            return False
