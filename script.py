


# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
 
#     return os.path.join(base_path, relative_path)

# logger.add("file_{time:YYYY-MM-DD}.log", rotation="500 MB", level="TRACE")

# gc = gs.service_account(filename=resource_path('spreedsheet.json'))
# sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1iqa97QhQNCEpFGO0uqYIVEBO36rBh2eH4YXAWYCwki4/edit#gid=0')

# # Example initialization
# track_df = pd.DataFrame(columns=['phone_no', 'message', 'status', 'datetime'])    

# def date_difference(date_str1, date_str2):
#     date_format = "%d-%m-%Y"
#     date1 = datetime.strptime(date_str1, date_format)
#     date2 = datetime.strptime(date_str2, date_format)

#     date_difference = date2 - date1
#     return date_difference.days

# def add_row_to_dataframe(dataframe, new_row_dict):
#     # If the DataFrame is empty, create it with columns using the keys of the new row dictionary
#     if dataframe.empty:
#         dataframe = pd.DataFrame(columns=new_row_dict.keys())
    
#     # Get the current index count to determine the index for the new row
#     index = len(dataframe)
    
#     # Use loc to add the new row at the end
#     dataframe.loc[index] = new_row_dict
    
#     return dataframe


# @logger.catch()
# def sent_messages(phone_number,message):
#     message = message.replace('\n', '%0a')
#     try:
#         url = 'https://web.whatsapp.com/send?phone={}&text={}'.format(phone_number, str(message))
#         sent = False
#         # It tries 3 times to send a message in case there is any error
#         driver.get(url)
#         #time.sleep(25)
#         try:
#             click_btn = WebDriverWait(driver, 120).until(
#                 EC.element_to_be_clickable((By.CLASS_NAME, '_3XKXx')))
#         except Exception as e:
#             print("Sorry, the message could not be sent to ", phone_number)
#             logger.warning("Sorry, the message could not be sent to {}", format(phone_number))
#             status = "Failed"
#         else:
#             time.sleep(2)
#             click_btn.click()
#             sent = True
#             time.sleep(5)
#             print('Message sent to:', phone_number)
#             logger.success('Message sent to: {}', format(phone_number))
#             status = "Complete"
#     except Exception as e:
#         print('Failed to send message to ', phone_number)
#         logger.error('Failed to send message to {}', format(phone_number))
#         status = "Failed"
#     return status
        
# def replace_placeholders(file_path, **kwargs):
    
#     # Open the text file
#     with open(file_path, 'r') as file:
#         # Read the entire content of the file
#         content = file.read()
    
#     # Replace the placeholders with values
#     content = content.format(**kwargs)
    
#     return content

# def check_date_format(df, column_names, expected_format="%d-%m-%Y"):

#     result = {}

#     # Function to check if a date string matches the expected format
#     def check_date(date_str):
#         try:
#             datetime.strptime(date_str, expected_format)
#             return True
#         except ValueError:
#             return False

#     # Check each date in each column
#     for column_name in column_names:
#         date_column = df[column_name]
#         all_dates_match = all(check_date(date_str) for date_str in date_column)
#         result[column_name] = all_dates_match

#     return result

# def add_row_to_dataframe(dataframe, new_row_dict):
    
#     # Get the current index count to determine the index for the new row
#     index = len(dataframe)
    
#     # Use loc to add the new row at the end
#     dataframe.loc[index] = new_row_dict
    
#     return dataframe

# if st.button("Open WhatsApp"):     
#     options = webdriver.ChromeOptions()
#     # You may need to specify the path to your Chrome executable if it's not in your system PATH
#     # options.binary_location = 'path/to/chrome.exe' 
#     driver = webdriver.Chrome(options=options)
#     driver.get('https://web.whatsapp.com')
#     st.write("Press Start after logging into Whatsapp Web and your chats are visible.")

#     if st.button("Start"):

#         current_date = datetime.now()

#         curr_date = current_date.strftime("%d-%m-%Y")

#         # Format the datetime object as "Month day"
#         formatted_month = current_date.strftime("%b")
#         formatted_date = current_date.strftime("%d")
#         sheet_name = f"{formatted_month} {int(formatted_date)}"

#         ws = sh.worksheet(sheet_name)
#         df = pd.DataFrame(ws.get_all_records())

#         df = df[df['send_text'] == "TRUE"]
#         # Remove rows with empty values
#         df.dropna(subset=['Interview line up date'], inplace=True)
#         columns_to_check = ['Interview line up date', 'Number', 'Name', 'conversation Date']
#         df = df.loc[~df[columns_to_check].eq('').all(axis=1)]

#         ## check date time format
#         date_columns = ['conversation Date', 'Interview line up date']

#         date_format_results = check_date_format(df, date_columns)

#         for column_name, matches_format in date_format_results.items():
#             if matches_format:
#                 pass
#             else:
#                 logger.error(f"Some dates in column '{column_name}' do not match the expected format: day-month-year (e.g., 06-02-2024)")
#                 time.sleep(10)
#                 sys.exit()
                
#         # start texting
#         for i in range(len(df)):
#             datetime = datetime.now()
            
#             conversion_date = df.iloc[i]['conversation Date']
#             interview_date = df.iloc[i]['Interview line up date']
#             cname = df.iloc[i]['Name']
#             rname = df.iloc[i]['Recruiter Name']
#             desi = df.iloc[i]['Designation']
#             company_name = df.iloc[i]['Company Name']

            
#             if date_difference(curr_date, interview_date) == 1:
                
#                 file_path = resource_path("text_template/tomorrow_temp.txt")
#                 text = replace_placeholders(file_path,
#                                                         candidate_name = cname,
#                                                         final_line_up_at_company = company_name)
                
#                 value = sent_messages(df.iloc[i]['Number'], text)
                
#                 row = { 'phone_no': df.iloc[i]['Number'], 'message': text, 'status': value, 'datetime': datetime}
                
#                 #track_df = track_df.append(row, ignore_index= True)
#                 track_df = add_row_to_dataframe(track_df, row)
                
#                 track_df.to_csv("wp_auto_track.csv",index = False)
                
#             elif date_difference(curr_date, interview_date) == 0:
                
#                 file_path = resource_path("text_template/today_temp.txt")
#                 text = replace_placeholders(file_path,
#                                                         candidate_name = cname,
#                                                         final_line_up_at_company = company_name)
                
#                 value = sent_messages(df.iloc[i]['Number'], text)
                
#                 row = { 'phone_no': df.iloc[i]['Number'], 'message': text, 'status': value, 'datetime': datetime }
                
#                 #track_df = track_df.append(row, ignore_index= True)
#                 track_df = add_row_to_dataframe(track_df, row)
                
#                 track_df.to_csv("wp_auto_track.csv",index = False)
            
#             else:
#                 if date_difference(conversion_date, curr_date) == 1:
                    
#                     file_path = resource_path('text_template/1st_round_temp.txt')
#                     text = replace_placeholders(file_path,
#                                                             candidate_name = cname,
#                                                             recruiter_name = rname,
#                                                             conversation_date = conversion_date,
#                                                             interview_line_up_date = interview_date,
#                                                             designation = desi,
#                                                             final_line_up_at_company = company_name)
#                     # text = "yes"
#                     # print("yes")
                    
#                     value = sent_messages(df.iloc[i]['Number'], text)
                    
#                     row = { 'phone_no': df.iloc[i]['Number'], 'message': text, 'status': value, 'datetime': datetime }
                    
#                     #track_df = track_df.append(row, ignore_index= True)
#                     track_df = add_row_to_dataframe(track_df, row)
                    
#                     track_df.to_csv("wp_auto_track.csv",index = False)
                    
#                 elif date_difference(conversion_date, curr_date) > 1 and date_difference(curr_date, interview_date) > 1:
                    
#                     file_path = resource_path('text_template/gen_temp.txt')
#                     text = replace_placeholders(file_path,
#                                                             candidate_name = cname,
#                                                             interview_line_up_date = interview_date,
#                                                             final_line_up_at_company = company_name)
                    
                    
#                     value = sent_messages(df.iloc[i]['Number'], text)
                    
#                     row = { 'phone_no': df.iloc[i]['Number'], 'message': text, 'status': value, 'datetime': datetime }
                    
#                     #track_df = track_df.append(row, ignore_index= True)
#                     track_df = add_row_to_dataframe(track_df, row)
                    
#                     track_df.to_csv("wp_auto_track.csv",index = False)
                    
#             if i == len(df) - 1:
#                 logger.info("going to sleep for 30 seconds")
#                 print("please wait for 30 seconds")
#                 time.sleep(30)
                
#         error_df = track_df[track_df['status'] == "Failed"]        
#         if len(error_df)>0:
#             for i in range(len(error_df)):
#                 value = sent_messages(error_df.iloc[i]['phone_no'], error_df.iloc[i]['message'])
                
#                 track_df.loc[track_df['phone_no'] == error_df.iloc[i]['phone_no'], 'message'] = "Complete"
#                 track_df.to_csv("wp_auto_track.csv",index = False)

#         driver.quit()
#         print("The script executed successfully.")     
#         logger.success("The script executed successfully.") 

# def sent_messages(phone_number,message):
#     message = message.replace('\n', '%0a')
#     try:
#         url = 'https://web.whatsapp.com/send?phone={}&text={}'.format(phone_number, str(message))
#         sent = False
#         # It tries 3 times to send a message in case there is any error
#         driver.get(url)
#         #time.sleep(25)
#         try:
#             click_btn = WebDriverWait(driver, 120).until(
#                 EC.element_to_be_clickable((By.CLASS_NAME, '_3XKXx')))
#         except Exception as e:
#             print("Sorry, the message could not be sent to ", phone_number)
#             logger.warning("Sorry, the message could not be sent to {}", format(phone_number))
#             status = "Failed"
#         else:
#             time.sleep(2)
#             click_btn.click()
#             sent = True
#             time.sleep(5)
#             print('Message sent to:', phone_number)
#             logger.success('Message sent to: {}', format(phone_number))
#             status = "Complete"
#     except Exception as e:
#         print('Failed to send message to ', phone_number)
#         logger.error('Failed to send message to {}', format(phone_number))
#         status = "Failed"
#     return status

# if st.button("Open WhatsApp"):     
#     options = webdriver.ChromeOptions()
#     # You may need to specify the path to your Chrome executable if it's not in your system PATH
#     # options.binary_location = 'path/to/chrome.exe' 
#     driver = webdriver.Chrome(options=options)
#     driver.get('https://web.whatsapp.com')
#     st.write("Press Start after logging into Whatsapp Web and your chats are visible.")
    
#     if st.button("Start"):
#         url = 'https://web.whatsapp.com/send?phone={}&text={}'.format(7679735335, str("hello"))
#         driver.get(url)
#         #sent_messages('7679735335','hellow')
#         time.sleep(10)


# streamlit_app.py

import streamlit as st
import pywhatkit as kit




import streamlit as st

# Display a time input widget
from datetime import datetime

# Get the current time

if st.button("Send WhatsApp Message"):
    st.write("Sending WhatsApp message...")
    current_time = datetime.now().time()
    current_hour = current_time.hour
    current_minute = current_time.minute
    # Display the selected time
    st.write("Your textwill be deliver at:", current_hour,current_minute+1)
    # Send a WhatsApp Message to a Contact at 1:30 PM
    kit.sendwhatmsg("+917679735335", "Hi", current_hour, current_minute+1,20)
