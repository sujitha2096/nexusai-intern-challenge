import asyncio
import time
import random
from dataclasses import dataclass

@dataclass
class CustomerContext:
    crm_data: dict
    billing_data: dict
    tickets: list
    data_complete: bool

async def fetch_crm(phone):
    await asyncio.sleep(0.2)  # Simulate network
    return {"name": "Alex", "plan": "Premium"}

async def fetch_billing(phone):
    if random.random() < 0.1:  # 10% failure rate as per task
        raise Exception("Billing System Timeout")
    await asyncio.sleep(0.3)
    return {"balance": 0, "status": "paid"}

async def fetch_tickets(phone):
    await asyncio.sleep(0.1)
    return [{"id": 101, "status": "open"}]

async def get_customer_context(phone):
    # This runs all 3 functions at the SAME time
    results = await asyncio.gather(
        fetch_crm(phone),
        fetch_billing(phone),
        fetch_tickets(phone),
        return_exceptions=True
    )

    # Check if any failed
    crm = results[0] if not isinstance(results[0], Exception) else None
    billing = results[1] if not isinstance(results[1], Exception) else None
    tickets = results[2] if not isinstance(results[2], Exception) else []

    return CustomerContext(
        crm_data=crm,
        billing_data=billing,
        tickets=tickets,
        data_complete=all([crm, billing])
    )

if __name__ == "__main__":
    start = time.perf_counter()
    context = asyncio.run(get_customer_context("555-0199"))
    print(f"Fetched in {time.perf_counter() - start:.2f}s")
    print(f"Data Complete: {context.data_complete}")