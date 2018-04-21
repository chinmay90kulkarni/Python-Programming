from crontab import CronTab

my_cron=CronTab(user=True);

job=my_cron.new(command="python ./APPRemainder.py");
job.minute.every(1);

my_cron.write("user.txt");




