import asyncio
from time import sleep

sent_count = 0

async def send_mail(to: str, body: str) :
    global sent_count
    sent_count += 1
    print(f"email sending... to:{to}, body: {body}")
    sleep(2)
    print(f"total {sent_count} mail sent.....")

if __name__ == "__main__": 
    asyncio.run(send_mail('eric','hllow eokd'))