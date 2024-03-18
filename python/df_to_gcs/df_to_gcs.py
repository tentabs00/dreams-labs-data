def df_to_gcs(
        df
        ,filename
    ):
    '''
    uploads a df to google cloud storage
    param: df <dataframe> the dataframe to be uploaded
    param: filename <string> the complete filename including ".csv"
    '''
    current_date_string = datetime.datetime.now().strftime('%Y%m%d')
    filename_full = filename + '_' + current_date_string + '.csv'

    client = storage.Client(project='dreams-labs-data')
    bucket = client.get_bucket('dreams-labs-storage')

    blob = bucket.blob(filename)
    blob.upload_from_string(df.to_csv(index = False),content_type = 'csv')

    print('Uploaded '+filename)