from sales_package.test import odooTest
import time

with odooTest() as bot:
    start_time = time.time()
    for i in range(1000):
        bot.first_landing_page()
        if(i == 0):
            bot.enter_email_pass()
        bot.sales_section()
        bot.new_order()
    elapsed_time = time.time() - start_time
    print(f"Execution time: {elapsed_time} seconds")
