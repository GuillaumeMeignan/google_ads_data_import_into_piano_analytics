1. Configure the new Piano Analytics measurement import: you can find my personal configuration below.

![image](https://github.com/user-attachments/assets/673f1259-f3c8-4f6d-a70d-ca03c8e7ac31)
![image](https://github.com/user-attachments/assets/909b1b79-7823-4abf-a05c-0f0599dfc031)

2. Extract your data from Google Ads: you can start with at least the spend, impressions, clicks, and conversions per date, campaign ID, and ad group ID.
   
3. Then, build your CSV file and make sure you have:
   - a YYYY-MM-DD format for the date
   - a float format for spend
   - an integer format for impressions, clicks, and conversions
   - remove the table headers (first row)
  
<img width="752" alt="Capture d’écran 2024-10-24 à 13 45 08" src="https://github.com/user-attachments/assets/88d35e89-9943-43a8-b3e6-046684050e7f">

4. Complete the Python script to adapt it to your Piano Analytics configuration.

PS : I use the ‘src_campaign’ property in Piano Analytics for Google Ads campaign identifiers and the ‘src_variant’ property for Google Ads ad group identifiers.
