from flask import Flask
import sqlite3

app = Flask(__name__)


@app.route('/jobs/<variable>', methods=['GET'])
def jobs_location(variable):
    variable = variable.replace('_', ' ')
    conn = sqlite3.connect(r"C:\sqlite\db\jobs.db")
    mycursor = conn.cursor()
    mycursor.execute(f"SELECT vacancy, team, types.type, locations.name FROM jobs INNER JOIN locations ON jobs.locationId=locations.id \
                        INNER JOIN types ON types.id=jobs.employmentId WHERE locations.name='{variable}'")
    myresult = mycursor.fetchall()
    conn.close()
    return "\n".join([", ".join(x) for x in myresult])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
