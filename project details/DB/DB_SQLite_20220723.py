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
                              "solution_type TEXT   NOT NULL," \
                              "curriculum_type TEXT   NOT NULL" \
                              ");"
        return self.execute_query(connection, sql_1_school_detail)
        ######################################################################

    ###IMPORT###
    def import_school_detail(self, connection, path):
        ############### school ############################
        # sql_test = "SELECT * FROM school;"
        # cursor = connection.execute(sql_test)
        # print(cursor.fetchall()[0][0])
        insert_1_school_detail = "INSERT INTO school_detail (school_webpage,school_name,school_type,domain" \
                                 ",grade_min,grade_max,solution, solution_type, curriculum_type) " \
                                 "VALUES (?,?,?,?,?,?,?,?,?);"
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
        return None  # cursor.fetchall()[0][0]
        ######################################################################
        # startpaste

    def academic_planning_guides(self, connection):
        ############### EDIT SQL STATEMENT ###################################
        sql_6_subject_domain = "CREATE TABLE IF NOT EXISTS academic_planning_guides (" \
                               "state_jurisdiction TEXT  NOT NULL," \
                               "local_district		TEXT  NOT NULL," \
                               "organization       TEXT  NOT NULL," \
                               "link               TEXT  NOT NULL," \
                               "grade_range        TEXT  NOT NULL," \
                               "type               TEXT  NOT NULL," \
                               "tag                TEXT  NOT NULL," \
                               "giapii_rating      INTEGER  NOT NULL," \
                               "PRIMARY KEY (local_district, organization, grade_range, tag)" \
                               ");"
        return self.execute_query(connection, sql_6_subject_domain)
        ######################################################################

    ###IMPORT###
    def import_academic_planning_guides(self, connection, path):
        insert_6_academic_planning_guides = "INSERT INTO academic_planning_guides " \
                                  " (state_jurisdiction, local_district, organization, link, grade_range, type, tag" \
                                  ", giapii_rating) VALUES (?,?,?,?,?,?,?,?)"
        # path.encode("utf-8")
        with open(path, mode='r', encoding="utf8") as academic_planning_guides_csv_file:
            read_csv = csv.reader(academic_planning_guides_csv_file)
            next(read_csv)
            for col in read_csv:
                # print(col)
                # print(col[1:-1])
                connection.execute(insert_6_academic_planning_guides, col[1:])
                connection.commit()
        ######################################################################
        return None  # cursor.fetchall()[0][0]
        ######################################################################

    def iap_guidelines(self, connection):
        ############### EDIT SQL STATEMENT ###################################
        sql_7_iap_guidelines = "CREATE TABLE IF NOT EXISTS iap_guidelines (" \
                               "section            INTEGER NOT NULL," \
                               "subsection         INTEGER NOT NULL," \
                               "description        TEXT  NOT NULL," \
                               "to_be_completed_by TEXT  NOT NULL," \
                               "more_information   TEXT  NOT NULL," \
                               "PRIMARY KEY (section, subsection)" \
                               ");"
        return self.execute_query(connection, sql_7_iap_guidelines)
        ######################################################################

    ###IMPORT###
    def import_iap_guidelines(self, connection, path):
        insert_7_iap_guidelines = "INSERT INTO iap_guidelines " \
                                  " (section, subsection, description, to_be_completed_by, more_information" \
                                  ") VALUES (?,?,?,?,?)"
        # path.encode("utf-8")
        with open(path, mode='r', encoding="utf8") as iap_guidelines_csv_file:
            read_csv = csv.reader(iap_guidelines_csv_file)
            next(read_csv)
            for col in read_csv:
                # print(col)
                # print(col[1:-1])
                connection.execute(insert_7_iap_guidelines, col[1:])
                connection.commit()
        ######################################################################
        return None
        ######################################################################

    def iap_guidelines_resources(self, connection):
        ############### EDIT SQL STATEMENT ###################################
        sql_8_iap_guidelines_resources = "CREATE TABLE IF NOT EXISTS iap_guidelines_resources (" \
                               "seq_no             INTEGER NOT NULL," \
                               "section            INTEGER NOT NULL," \
                               "subsection         INTEGER NOT NULL," \
                               "description        TEXT  NOT NULL," \
                               "reference          TEXT  NOT NULL," \
                               "PRIMARY KEY (seq_no, section, subsection)" \
                               ");"
        return self.execute_query(connection, sql_8_iap_guidelines_resources)
        ######################################################################

    ###IMPORT###
    def import_iap_guidelines_resources(self, connection, path):
        insert_8_iap_guidelines_resources = "INSERT INTO iap_guidelines_resources " \
                                  " (seq_no, section, subsection, description, reference" \
                                  ") VALUES (?, ?,?,?,?)"
        # path.encode("utf-8")
        with open(path, mode='r', encoding="utf8") as iap_guidelines_resources_csv_file:
            read_csv = csv.reader(iap_guidelines_resources_csv_file)
            next(read_csv)
            for col in read_csv:
                # print(col)
                # print(col[1:-1])
                connection.execute(insert_8_iap_guidelines_resources, col[:])
                connection.commit()
        ######################################################################
        return None
        ######################################################################

    ##########  create views  ####################################

    # Create Indexes
    def idx_school_detail_1(self, connection):
        sql_1_school_detail_idx_1 = "CREATE INDEX ""idx_school_1"" ON ""school_detail""" \
                                  "(""school_no"");"
        return self.execute_query(connection, sql_1_school_detail_idx_1)
        ######################################################################
    def idx_school_detail_2(self, connection):
        sql_2_school_detail_idx_2 = "CREATE INDEX ""idx_school_2"" ON ""school_detail""" \
                                  "(""school_no, school_name, solution"");"
        return self.execute_query(connection, sql_2_school_detail_idx_2)
        ######################################################################
    def idx_school_detail_3(self, connection):
        sql_3_school_detail_idx_3 = "CREATE INDEX ""idx_school_3"" ON ""school_detail""" \
                                  "(""school_no, school_name, school_type"");"
        return self.execute_query(connection, sql_3_school_detail_idx_3)
        ######################################################################

    def idx_solution_1(self, connection):
        sql_4_solution_idx_1 = "CREATE INDEX ""idx_solution_1"" ON ""solution""" \
                             "(""solution_no"");"
        return self.execute_query(connection, sql_4_solution_idx_1)
        ######################################################################
    def idx_solution_2(self, connection):
        sql_5_solution_idx_2 = "CREATE INDEX ""idx_solution_2"" ON ""solution""" \
                             "(""solution_no, school_name, solution"");"
        return self.execute_query(connection, sql_5_solution_idx_2)
        ######################################################################
    def idx_solution_3(self, connection):
        sql_6_solution_idx_3 = "CREATE INDEX ""idx_solution_3"" ON ""solution""" \
                             "(""solution_no, school_name, solution_type"");"
        return self.execute_query(connection, sql_6_solution_idx_3)
        ######################################################################

    def idx_solution_research_1(self, connection):
        sql_7_solution_research_idx_1 = "CREATE INDEX ""idx_solution_research_1"" ON ""solution_research""" \
                                      "(""school_name, solution, research_page"");"
        return self.execute_query(connection, sql_7_solution_research_idx_1)
        ######################################################################

    def idx_apg_1(self, connection):
        sql_8_apg_idx_1 = "CREATE INDEX ""idx_apg_1"" ON ""academic_planning_guides""" \
                                      "(""local_district, grade_range, tag"");"
        return self.execute_query(connection, sql_8_apg_idx_1)
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
    print("what is in the directory: ", os.listdir("csv_source"))
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
        db.import_academic_planning_guides(conn, "csv_source/academic_planning_guides_v2.csv")
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

    # idx1-8
    try:
        db.idx_school_detail_1(conn)
        print("idx_school_detail_1 should be populated")
        db.idx_school_detail_2(conn)
        print("idx_school_detail_2 should be populated")
        db.idx_school_detail_3(conn)
        print("idx_school_detail_3 should be populated")
        db.idx_solution_1(conn)
        print("idx_solution_1 should be populated")
        db.idx_solution_2(conn)
        print("idx_solution_2 should be populated")
        db.idx_solution_3(conn)
        print("idx_solution_3 should be populated")
        db.idx_solution_research_1(conn)
        print("idx_solution_research_1 should be populated")
        db.idx_apg_1(conn)
        print("idx_idx_apg_1 should be populated")
    except Exception as e:
        print("Error with indexing: ", e)

    conn.close()
    #################################################################################
    #################################################################################
