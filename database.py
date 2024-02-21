
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
import os

myconn = mysql.connector.connect(host =os.getenv("HOST"),user = os.getenv("USER"),passwd = os.getenv("PASSWORD") ,database = os.getenv("DATABASE"))
cur = myconn.cursor()




def load_jobs():
    sql = "select *from carrer_website.carrer"
    cur.execute(sql)
    jobs =[]
    result = cur.fetchall()
    for res in result:
        res = list(res)
        temp ={
            'id':res[0],
            'title':res[1].title(),
            'location':res[2].title(),
            'salary':res[3],
            'currency':res[4],
            'responsibilty':res[5],
            'requirements':res[6]

        }
        jobs.append(temp)

    
    return jobs


def load_job_id(id):
    
    sql = f"select *from carrer_website.carrer where id = {id}"
    cur.execute(sql)

    job = cur.fetchone()

    res = list(job)
    
    tempk = {
            'id':res[0],
            'title':res[1].title(),
            'location':res[2],
            'salary':res[3],
            'currency':res[4],
            'responsibilty':res[5],
            'requirements':res[6]

    }
    return tempk
    

def add_application_to_db(job_id ,data):
    
    query = "Insert into carrer_website.applications(job_id ,full_name ,email ,linkedin_url ,education ,work_experience ,resume_url) values(%s ,%s,%s,%s,%s,%s,%s)"
    
    val = (job_id  ,data['full_name'],data['email'],data['linkedIn_url'],data['education'] ,data['work_experience'],data['resume_url'])
    cur.execute(query,val)

    myconn.commit()

    
    




    











    



