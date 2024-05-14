########################### IMPORT ##########################
#################################################################################
import sqlite3
from sqlite3 import Error
import csv
import os


######################################################################

class GIAPII_db():
    ############### DO NOT MODIFY THIS SECTION ###########################
    ######################################################################
    def create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            connection.text_factory = str
        except Error as e:
            print("Error occurred: " + str(e))

        return connection

    def execute_query(self, connection, query):
        cursor = connection.cursor()
        try:
            if query == "":
                return "Query Blank"
            else:
                cursor.execute(query)
                connection.commit()
                return "Query executed successfully"
        except Error as e:
            return "Error occurred: " + str(e)

    ######################################################################
    ######################################################################

    # Tables
    def school_detail(self, connection):
        ############### EDIT SQL STATEMENT ###################################
        sql_1_school_detail = "CREATE TABLE IF NOT EXISTS school_detail (" \
                              "school_no INTEGER PRIMARY KEY NOT NULL," \
                              "school_webpage TEXT NOT NULL," \
                              "school_name    TEXT  NOT NULL," \
                              "school_type    TEXT  DEFAULT "'" "'"," \
                              "domain    TEXT  NOT NULL," \
                              "grade_min  TEXT    DEFAULT "'" "'"," \
                              "grade_max  TEXT    DEFAULT "'" "'"," \
                              "solution  TEXT   NOT NULL," \
                              "solution_type TEXT   NOT NULL" \
                              ");"
        # print("made school_detail")
        return self.execute_query(connection, sql_1_school_detail)
        ######################################################################

    ###IMPORT###
    def import_school_detail(self, connection, path):
        ############### school ############################
        # sql_test = "SELECT * FROM school;"
        # cursor = connection.execute(sql_test)
        # print(cursor.fetchall()[0][0])
        insert_1_school_detail = "INSERT INTO school_detail (school_webpage,school_name,school_type,domain" \
                                 ",grade_min,grade_max,solution, solution_type) VALUES (?,?,?,?,?,?,?,?);"
        # path.encode("utf-8")
        with open(path, mode='r', encoding="utf8") as school_detail_csv_file:
            read_csv = csv.reader(school_detail_csv_file)
            next(read_csv)
            for col in read_csv:
                # print(col)
                # print(col[1:-1])
                # print(col[-1])
                # print(len(col))
                # print(col[1:])
                connection.execute(insert_1_school_detail, col[1:])
                connection.commit()
        ######################################################################

        # sql = "SELECT * FROM school;"
        # print(connection.execute(sql).fetchall())
        return None
        ######################################################################

    def solution(self, connection):
        ############### EDIT SQL STATEMENT ###################################
        sql_2_solution = "CREATE TABLE IF NOT EXISTS solution (" \
                         "solution_no INTEGER NOT NULL PRIMARY KEY," \
                         "solution   TEXT  NOT NULL," \
                         "school_name    TEXT  NOT NULL," \
                         "solution_type  TEXT  NOT NULL" \
                         ");"
        self.execute_query(connection, sql_2_solution)
        print("table was created")
        ############### IMPORT FROM school ############################
        ############### solution is vert partition of school
        insert_2_solution = "INSERT INTO solution (" \
                            "solution, school_name, solution_type)" \
                            "select distinct solution, school_name, solution_type" \
                            " from school_detail;"
        self.execute_query(connection, insert_2_solution)
        #
        # sql = "SELECT * FROM solution;"
        # cursor = connection.execute(sql)
        return None  # cursor.fetchall()

        ######################################################################

    def school_type(self, connection):
        ############### EDIT SQL STATEMENT ###################################
        sql_3_school_type = "CREATE TABLE IF NOT EXISTS school_type (" \
                            "seq_no INTEGER NOT NULL PRIMARY KEY," \
                            "grade TEXT  NOT NULL," \
                            "school_type TEXT  NOT NULL" \
                            ");"
        return self.execute_query(connection, sql_3_school_type)
        ######################################################################

    ###IMPORT###
    def import_school_type(self, connection, path):
        ############### school ############################
        insert_3_school_type = "INSERT INTO school_type (grade, school_type) VALUES (?,?)"
        # path.encode("utf-8")
        with open(path, mode='r', encoding="utf8") as school_type_csv_file:
            read_csv = csv.reader(school_type_csv_file)
            next(read_csv)
            for col in read_csv:
                # print(col)
                # print(col[1:-1])
                connection.execute(insert_3_school_type, col[1:])
                connection.commit()
        ######################################################################

        # sql = "SELECT * FROM school_type;"
        # cursor = connection.execute(sql)
        return None  # cursor.fetchall()[0][0]
        ######################################################################

    def subject_domain(self, connection):
        ############### EDIT SQL STATEMENT ###################################
        sql_4_subject_domain = "CREATE TABLE IF NOT EXISTS subject_domain (" \
                               "seq_no INTEGER NOT NULL PRIMARY KEY," \
                               "course    TEXT  NOT NULL," \
                               "domain    TEXT  NOT NULL" \
                               ");"
        return self.execute_query(connection, sql_4_subject_domain)
        ######################################################################

    ###IMPORT###
    def import_subject_domain(self, connection, path):
        insert_4_subject_domain = "INSERT INTO subject_domain (course, domain) VALUES (?,?)"
        # path.encode("utf-8")
        with open(path, mode='r', encoding="utf8") as subject_domain_csv_file:
            read_csv = csv.reader(subject_domain_csv_file)
            next(read_csv)
            for col in read_csv:
                # print(col)
                # print(col[1:-1])
                connection.execute(insert_4_subject_domain, col[1:])
                connection.commit()
        ######################################################################

        # sql = "SELECT * FROM subject_grade;"
        # cursor = connection.execute(sql)
        return None  # cursor.fetchall()[0][0]
        ######################################################################

    def solution_research(self, connection):
        ############### EDIT SQL STATEMENT ###################################
        sql_5_solution_research = "CREATE TABLE IF NOT EXISTS solution_research (" \
                                  "school_name    TEXT  NOT NULL," \
                                  "solution  TEXT   NOT NULL," \
                                  "research_page TEXT    DEFAULT "'"N/A"'"," \
                                  "PRIMARY KEY (school_name, solution, research_page)" \
                                  ");"

        return self.execute_query(connection, sql_5_solution_research)
        ######################################################################

    ###IMPORT###
    def import_solution_research(self, connection, path):
        insert_5_solution_research = "INSERT INTO solution_research (school_name, solution, research_page) VALUES (?,?,?)"
        # path.encode("utf-8")
        with open(path, mode='r', encoding="utf8") as solution_research_csv_file:
            read_csv = csv.reader(solution_research_csv_file)
            next(read_csv)
            for col in read_csv:
                connection.execute(insert_5_solution_research, col[1:])
                connection.commit()
        ######################################################################

        # sql = "SELECT * FROM solution_research;"
        # cursor = connection.execute(sql)
        return None  # cursor.fetchall()[0][0]
        ######################################################################
        # startpaste

    def academic_planning_guides(self, connection):
        ############### EDIT SQL STATEMENT ###################################
        sql_6_subject_domain = "CREATE TABLE IF NOT EXISTS subject_domain (" \
                               "state_jurisdiction TEXT  NOT NULL," \
                               "local_district		TEXT  NOT NULL," \
                               "organization       TEXT  NOT NULL," \
                               "link               TEXT  NOT NULL," \
                               "grade_range        TEXT  NOT NULL," \
                               "type               TEXT  NOT NULL," \
                               "tag                TEXT  NOT NULL," \
                               "tag2               TEXT  NOT NULL," \
                               "giapii_rating      INTEGER  NOT NULL" \
                               "PRIMARY KEY (organization, grade_range, tag)" \
                               ");"
        return self.execute_query(connection, sql_6_subject_domain)
        ######################################################################

    ###IMPORT###
    def import_academic_planning_guides(self, connection, path):
        insert_6_subject_domain = "INSERT INTO academic_planning_guides " \
                                  " (state_jurisdiction, local_district, organization, link, grade_range, type, tag" \
                                  ", tag2, giapii_rating) VALUES (?,?,?,?,?,?,?,?,?)"
        # path.encode("utf-8")
        with open(path, mode='r', encoding="utf8") as subject_domain_csv_file:
            read_csv = csv.reader(subject_domain_csv_file)
            next(read_csv)
            for col in read_csv:
                # print(col)
                # print(col[1:-1])
                connection.execute(insert_6_subject_domain, col[1:])
                connection.commit()
        ######################################################################

        # sql = "SELECT * FROM subject_grade;"
        # cursor = connection.execute(sql)
        return None  # cursor.fetchall()[0][0]
        ######################################################################

    ##########  create views  ####################################

    # Create Indexes [1 points]
    def idx_school_detail(self, connection):
        sql_1_school_detail_idx = "CREATE INDEX ""movie_index"" ON ""movies""" \
                                  "(""id"");"
        return self.execute_query(connection, sql_1_school_detail_idx)
        ######################################################################

    def idx_solution(self, connection):
        sql_2_solution_idx = "CREATE INDEX ""cast_index"" ON ""movie_cast""" \
                             "(""cast_id"");"
        return self.execute_query(connection, sql_2_solution_idx)
        ######################################################################

    def idx_school_type(self, connection):
        sql_3_school_type_idx = "CREATE INDEX ""cast_bio_index"" ON ""cast_bio""" \
                                "(""cast_id"");"
        return self.execute_query(connection, sql_3_school_type_idx)
        ######################################################################

    def idx_subject_grade(self, connection):
        sql_4_subject_grade_idx = "CREATE INDEX ""cast_bio_index"" ON ""cast_bio""" \
                                  "(""cast_id"");"
        return self.execute_query(connection, sql_4_subject_grade_idx)

    def idx_solution_research(self, connection):
        sql_5_solution_research_idx = "CREATE INDEX ""cast_bio_index"" ON ""cast_bio""" \
                                      "(""cast_id"");"
        return self.execute_query(connection, sql_5_solution_research_idx)
        ######################################################################
        # endpaste


if __name__ == "__main__":
    #################################################################################
    print("are we here?")
    print("this is my working directory: ", os.getcwd())
    print("what is in the directory: ", os.listdir())
    # print("and now")
    # dir = r"C:\Users\thom015\OneDrive - INFICON GmbH\Documents\Georgia Tech\CS-6460 - O01 - Education Technology\Project"
    # # print("\n", os.chdir(dir))
    # # os.chdir(dir)
    folder = r"C:\Users\thom015\OneDrive - INFICON GmbH\Documents\Georgia Tech\CS-6460 - O01 - Education Technology\Project\DB\csv_source"
    # dest = r"Formatted Dummy"
    # print("this is my working directory: ", os.getcwd())
    # print("what is in the directory: ", os.listdir())
    print('starting dB')
    db = GIAPII_db()

    try:
        conn = db.create_connection("GIAPII_20220723")
    except:
        print("Database Creation Error")

    try:
        conn.execute("DROP TABLE IF EXISTS school_detail;")
        conn.execute("DROP TABLE IF EXISTS solution;")
        conn.execute("DROP TABLE IF EXISTS school_type;")
        conn.execute("DROP TABLE IF EXISTS subject_domain;")
        conn.execute("DROP TABLE IF EXISTS solution_research;")
        conn.execute("DROP TABLE IF EXISTS academic_planning_guides;")
        conn.execute("DROP TABLE IF EXISTS iap_guidelines;")
        conn.execute("DROP TABLE IF EXISTS iap_guidelines_resources;")
        conn.execute("DROP VIEW IF EXISTS user_view;")
        print("check table creation")
    except:
        print("Error in Table Drops")

    # tb1 creation
    try:
        db.school_detail(conn)
        print("school_detail table should exist")
    except Exception as e:
        print("create school_detail failed: ", e)

    # tb1 import
    try:
        db.import_school_detail(conn, "csv_source/school_detail_v3.csv")
        print("school_detail should be populated")
    except Exception as e:
        print("Error with school_detail import: ", e)

    # tb2 creation
    try:
        db.solution(conn)
        print("solution table should exist")
    except:
        print("solution failed")

    # tb3 creation
    try:
        db.school_type(conn)
        print("school type table should exist")
    except:
        print("create school type failed")

    # tb3 import
    try:
        db.import_school_type(conn, "csv_source/school_type_v2.csv")
        print("school type should be populated")
    except Exception as e:
        print("Error with school type import: ", e)

    # tb4 creation
    try:
        db.subject_domain(conn)
        print("subject_domain table should exist")
    except:
        print("create subject_domain failed")

    # tb4 import
    try:
        db.import_subject_domain(conn, "csv_source/subject_domain.csv")
        print("subjects should be populated")
    except Exception as e:
        print("Error with subjects import: ", e)

    # tb5 creation
    try:
        db.solution_research(conn)
        print("solution research table should exist")
    except:
        print("create solution research failed")

    # tb5 import
    try:
        db.import_solution_research(conn, "csv_source/solution_research.csv")
        print("solution_research should be populated")
    except Exception as e:
        print("Error with solution research import: ", e)

    # tb6 creation
    try:
        db.academic_planning_guides(conn)
        print("academic_planning_guides table should exist")
    except:
        print("create academic_planning_guides failed")

    # tb6 import
    try:
        db.import_academic_planning_guides(conn, "csv_source/academic_planning_guides.csv")
        print("academic_planning_guides should be populated")
    except Exception as e:
        print("Error with academic_planning_guides import: ", e)

    # tb7 creation
    try:
        db.iap_guidelines(conn)
        print("iap_guidelines table should exist")
    except:
        print("create iap_guidelines failed")

    # tb7 import
    try:
        db.import_iap_guidelines(conn, "csv_source/guidelines_IAP_v4.csv")
        print("iap_guidelines should be populated")
    except Exception as e:
        print("Error with iap_guidelines import: ", e)

    # tb8 creation
    try:
        db.iap_guidelines_resources(conn)
        print("iap_guidelines table should exist")
    except:
        print("create iap_guidelines_resources failed")

    # tb8 import
    try:
        db.import_iap_guidelines_resources(conn, "csv_source/guidelines_IAP_resources_v2.csv")
        print("iap_guidelines should be populated")
    except Exception as e:
        print("Error with iap_guidelines_resources import: ", e)

    conn.close()
    #################################################################################
    #################################################################################
