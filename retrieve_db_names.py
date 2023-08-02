#PySpark script to check if some columns (desired columns) from S/4 HANA exists in CDL tables inside
#of CDL DB

desiredColumns = ["LTRMP", "STPOZ", "CUMLM", "VALID_TO", "VGW01", "CINSM", "IBLNR",
                  "IDNRK", "LGMNG", "FKBTX", "ZTNOR", "PAMNG", "DESCRIPTION", "VGW03",
                  "RFAREA", "CSPEM", "IEDZ", "MEINH", "ZZ1_START_PLANT_PRD", "ATWTB", "AUFPL", "MEINS", "BUTXT"]
databases = ["dev_cmo_poc", "dev_hm2", "dev_hmd", "dev_hx2", "dev_hxn",
             "dev_np_silver", "l1_view", "pqa_hm2", "pqa_hmd", "qa_9jc", "qa_9jr", "qa_9p0", "qa_fsn"]
database_names_dict = {col: set() for col in desiredColumns}

# Function to check if the desired column is present in a table
def check_column_in_table(database, table, desiredColumn):
    try:
        cols = spark.table(f"{database}.{table}").columns
        return desiredColumn in cols
    except Exception:
        return False

# Loop through each database and retrieve the tables for each desired column
for desiredColumn in desiredColumns:
    for databaseName in databases:
        database = spark.sql(f"show tables in {databaseName} ").collect()
        for row in database:
            if check_column_in_table(databaseName, row.tableName, desiredColumn):
                database_names_dict[desiredColumn].add(databaseName)
                break  # Break after finding the column in one table to avoid unnecessary checks

# Print the databases containing the desired column
for desiredColumn, database_names in database_names_dict.items():
    if database_names:
        print(f"{desiredColumn}: {', '.join(database_names)}")
    else:
        print(f"{desiredColumn}: NO")
