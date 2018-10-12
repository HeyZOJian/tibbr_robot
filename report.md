## 1. Key learning, skills and experience acquired
1. Pair with Nickey on monring, we pick up the story that Make shipment extractor not check the create date when re-processing.When re-process all the shipments, we do not filter out the shipments that create date < now - 180.We modify the SQL to add a parameter about the create date. When the job type is auto we just handle the data created in this half year.When the job type is manual we handle all the data.
2. Pair with Carol on afternoon,the story is that cargo description is null in E2EV.Carol shared the backgroud about the ETL to me again, it make me more clearly on this project.
3. Pair with kevin to check the issue about Internal Server Error in App when the brother user login in the App.After check the code and logs,but the logs show few information and we cannot reproduce this error, so we didn't found the special code about this issue,and we just fixed potential nullPointException in the correlative code.
4. Pair with Chris,we add additional rule that when Last leg ETA greater than 60 days from today or Booking ETD on the first leg greater than 180 days from today we update the I/B complete flag to 1 in ref table and  refactor the code to extract the updated operate for ref table.
5. Pair with Amelia to study python together and write a script to auto-post weekly report in tibbr. Actually, this report is post by the script.

## 2. Problem / Confusing / Difficulties
## 3. Other Comments / Suggestion
