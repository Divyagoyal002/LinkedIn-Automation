from apscheduler.schedulers.blocking import BlockingScheduler
from generate_post import generate_linkedin_post

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', days=2)
def scheduled_post_job():
    print("[⏰] Running scheduled post job...")
    generate_linkedin_post()

if __name__ == "__main__":
    print("[🟢] Scheduler started.")
    scheduler.start()
